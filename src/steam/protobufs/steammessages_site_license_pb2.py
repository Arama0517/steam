# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_site_license.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'steammessages_site_license.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n steammessages_site_license.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"\x8d\x01\n)CSiteManagerClient_IncomingClient_Request\x12\x17\n\x0fsite_instanceid\x18\x01 \x01(\x06\x12\x16\n\x0e\x63lient_steamid\x18\x02 \x01(\x06\x12\x17\n\x0f\x63lient_local_ip\x18\x03 \x01(\x07\x12\x16\n\x0e\x63onnection_key\x18\x04 \x01(\x0c\",\n*CSiteManagerClient_IncomingClient_Response\"N\n,CSiteLicense_ClientSeatCheckout_Notification\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x65result\x18\x02 \x01(\r\"\xe3\x02\n/CSiteManagerClient_TrackedPayments_Notification\x12\x0f\n\x07site_id\x18\x01 \x01(\x06\x12J\n\x08payments\x18\x02 \x03(\x0b\x32\x38.CSiteManagerClient_TrackedPayments_Notification.Payment\x1a\xd2\x01\n\x07Payment\x12\x0f\n\x07transid\x18\x01 \x01(\x04\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x12\x11\n\tecurrency\x18\x04 \x01(\r\x12\x14\n\x0ctime_created\x18\x05 \x01(\x05\x12\x17\n\x0fpurchase_status\x18\x06 \x01(\x05\x12\x14\n\x0cmachine_name\x18\x07 \x01(\t\x12\x14\n\x0cpersona_name\x18\x08 \x01(\t\x12\x13\n\x0bprofile_url\x18\t \x01(\t\x12\x12\n\navatar_url\x18\n \x01(\t\"r\n(CSiteLicense_InitiateAssociation_Request\x12\x14\n\x0csite_steamid\x18\x01 \x01(\x06\x12\x17\n\x0fsite_instanceid\x18\x02 \x01(\x06\x12\x17\n\x0f\x63lient_local_ip\x18\x03 \x01(\x07\"C\n)CSiteLicense_InitiateAssociation_Response\x12\x16\n\x0e\x63onnection_key\x18\x01 \x01(\x0c\":\n$CSiteLicense_LCSAuthenticate_Request\x12\x12\n\ninstanceid\x18\x01 \x01(\x06\"z\n%CSiteLicense_LCSAuthenticate_Response\x12\x0f\n\x07site_id\x18\x01 \x01(\x04\x12\x11\n\tsite_name\x18\x02 \x01(\t\x12\x13\n\x0bnew_session\x18\x03 \x01(\x08\x12\x18\n\x10no_site_licenses\x18\x04 \x01(\x08\"t\n%CSiteLicense_LCSAssociateUser_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x10\n\x08local_ip\x18\x02 \x01(\x07\x12\x12\n\ninstanceid\x18\x03 \x01(\x06\x12\x14\n\x0cmachine_name\x18\x04 \x01(\t\"(\n&CSiteLicense_LCSAssociateUser_Response\"]\n\'CSiteLicense_ClientSeatCheckout_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x12\n\ninstanceid\x18\x02 \x01(\x06\x12\r\n\x05\x61ppid\x18\x03 \x01(\r\"*\n(CSiteLicense_ClientSeatCheckout_Response\"b\n,CSiteLicense_ClientGetAvailableSeats_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x12\n\ninstanceid\x18\x02 \x01(\x06\x12\r\n\x05\x61ppid\x18\x03 \x01(\r\"H\n-CSiteLicense_ClientGetAvailableSeats_Response\x12\x17\n\x0f\x61vailable_seats\x18\x01 \x01(\r2\xc0\x02\n\x11SiteManagerClient\x12i\n\x0eIncomingClient\x12*.CSiteManagerClient_IncomingClient_Request\x1a+.CSiteManagerClient_IncomingClient_Response\x12\\\n\x1e\x43lientSeatCheckoutNotification\x12-.CSiteLicense_ClientSeatCheckout_Notification\x1a\x0b.NoResponse\x12\\\n\x1bTrackedPaymentsNotification\x12\x30.CSiteManagerClient_TrackedPayments_Notification\x1a\x0b.NoResponse\x1a\x04\xc0\xb5\x18\x02\x32\xa7\x04\n\x0bSiteLicense\x12l\n\x13InitiateAssociation\x12).CSiteLicense_InitiateAssociation_Request\x1a*.CSiteLicense_InitiateAssociation_Response\x12`\n\x0fLCSAuthenticate\x12%.CSiteLicense_LCSAuthenticate_Request\x1a&.CSiteLicense_LCSAuthenticate_Response\x12\x63\n\x10LCSAssociateUser\x12&.CSiteLicense_LCSAssociateUser_Request\x1a\'.CSiteLicense_LCSAssociateUser_Response\x12i\n\x12\x43lientSeatCheckout\x12(.CSiteLicense_ClientSeatCheckout_Request\x1a).CSiteLicense_ClientSeatCheckout_Response\x12x\n\x17\x43lientGetAvailableSeats\x12-.CSiteLicense_ClientGetAvailableSeats_Request\x1a..CSiteLicense_ClientGetAvailableSeats_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_site_license_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_SITEMANAGERCLIENT']._loaded_options = None
  _globals['_SITEMANAGERCLIENT']._serialized_options = b'\300\265\030\002'
  _globals['_CSITEMANAGERCLIENT_INCOMINGCLIENT_REQUEST']._serialized_start=97
  _globals['_CSITEMANAGERCLIENT_INCOMINGCLIENT_REQUEST']._serialized_end=238
  _globals['_CSITEMANAGERCLIENT_INCOMINGCLIENT_RESPONSE']._serialized_start=240
  _globals['_CSITEMANAGERCLIENT_INCOMINGCLIENT_RESPONSE']._serialized_end=284
  _globals['_CSITELICENSE_CLIENTSEATCHECKOUT_NOTIFICATION']._serialized_start=286
  _globals['_CSITELICENSE_CLIENTSEATCHECKOUT_NOTIFICATION']._serialized_end=364
  _globals['_CSITEMANAGERCLIENT_TRACKEDPAYMENTS_NOTIFICATION']._serialized_start=367
  _globals['_CSITEMANAGERCLIENT_TRACKEDPAYMENTS_NOTIFICATION']._serialized_end=722
  _globals['_CSITEMANAGERCLIENT_TRACKEDPAYMENTS_NOTIFICATION_PAYMENT']._serialized_start=512
  _globals['_CSITEMANAGERCLIENT_TRACKEDPAYMENTS_NOTIFICATION_PAYMENT']._serialized_end=722
  _globals['_CSITELICENSE_INITIATEASSOCIATION_REQUEST']._serialized_start=724
  _globals['_CSITELICENSE_INITIATEASSOCIATION_REQUEST']._serialized_end=838
  _globals['_CSITELICENSE_INITIATEASSOCIATION_RESPONSE']._serialized_start=840
  _globals['_CSITELICENSE_INITIATEASSOCIATION_RESPONSE']._serialized_end=907
  _globals['_CSITELICENSE_LCSAUTHENTICATE_REQUEST']._serialized_start=909
  _globals['_CSITELICENSE_LCSAUTHENTICATE_REQUEST']._serialized_end=967
  _globals['_CSITELICENSE_LCSAUTHENTICATE_RESPONSE']._serialized_start=969
  _globals['_CSITELICENSE_LCSAUTHENTICATE_RESPONSE']._serialized_end=1091
  _globals['_CSITELICENSE_LCSASSOCIATEUSER_REQUEST']._serialized_start=1093
  _globals['_CSITELICENSE_LCSASSOCIATEUSER_REQUEST']._serialized_end=1209
  _globals['_CSITELICENSE_LCSASSOCIATEUSER_RESPONSE']._serialized_start=1211
  _globals['_CSITELICENSE_LCSASSOCIATEUSER_RESPONSE']._serialized_end=1251
  _globals['_CSITELICENSE_CLIENTSEATCHECKOUT_REQUEST']._serialized_start=1253
  _globals['_CSITELICENSE_CLIENTSEATCHECKOUT_REQUEST']._serialized_end=1346
  _globals['_CSITELICENSE_CLIENTSEATCHECKOUT_RESPONSE']._serialized_start=1348
  _globals['_CSITELICENSE_CLIENTSEATCHECKOUT_RESPONSE']._serialized_end=1390
  _globals['_CSITELICENSE_CLIENTGETAVAILABLESEATS_REQUEST']._serialized_start=1392
  _globals['_CSITELICENSE_CLIENTGETAVAILABLESEATS_REQUEST']._serialized_end=1490
  _globals['_CSITELICENSE_CLIENTGETAVAILABLESEATS_RESPONSE']._serialized_start=1492
  _globals['_CSITELICENSE_CLIENTGETAVAILABLESEATS_RESPONSE']._serialized_end=1564
  _globals['_SITEMANAGERCLIENT']._serialized_start=1567
  _globals['_SITEMANAGERCLIENT']._serialized_end=1887
  _globals['_SITELICENSE']._serialized_start=1890
  _globals['_SITELICENSE']._serialized_end=2441
_builder.BuildServices(DESCRIPTOR, 'steammessages_site_license_pb2', _globals)
# @@protoc_insertion_point(module_scope)
