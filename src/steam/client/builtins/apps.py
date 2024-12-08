from binascii import hexlify
from typing import Any

import vdf

from steam.core.msg import MsgProto
from steam.enums import EResult
from steam.enums.emsg import EMsg
from steam.protobufs.encrypted_app_ticket_pb2 import EncryptedAppTicket
from steam.protobufs.steammessages_clientserver_2_pb2 import (
    CMsgClientGetCDNAuthTokenResponse,
    CMsgClientGetDepotDecryptionKeyResponse,
)
from steam.protobufs.steammessages_clientserver_appinfo_pb2 import (
    CMsgClientPICSChangesSinceResponse,
)
from steam.protobufs.steammessages_clientserver_pb2 import (
    CMsgClientGetAppOwnershipTicketResponse,
)
from steam.utils.proto import proto_fill_from_dict


class Apps:
    licenses = None  #: :class:`dict` Accounts' package licenses

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.licenses = {}
        self.on(self.EVENT_DISCONNECTED, self.__handle_disconnect)
        self.on(EMsg.ClientLicenseList, self._handle_licenses)

    async def __handle_disconnect(self):
        self.licenses = {}

    async def _handle_licenses(self, message):
        for entry in message.body.licenses:
            self.licenses[entry.package_id] = entry

    async def get_player_count(self, app_id: int, timeout: int = 5) -> int | EResult:
        """Get numbers of players for app id

        :param app_id: app id
        :return: number of players
        :rtype: :class:`int`, :class:`.EResult`
        """
        resp = await self.send_job_and_wait(
            MsgProto(EMsg.ClientGetNumberOfCurrentPlayersDP),
            {'appid': app_id},
            timeout=timeout,
        )
        if resp is None:
            return EResult.Timeout
        elif resp.eresult == EResult.OK:
            return resp.player_count
        else:
            return EResult(resp.eresult)

    async def get_product_info(
        self,
        apps: list,
        packages: list,
        meta_data_only: bool = False,
        raw: bool = False,
        auto_access_tokens: bool = True,
        timeout: int = 15,
    ) -> dict | None:
        """Get product info for apps and packages

        :param apps: items in the list should be either just ``app_id``, or :class:`dict`
        :param packages: items in the list should be either just ``package_id``, or :class:`dict`
        :param meta_data_only: only meta data will be returned in the reponse (e.g. change number, missing_token, sha1)
        :param raw: Data buffer for each app is returned as bytes in its' original form. Apps buffer is text VDF, and package buffer is binary VDF
        :param auto_access_token: automatically request and fill access tokens
        :return: dict with ``apps`` and ``packages`` containing their info, see example below

        .. code:: python

            {'apps':     {570: {...}, ...},
             'packages': {123: {...}, ...}
            }

        Access token is needed to access full information for certain apps, and also package info.
        Each app and package has its' own access token.
        If a token is required then ``_missing_token=True`` in the response.

        App access tokens are obtained by calling :meth:`get_access_tokens`, and are returned only
        when the account has a license for the specified app. Example code:

        .. code:: python

            result = client.get_product_info(apps=[123])

            if result['apps'][123]['_missing_token']:
                tokens = client.get_access_token(apps=[123])

                result = client.get_product_info(apps=[{'appid': 123,
                                                        'access_token': tokens['apps'][123]
                                                        }])

        .. note::
            It is best to just request access token for all apps, before sending a product info
            request.

        Package tokens are located in the account license list. See :attr:`.licenses`

        .. code:: python

            result = client.get_product_info(packages=[{'packageid': 123,
                                                        'access_token': client.licenses[123].access_token,
                                                        }])
        """

        if auto_access_tokens:
            tokens = await self.get_access_tokens(
                app_ids=list(map(lambda app: app['appid'] if isinstance(app, dict) else app, apps)),
                package_ids=list(
                    map(
                        lambda pkg: pkg['packageid'] if isinstance(pkg, dict) else pkg,
                        packages,
                    )
                ),
            )
        else:
            tokens = None

        message = MsgProto(EMsg.ClientPICSProductInfoRequest)

        for app in apps:
            app_info = message.body.apps.add()

            if tokens:
                app_info.access_token = tokens['apps'].get(
                    app['appid'] if isinstance(app, dict) else app, 0
                )

            if isinstance(app, dict):
                proto_fill_from_dict(app_info, app)
            else:
                app_info.appid = app

        for package in packages:
            package_info = message.body.packages.add()

            if tokens:
                package_info.access_token = tokens['packages'].get(
                    package['packageid'] if isinstance(package, dict) else package, 0
                )

            if isinstance(package, dict):
                proto_fill_from_dict(package_info, package)
            else:
                package_info.packageid = package

        message.body.meta_data_only = meta_data_only
        message.body.num_prev_failed = 0
        message.body.supports_package_tokens = 1

        job_id = await self.send_job(message)

        data = dict(apps={}, packages={})

        while True:
            chunk = await self.wait_event(job_id, timeout=timeout, raises=True)

            chunk = chunk[0].body

            for app in chunk.apps:
                if app.buffer and not raw:
                    data['apps'][app.appid] = vdf.loads(app.buffer[:-1].decode('utf-8', 'replace'))[
                        'appinfo'
                    ]
                else:
                    data['apps'][app.appid] = {}

                data['apps'][app.appid]['_missing_token'] = app.missing_token
                data['apps'][app.appid]['_change_number'] = app.change_number
                data['apps'][app.appid]['_sha'] = hexlify(app.sha).decode('ascii')
                data['apps'][app.appid]['_size'] = app.size

                if app.buffer and raw:
                    data['apps'][app.appid]['_buffer'] = app.buffer

            for pkg in chunk.packages:
                if pkg.buffer and not raw:
                    data['packages'][pkg.packageid] = vdf.binary_loads(pkg.buffer[4:]).get(
                        str(pkg.packageid), {}
                    )
                else:
                    data['packages'][pkg.packageid] = {}

                data['packages'][pkg.packageid]['_missing_token'] = pkg.missing_token
                data['packages'][pkg.packageid]['_change_number'] = pkg.change_number
                data['packages'][pkg.packageid]['_sha'] = hexlify(pkg.sha).decode('ascii')
                data['packages'][pkg.packageid]['_size'] = pkg.size

                if pkg.buffer and raw:
                    data['packages'][pkg.packageid]['_buffer'] = pkg.buffer

            if not chunk.response_pending:
                break

        return data

    async def get_changes_since(
        self,
        change_number: int,
        app_changes: bool = True,
        package_changes: bool = False,
    ) -> CMsgClientPICSChangesSinceResponse | None:
        """Get changes since a change number

        :param change_number: change number to use as stating point
        :param app_changes: whether to inclued app changes
        :param package_changes: whether to inclued package changes
        :return: proto message instance, or None on timeout
        """
        return await self.send_job_and_wait(
            MsgProto(EMsg.ClientPICSChangesSinceRequest),
            {
                'since_change_number': change_number,
                'send_app_info_changes': app_changes,
                'send_package_info_changes': package_changes,
            },
            timeout=10,
        )

    async def get_app_ticket(self, app_id: int) -> CMsgClientGetAppOwnershipTicketResponse:
        """Get app ownership ticket

        :param app_id: app id
        :return: proto message
        """
        return await self.send_job_and_wait(
            MsgProto(EMsg.ClientGetAppOwnershipTicket), {'app_id': app_id}, timeout=10
        )

    async def get_encrypted_app_ticket(self, app_id: int, userdata: bytes) -> EncryptedAppTicket:
        """Gets the encrypted app ticket
        :param app_id: app id
        :param userdata: userdata
        :return: proto message
        """
        return await self.send_job_and_wait(
            MsgProto(EMsg.ClientRequestEncryptedAppTicket),
            {'app_id': app_id, 'userdata': userdata},
            timeout=10,
        )

    async def get_depot_key(
        self, app_id: int, depot_id: int
    ) -> CMsgClientGetDepotDecryptionKeyResponse:
        """Get depot decryption key

        :param app_id: app id
        :param depot_id: depot id
        :return: proto message
        """
        return await self.send_job_and_wait(
            MsgProto(EMsg.ClientGetDepotDecryptionKey),
            {
                'app_id': app_id,
                'depot_id': depot_id,
            },
            timeout=10,
        )

    async def get_cdn_auth_token(
        self, depot_id: int, hostname: str
    ) -> CMsgClientGetCDNAuthTokenResponse:
        """Get CDN authentication token

        .. note::
            This token is no longer needed for access to CDN files

        :param depot_id: depot id
        :param hostname: cdn hostname
        :return: proto message
        """
        return await self.send_job_and_wait(
            MsgProto(EMsg.ClientGetCDNAuthToken),
            {
                'depot_id': depot_id,
                'host_name': hostname,
            },
            timeout=10,
        )

    async def get_access_tokens(self, app_ids: list, package_ids: list) -> dict | None:
        """Get access tokens

        :param app_ids: list of app ids
        :param package_ids: list of package ids
        :return: dict with ``apps`` and ``packages`` containing their access tokens, see example below

        .. code:: python

            {'apps':     {123: 8888888886, ...},
             'packages': {456: 6666666666, ...}
            }
        """

        resp = await self.send_job_and_wait(
            MsgProto(EMsg.ClientPICSAccessTokenRequest),
            {
                'appids': map(int, app_ids),
                'packageids': map(int, package_ids),
            },
            timeout=10,
        )

        if resp:
            return {
                'apps': dict(
                    map(
                        lambda app: (app.appid, app.access_token),
                        resp.app_access_tokens,
                    )
                ),
                'packages': dict(
                    map(
                        lambda pkg: (pkg.packageid, pkg.access_token),
                        resp.package_access_tokens,
                    )
                ),
            }

    async def register_product_key(self, key: str) -> tuple[EResult, int | None, Any | None]:
        """Register/Redeem a CD-Key

        :param key: CD-Key
        :type  key: :class:`str`
        :return: format ``(eresult, result_details, receipt_info)``
        :rtype: :class:`tuple`

        Example ``receipt_info``:

        .. code:: python

            {'BasePrice': 0,
              'CurrencyCode': 0,
              'ErrorHeadline': '',
              'ErrorLinkText': '',
              'ErrorLinkURL': '',
              'ErrorString': '',
              'LineItemCount': 1,
              'PaymentMethod': 1,
              'PurchaseStatus': 1,
              'ResultDetail': 0,
              'Shipping': 0,
              'Tax': 0,
              'TotalDiscount': 0,
              'TransactionID': UINT_64(111111111111111111),
              'TransactionTime': 1473000000,
              'lineitems': {'0': {'ItemDescription': 'Half-Life 3',
                'TransactionID': UINT_64(11111111111111111),
                'packageid': 1234}},
              'packageid': -1}
        """
        resp = await self.send_job_and_wait(
            MsgProto(EMsg.ClientRegisterKey),
            {'key': key},
            timeout=30,
        )

        if resp:
            details = vdf.binary_loads(resp.purchase_receipt_info).get('MessageObject', None)
            return EResult(resp.eresult), resp.purchase_result_details, details
        else:
            return EResult.Timeout, None, None

    async def request_free_license(
        self, app_ids: list[int]
    ) -> tuple[EResult, list[int] | None, list[int] | None]:
        """Request license for free app(s)

        :param app_ids: list of app ids
        :return: format (:class:`.EResult`, result_details, receipt_info)
        """
        resp = await self.send_job_and_wait(
            MsgProto(EMsg.ClientRequestFreeLicense),
            {'appids': map(int, app_ids)},
            timeout=10,
        )

        if resp:
            return EResult(resp.eresult), resp.granted_appids, resp.granted_packageids

        else:
            return EResult.Timeout, None, None
