# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_remoteclient_discovery.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'steammessages_remoteclient_discovery.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*steammessages_remoteclient_discovery.proto\"\xcf\x01\n\x1f\x43MsgRemoteClientBroadcastHeader\x12\x11\n\tclient_id\x18\x01 \x01(\x04\x12R\n\x08msg_type\x18\x02 \x01(\x0e\x32\x1a.ERemoteClientBroadcastMsg:$k_ERemoteClientBroadcastMsgDiscovery\x12\x13\n\x0binstance_id\x18\x03 \x01(\x04\x12\x1a\n\x12\x64\x65vice_id_OBSOLETE\x18\x04 \x01(\x04\x12\x14\n\x0c\x64\x65vice_token\x18\x05 \x01(\x0c\"\xb6\x05\n\x1f\x43MsgRemoteClientBroadcastStatus\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x13\n\x0bmin_version\x18\x02 \x01(\x05\x12\x14\n\x0c\x63onnect_port\x18\x03 \x01(\r\x12\x10\n\x08hostname\x18\x04 \x01(\t\x12\x18\n\x10\x65nabled_services\x18\x06 \x01(\r\x12\x11\n\x06ostype\x18\x07 \x01(\x05:\x01\x30\x12\x0f\n\x07is64bit\x18\x08 \x01(\x08\x12\x34\n\x05users\x18\t \x03(\x0b\x32%.CMsgRemoteClientBroadcastStatus.User\x12\x11\n\teuniverse\x18\x0b \x01(\x05\x12\x11\n\ttimestamp\x18\x0c \x01(\r\x12\x15\n\rscreen_locked\x18\r \x01(\x08\x12\x15\n\rgames_running\x18\x0e \x01(\x08\x12\x15\n\rmac_addresses\x18\x0f \x03(\t\x12\x1f\n\x17\x64ownload_lan_peer_group\x18\x10 \x01(\r\x12\x1b\n\x13\x62roadcasting_active\x18\x11 \x01(\x08\x12\x11\n\tvr_active\x18\x12 \x01(\x08\x12\x1a\n\x12\x63ontent_cache_port\x18\x13 \x01(\r\x12\x14\n\x0cip_addresses\x18\x14 \x03(\t\x12\x19\n\x11public_ip_address\x18\x15 \x01(\t\x12\x19\n\x11remoteplay_active\x18\x16 \x01(\x08\x12\x1a\n\x12supported_services\x18\x17 \x01(\r\x12\x12\n\nsteam_deck\x18\x18 \x01(\x08\x12\x15\n\rsteam_version\x18\x19 \x01(\x04\x12\x38\n\x0cvr_link_caps\x18\x1a \x01(\x0e\x32\x0c.EVRLinkCaps:\x14k_EVRLinkCapsUnknown\x1a,\n\x04User\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x13\n\x0b\x61uth_key_id\x18\x02 \x01(\r\"I\n\"CMsgRemoteClientBroadcastDiscovery\x12\x0f\n\x07seq_num\x18\x01 \x01(\r\x12\x12\n\nclient_ids\x18\x02 \x03(\x04\"A\n+CMsgRemoteClientBroadcastClientIDDeconflict\x12\x12\n\nclient_ids\x18\x02 \x03(\x04\"\xf5\x03\n$CMsgRemoteDeviceAuthorizationRequest\x12\x14\n\x0c\x64\x65vice_token\x18\x01 \x02(\x0c\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x19\n\x11\x65ncrypted_request\x18\x03 \x02(\x0c\x12\x10\n\x08\x61uth_key\x18\x04 \x01(\x0c\x12\x12\n\nrequest_id\x18\x05 \x01(\r\x1a\xa7\x02\n\x11\x43KeyEscrow_Ticket\x12\x10\n\x08password\x18\x01 \x01(\x0c\x12\x12\n\nidentifier\x18\x02 \x01(\x04\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\r\x12\x66\n\x05usage\x18\x05 \x01(\x0e\x32\x35.CMsgRemoteDeviceAuthorizationRequest.EKeyEscrowUsage: k_EKeyEscrowUsageStreamingDevice\x12\x13\n\x0b\x64\x65vice_name\x18\x06 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x07 \x01(\t\x12\x15\n\rdevice_serial\x18\x08 \x01(\t\x12\x1e\n\x16\x64\x65vice_provisioning_id\x18\t \x01(\r\"7\n\x0f\x45KeyEscrowUsage\x12$\n k_EKeyEscrowUsageStreamingDevice\x10\x00\",\n*CMsgRemoteDeviceAuthorizationCancelRequest\"\xb8\x01\n%CMsgRemoteDeviceAuthorizationResponse\x12V\n\x06result\x18\x01 \x02(\x0e\x32!.ERemoteDeviceAuthorizationResult:#k_ERemoteDeviceAuthorizationSuccess\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\x12\x10\n\x08\x61uth_key\x18\x03 \x01(\x0c\x12\x14\n\x0c\x64\x65vice_token\x18\x04 \x01(\x0c\"\x80\x01\n&CMsgRemoteDeviceAuthorizationConfirmed\x12V\n\x06result\x18\x01 \x02(\x0e\x32!.ERemoteDeviceAuthorizationResult:#k_ERemoteDeviceAuthorizationSuccess\"\x91\x06\n CMsgRemoteDeviceStreamingRequest\x12\x12\n\nrequest_id\x18\x01 \x02(\r\x12\x1c\n\x14maximum_resolution_x\x18\x02 \x01(\x05\x12\x1c\n\x14maximum_resolution_y\x18\x03 \x01(\x05\x12\x1e\n\x13\x61udio_channel_count\x18\x04 \x01(\x05:\x01\x32\x12\x16\n\x0e\x64\x65vice_version\x18\x05 \x01(\t\x12\x16\n\x0estream_desktop\x18\x06 \x01(\x08\x12\x14\n\x0c\x64\x65vice_token\x18\x07 \x01(\x0c\x12\x0b\n\x03pin\x18\x08 \x01(\x0c\x12$\n\x16\x65nable_video_streaming\x18\t \x01(\x08:\x04true\x12$\n\x16\x65nable_audio_streaming\x18\n \x01(\x08:\x04true\x12$\n\x16\x65nable_input_streaming\x18\x0b \x01(\x08:\x04true\x12\x14\n\x0cnetwork_test\x18\x0c \x01(\x08\x12\x11\n\tclient_id\x18\r \x01(\x04\x12.\n\x13supported_transport\x18\x0e \x03(\x0e\x32\x11.EStreamTransport\x12\x12\n\nrestricted\x18\x0f \x01(\x08\x12O\n\x0b\x66orm_factor\x18\x10 \x01(\x0e\x32\x18.EStreamDeviceFormFactor: k_EStreamDeviceFormFactorUnknown\x12\x15\n\rgamepad_count\x18\x11 \x01(\x05\x12\x43\n\x08gamepads\x18\x12 \x03(\x0b\x32\x31.CMsgRemoteDeviceStreamingRequest.ReservedGamepad\x12\x0e\n\x06gameid\x18\x13 \x01(\x04\x12\x46\n\x10stream_interface\x18\x14 \x01(\x0e\x32\x11.EStreamInterface:\x19k_EStreamInterfaceDefault\x1a\x46\n\x0fReservedGamepad\x12\x17\n\x0f\x63ontroller_type\x18\x01 \x01(\r\x12\x1a\n\x12\x63ontroller_subtype\x18\x02 \x01(\r\"<\n&CMsgRemoteDeviceStreamingCancelRequest\x12\x12\n\nrequest_id\x18\x01 \x02(\r\"I\n!CMsgRemoteDeviceStreamingProgress\x12\x12\n\nrequest_id\x18\x01 \x02(\r\x12\x10\n\x08progress\x18\x02 \x01(\x02\"\x95\x02\n!CMsgRemoteDeviceStreamingResponse\x12\x12\n\nrequest_id\x18\x01 \x02(\r\x12N\n\x06result\x18\x02 \x02(\x0e\x32\x1d.ERemoteDeviceStreamingResult:\x1fk_ERemoteDeviceStreamingSuccess\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x1d\n\x15\x65ncrypted_session_key\x18\x04 \x01(\x0c\x12;\n\ttransport\x18\x06 \x01(\x0e\x32\x11.EStreamTransport:\x15k_EStreamTransportUDP\x12\x14\n\x0crelay_server\x18\x07 \x01(\t\x12\x0c\n\x04\x63\x65rt\x18\x08 \x01(\t\"\\\n\x1c\x43MsgRemoteDeviceProofRequest\x12\x11\n\tchallenge\x18\x01 \x02(\x0c\x12\x12\n\nrequest_id\x18\x02 \x01(\r\x12\x15\n\rupdate_secret\x18\x03 \x01(\x08\"]\n\x1d\x43MsgRemoteDeviceProofResponse\x12\x10\n\x08response\x18\x01 \x02(\x0c\x12\x12\n\nrequest_id\x18\x02 \x01(\r\x12\x16\n\x0eupdated_secret\x18\x03 \x01(\x08\"G\n%CMsgRemoteDeviceStreamTransportSignal\x12\r\n\x05token\x18\x01 \x01(\x0c\x12\x0f\n\x07payload\x18\x02 \x01(\x0c*\xfd\x04\n\x19\x45RemoteClientBroadcastMsg\x12(\n$k_ERemoteClientBroadcastMsgDiscovery\x10\x00\x12%\n!k_ERemoteClientBroadcastMsgStatus\x10\x01\x12&\n\"k_ERemoteClientBroadcastMsgOffline\x10\x02\x12\'\n#k_ERemoteDeviceAuthorizationRequest\x10\x03\x12(\n$k_ERemoteDeviceAuthorizationResponse\x10\x04\x12#\n\x1fk_ERemoteDeviceStreamingRequest\x10\x05\x12$\n k_ERemoteDeviceStreamingResponse\x10\x06\x12\x1f\n\x1bk_ERemoteDeviceProofRequest\x10\x07\x12 \n\x1ck_ERemoteDeviceProofResponse\x10\x08\x12-\n)k_ERemoteDeviceAuthorizationCancelRequest\x10\t\x12)\n%k_ERemoteDeviceStreamingCancelRequest\x10\n\x12\x31\n-k_ERemoteClientBroadcastMsgClientIDDeconflict\x10\x0b\x12(\n$k_ERemoteDeviceStreamTransportSignal\x10\x0c\x12$\n k_ERemoteDeviceStreamingProgress\x10\r\x12)\n%k_ERemoteDeviceAuthorizationConfirmed\x10\x0e*\x80\x02\n\x14\x45RemoteClientService\x12\x1e\n\x1ak_ERemoteClientServiceNone\x10\x00\x12\'\n#k_ERemoteClientServiceRemoteControl\x10\x01\x12\'\n#k_ERemoteClientServiceGameStreaming\x10\x02\x12%\n!k_ERemoteClientServiceSiteLicense\x10\x04\x12&\n\"k_ERemoteClientServiceContentCache\x10\x08\x12\'\n#k_ERemoteClientServiceContentServer\x10\x10*\x8d\x01\n\x0b\x45VRLinkCaps\x12\x18\n\x14k_EVRLinkCapsUnknown\x10\x00\x12\x1a\n\x16k_EVRLinkCapsAvailable\x10\x01\x12\x1e\n\x1ak_EVRLinkCapsUnimplemented\x10\x02\x12(\n$k_EVRLinkCapsMissingHardwareEncoding\x10\x03*\x97\x03\n ERemoteDeviceAuthorizationResult\x12\'\n#k_ERemoteDeviceAuthorizationSuccess\x10\x00\x12&\n\"k_ERemoteDeviceAuthorizationDenied\x10\x01\x12+\n\'k_ERemoteDeviceAuthorizationNotLoggedIn\x10\x02\x12\'\n#k_ERemoteDeviceAuthorizationOffline\x10\x03\x12$\n k_ERemoteDeviceAuthorizationBusy\x10\x04\x12*\n&k_ERemoteDeviceAuthorizationInProgress\x10\x05\x12(\n$k_ERemoteDeviceAuthorizationTimedOut\x10\x06\x12&\n\"k_ERemoteDeviceAuthorizationFailed\x10\x07\x12(\n$k_ERemoteDeviceAuthorizationCanceled\x10\x08*\xf8\x01\n\x17\x45StreamDeviceFormFactor\x12$\n k_EStreamDeviceFormFactorUnknown\x10\x00\x12\"\n\x1ek_EStreamDeviceFormFactorPhone\x10\x01\x12#\n\x1fk_EStreamDeviceFormFactorTablet\x10\x02\x12%\n!k_EStreamDeviceFormFactorComputer\x10\x03\x12\x1f\n\x1bk_EStreamDeviceFormFactorTV\x10\x04\x12&\n\"k_EStreamDeviceFormFactorVRHeadset\x10\x05*\xee\x01\n\x10\x45StreamTransport\x12\x1a\n\x16k_EStreamTransportNone\x10\x00\x12\x19\n\x15k_EStreamTransportUDP\x10\x01\x12\x1e\n\x1ak_EStreamTransportUDPRelay\x10\x02\x12%\n!k_EStreamTransportWebRTC_OBSOLETE\x10\x03\x12\x19\n\x15k_EStreamTransportSDR\x10\x04\x12\x1d\n\x19k_EStreamTransportUDP_SNS\x10\x05\x12\"\n\x1ek_EStreamTransportUDPRelay_SNS\x10\x06*\xb4\x01\n\x10\x45StreamInterface\x12\x1d\n\x19k_EStreamInterfaceDefault\x10\x00\x12!\n\x1dk_EStreamInterfaceRecentGames\x10\x01\x12 \n\x1ck_EStreamInterfaceBigPicture\x10\x02\x12\x1d\n\x19k_EStreamInterfaceDesktop\x10\x03\x12\x1d\n\x19k_EStreamInterfaceSteamVR\x10\x04*\xb9\x05\n\x1c\x45RemoteDeviceStreamingResult\x12#\n\x1fk_ERemoteDeviceStreamingSuccess\x10\x00\x12(\n$k_ERemoteDeviceStreamingUnauthorized\x10\x01\x12(\n$k_ERemoteDeviceStreamingScreenLocked\x10\x02\x12\"\n\x1ek_ERemoteDeviceStreamingFailed\x10\x03\x12 \n\x1ck_ERemoteDeviceStreamingBusy\x10\x04\x12&\n\"k_ERemoteDeviceStreamingInProgress\x10\x05\x12$\n k_ERemoteDeviceStreamingCanceled\x10\x06\x12/\n+k_ERemoteDeviceStreamingDriversNotInstalled\x10\x07\x12$\n k_ERemoteDeviceStreamingDisabled\x10\x08\x12.\n*k_ERemoteDeviceStreamingBroadcastingActive\x10\t\x12$\n k_ERemoteDeviceStreamingVRActive\x10\n\x12\'\n#k_ERemoteDeviceStreamingPINRequired\x10\x0b\x12\x30\n,k_ERemoteDeviceStreamingTransportUnavailable\x10\x0c\x12%\n!k_ERemoteDeviceStreamingInvisible\x10\r\x12,\n(k_ERemoteDeviceStreamingGameLaunchFailed\x10\x0e\x12/\n+k_ERemoteDeviceStreamingSteamVRNotInstalled\x10\x0f\x42\x02H\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_remoteclient_discovery_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001'
  _globals['_EREMOTECLIENTBROADCASTMSG']._serialized_start=3431
  _globals['_EREMOTECLIENTBROADCASTMSG']._serialized_end=4068
  _globals['_EREMOTECLIENTSERVICE']._serialized_start=4071
  _globals['_EREMOTECLIENTSERVICE']._serialized_end=4327
  _globals['_EVRLINKCAPS']._serialized_start=4330
  _globals['_EVRLINKCAPS']._serialized_end=4471
  _globals['_EREMOTEDEVICEAUTHORIZATIONRESULT']._serialized_start=4474
  _globals['_EREMOTEDEVICEAUTHORIZATIONRESULT']._serialized_end=4881
  _globals['_ESTREAMDEVICEFORMFACTOR']._serialized_start=4884
  _globals['_ESTREAMDEVICEFORMFACTOR']._serialized_end=5132
  _globals['_ESTREAMTRANSPORT']._serialized_start=5135
  _globals['_ESTREAMTRANSPORT']._serialized_end=5373
  _globals['_ESTREAMINTERFACE']._serialized_start=5376
  _globals['_ESTREAMINTERFACE']._serialized_end=5556
  _globals['_EREMOTEDEVICESTREAMINGRESULT']._serialized_start=5559
  _globals['_EREMOTEDEVICESTREAMINGRESULT']._serialized_end=6256
  _globals['_CMSGREMOTECLIENTBROADCASTHEADER']._serialized_start=47
  _globals['_CMSGREMOTECLIENTBROADCASTHEADER']._serialized_end=254
  _globals['_CMSGREMOTECLIENTBROADCASTSTATUS']._serialized_start=257
  _globals['_CMSGREMOTECLIENTBROADCASTSTATUS']._serialized_end=951
  _globals['_CMSGREMOTECLIENTBROADCASTSTATUS_USER']._serialized_start=907
  _globals['_CMSGREMOTECLIENTBROADCASTSTATUS_USER']._serialized_end=951
  _globals['_CMSGREMOTECLIENTBROADCASTDISCOVERY']._serialized_start=953
  _globals['_CMSGREMOTECLIENTBROADCASTDISCOVERY']._serialized_end=1026
  _globals['_CMSGREMOTECLIENTBROADCASTCLIENTIDDECONFLICT']._serialized_start=1028
  _globals['_CMSGREMOTECLIENTBROADCASTCLIENTIDDECONFLICT']._serialized_end=1093
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONREQUEST']._serialized_start=1096
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONREQUEST']._serialized_end=1597
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONREQUEST_CKEYESCROW_TICKET']._serialized_start=1245
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONREQUEST_CKEYESCROW_TICKET']._serialized_end=1540
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONREQUEST_EKEYESCROWUSAGE']._serialized_start=1542
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONREQUEST_EKEYESCROWUSAGE']._serialized_end=1597
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONCANCELREQUEST']._serialized_start=1599
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONCANCELREQUEST']._serialized_end=1643
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONRESPONSE']._serialized_start=1646
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONRESPONSE']._serialized_end=1830
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONCONFIRMED']._serialized_start=1833
  _globals['_CMSGREMOTEDEVICEAUTHORIZATIONCONFIRMED']._serialized_end=1961
  _globals['_CMSGREMOTEDEVICESTREAMINGREQUEST']._serialized_start=1964
  _globals['_CMSGREMOTEDEVICESTREAMINGREQUEST']._serialized_end=2749
  _globals['_CMSGREMOTEDEVICESTREAMINGREQUEST_RESERVEDGAMEPAD']._serialized_start=2679
  _globals['_CMSGREMOTEDEVICESTREAMINGREQUEST_RESERVEDGAMEPAD']._serialized_end=2749
  _globals['_CMSGREMOTEDEVICESTREAMINGCANCELREQUEST']._serialized_start=2751
  _globals['_CMSGREMOTEDEVICESTREAMINGCANCELREQUEST']._serialized_end=2811
  _globals['_CMSGREMOTEDEVICESTREAMINGPROGRESS']._serialized_start=2813
  _globals['_CMSGREMOTEDEVICESTREAMINGPROGRESS']._serialized_end=2886
  _globals['_CMSGREMOTEDEVICESTREAMINGRESPONSE']._serialized_start=2889
  _globals['_CMSGREMOTEDEVICESTREAMINGRESPONSE']._serialized_end=3166
  _globals['_CMSGREMOTEDEVICEPROOFREQUEST']._serialized_start=3168
  _globals['_CMSGREMOTEDEVICEPROOFREQUEST']._serialized_end=3260
  _globals['_CMSGREMOTEDEVICEPROOFRESPONSE']._serialized_start=3262
  _globals['_CMSGREMOTEDEVICEPROOFRESPONSE']._serialized_end=3355
  _globals['_CMSGREMOTEDEVICESTREAMTRANSPORTSIGNAL']._serialized_start=3357
  _globals['_CMSGREMOTEDEVICESTREAMTRANSPORTSIGNAL']._serialized_end=3428
# @@protoc_insertion_point(module_scope)
