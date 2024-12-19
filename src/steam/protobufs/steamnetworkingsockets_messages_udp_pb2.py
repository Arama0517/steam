# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steamnetworkingsockets_messages_udp.proto
# Protobuf Python Version: 5.29.2
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
    2,
    '',
    'steamnetworkingsockets_messages_udp.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steamnetworkingsockets_messages_certs_pb2 as steamnetworkingsockets__messages__certs__pb2
import steam.protobufs.steamnetworkingsockets_messages_pb2 as steamnetworkingsockets__messages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)steamnetworkingsockets_messages_udp.proto\x1a+steamnetworkingsockets_messages_certs.proto\x1a%steamnetworkingsockets_messages.proto\"n\n%CMsgSteamSockets_UDP_ChallengeRequest\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\x12\x14\n\x0cmy_timestamp\x18\x03 \x01(\x06\x12\x18\n\x10protocol_version\x18\x04 \x01(\r\"\x81\x01\n#CMsgSteamSockets_UDP_ChallengeReply\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\x12\x11\n\tchallenge\x18\x02 \x01(\x06\x12\x16\n\x0eyour_timestamp\x18\x03 \x01(\x06\x12\x18\n\x10protocol_version\x18\x04 \x01(\r\"\x91\x03\n#CMsgSteamSockets_UDP_ConnectRequest\x12\x1c\n\x14\x63lient_connection_id\x18\x01 \x01(\x07\x12\x11\n\tchallenge\x18\x02 \x01(\x06\x12\x14\n\x0cmy_timestamp\x18\x05 \x01(\x06\x12\x13\n\x0bping_est_ms\x18\x06 \x01(\r\x12\x37\n\x05\x63rypt\x18\x07 \x01(\x0b\x32(.CMsgSteamDatagramSessionCryptInfoSigned\x12\x31\n\x04\x63\x65rt\x18\x04 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\x12\x1f\n\x17legacy_protocol_version\x18\x08 \x01(\r\x12\x17\n\x0fidentity_string\x18\n \x01(\t\x12\x1e\n\x16legacy_client_steam_id\x18\x03 \x01(\x06\x12H\n\x16legacy_identity_binary\x18\t \x01(\x0b\x32(.CMsgSteamNetworkingIdentityLegacyBinary\"\xfc\x02\n\x1e\x43MsgSteamSockets_UDP_ConnectOK\x12\x1c\n\x14\x63lient_connection_id\x18\x01 \x01(\x07\x12\x1c\n\x14server_connection_id\x18\x05 \x01(\x07\x12\x16\n\x0eyour_timestamp\x18\x03 \x01(\x06\x12\x17\n\x0f\x64\x65lay_time_usec\x18\x04 \x01(\r\x12\x37\n\x05\x63rypt\x18\x07 \x01(\x0b\x32(.CMsgSteamDatagramSessionCryptInfoSigned\x12\x31\n\x04\x63\x65rt\x18\x08 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\x12\x17\n\x0fidentity_string\x18\x0b \x01(\t\x12\x1e\n\x16legacy_server_steam_id\x18\x02 \x01(\x06\x12H\n\x16legacy_identity_binary\x18\n \x01(\x0b\x32(.CMsgSteamNetworkingIdentityLegacyBinary\"\x81\x01\n%CMsgSteamSockets_UDP_ConnectionClosed\x12\x18\n\x10to_connection_id\x18\x04 \x01(\x07\x12\x1a\n\x12\x66rom_connection_id\x18\x05 \x01(\x07\x12\r\n\x05\x64\x65\x62ug\x18\x02 \x01(\t\x12\x13\n\x0breason_code\x18\x03 \x01(\r\"Y\n!CMsgSteamSockets_UDP_NoConnection\x12\x1a\n\x12\x66rom_connection_id\x18\x02 \x01(\x07\x12\x18\n\x10to_connection_id\x18\x03 \x01(\x07\"\xb7\x01\n\x1a\x43MsgSteamSockets_UDP_Stats\x12\x32\n\x05stats\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\r\n\x05\x66lags\x18\x03 \x01(\r\"V\n\x05\x46lags\x12\x13\n\x0f\x41\x43K_REQUEST_E2E\x10\x02\x12\x19\n\x15\x41\x43K_REQUEST_IMMEDIATE\x10\x04\x12\x1d\n\x19NOT_PRIMARY_TRANSPORT_E2E\x10\x10*\xa5\x02\n\x18\x45SteamNetworkingUDPMsgID\x12-\n)k_ESteamNetworkingUDPMsg_ChallengeRequest\x10 \x12+\n\'k_ESteamNetworkingUDPMsg_ChallengeReply\x10!\x12+\n\'k_ESteamNetworkingUDPMsg_ConnectRequest\x10\"\x12&\n\"k_ESteamNetworkingUDPMsg_ConnectOK\x10#\x12-\n)k_ESteamNetworkingUDPMsg_ConnectionClosed\x10$\x12)\n%k_ESteamNetworkingUDPMsg_NoConnection\x10%B\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steamnetworkingsockets_messages_udp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_ESTEAMNETWORKINGUDPMSGID']._serialized_start=1570
  _globals['_ESTEAMNETWORKINGUDPMSGID']._serialized_end=1863
  _globals['_CMSGSTEAMSOCKETS_UDP_CHALLENGEREQUEST']._serialized_start=129
  _globals['_CMSGSTEAMSOCKETS_UDP_CHALLENGEREQUEST']._serialized_end=239
  _globals['_CMSGSTEAMSOCKETS_UDP_CHALLENGEREPLY']._serialized_start=242
  _globals['_CMSGSTEAMSOCKETS_UDP_CHALLENGEREPLY']._serialized_end=371
  _globals['_CMSGSTEAMSOCKETS_UDP_CONNECTREQUEST']._serialized_start=374
  _globals['_CMSGSTEAMSOCKETS_UDP_CONNECTREQUEST']._serialized_end=775
  _globals['_CMSGSTEAMSOCKETS_UDP_CONNECTOK']._serialized_start=778
  _globals['_CMSGSTEAMSOCKETS_UDP_CONNECTOK']._serialized_end=1158
  _globals['_CMSGSTEAMSOCKETS_UDP_CONNECTIONCLOSED']._serialized_start=1161
  _globals['_CMSGSTEAMSOCKETS_UDP_CONNECTIONCLOSED']._serialized_end=1290
  _globals['_CMSGSTEAMSOCKETS_UDP_NOCONNECTION']._serialized_start=1292
  _globals['_CMSGSTEAMSOCKETS_UDP_NOCONNECTION']._serialized_end=1381
  _globals['_CMSGSTEAMSOCKETS_UDP_STATS']._serialized_start=1384
  _globals['_CMSGSTEAMSOCKETS_UDP_STATS']._serialized_end=1567
  _globals['_CMSGSTEAMSOCKETS_UDP_STATS_FLAGS']._serialized_start=1481
  _globals['_CMSGSTEAMSOCKETS_UDP_STATS_FLAGS']._serialized_end=1567
# @@protoc_insertion_point(module_scope)
