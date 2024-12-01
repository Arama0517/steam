# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_gamenetworkingui.proto
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
    'steammessages_gamenetworkingui.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steamnetworkingsockets_messages_pb2 as steamnetworkingsockets__messages__pb2
import steam.protobufs.steamdatagram_messages_sdr_pb2 as steamdatagram__messages__sdr__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$steammessages_gamenetworkingui.proto\x1a%steamnetworkingsockets_messages.proto\x1a steamdatagram_messages_sdr.proto\"\x1f\n\x1d\x43GameNetworkingUI_GlobalState\"\xcf\x07\n!CGameNetworkingUI_ConnectionState\x12\x16\n\x0e\x63onnection_key\x18\x01 \x01(\t\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x1b\n\x13\x63onnection_id_local\x18\x03 \x01(\x07\x12\x16\n\x0eidentity_local\x18\x04 \x01(\t\x12\x17\n\x0fidentity_remote\x18\x05 \x01(\t\x12\x18\n\x10\x63onnection_state\x18\n \x01(\r\x12\x12\n\nstart_time\x18\x0c \x01(\r\x12\x12\n\nclose_time\x18\r \x01(\r\x12\x14\n\x0c\x63lose_reason\x18\x0e \x01(\r\x12\x15\n\rclose_message\x18\x0f \x01(\t\x12\x18\n\x10status_loc_token\x18\x10 \x01(\t\x12\x16\n\x0etransport_kind\x18\x14 \x01(\r\x12\x16\n\x0esdrpopid_local\x18\x15 \x01(\t\x12\x17\n\x0fsdrpopid_remote\x18\x16 \x01(\t\x12\x16\n\x0e\x61\x64\x64ress_remote\x18\x17 \x01(\t\x12\x38\n\x0bp2p_routing\x18\x18 \x01(\x0b\x32#.CMsgSteamDatagramP2PRoutingSummary\x12\x15\n\rping_interior\x18\x19 \x01(\r\x12\x19\n\x11ping_remote_front\x18\x1a \x01(\r\x12#\n\x1bping_default_internet_route\x18\x1b \x01(\r\x12>\n\x11\x65\x32\x65_quality_local\x18\x1e \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12?\n\x12\x65\x32\x65_quality_remote\x18\x1f \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12-\n%e2e_quality_remote_instantaneous_time\x18  \x01(\x04\x12(\n e2e_quality_remote_lifetime_time\x18! \x01(\x04\x12@\n\x13\x66ront_quality_local\x18( \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x41\n\x14\x66ront_quality_remote\x18) \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12/\n\'front_quality_remote_instantaneous_time\x18* \x01(\x04\x12*\n\"front_quality_remote_lifetime_time\x18+ \x01(\x04\"Y\n\x19\x43GameNetworkingUI_Message\x12<\n\x10\x63onnection_state\x18\x01 \x03(\x0b\x32\".CGameNetworkingUI_ConnectionState\"\xe6\x01\n#CGameNetworkingUI_ConnectionSummary\x12\x16\n\x0etransport_kind\x18\x01 \x01(\r\x12\x18\n\x10\x63onnection_state\x18\x08 \x01(\r\x12\x14\n\x0csdrpop_local\x18\x02 \x01(\t\x12\x15\n\rsdrpop_remote\x18\x03 \x01(\t\x12\x0f\n\x07ping_ms\x18\x04 \x01(\r\x12\x13\n\x0bpacket_loss\x18\x05 \x01(\x02\x12#\n\x1bping_default_internet_route\x18\x06 \x01(\r\x12\x15\n\rip_was_shared\x18\x07 \x01(\x08\"\xca\x01\n\x1c\x43GameNetworkingUI_AppSummary\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12!\n\x19ip_was_shared_with_friend\x18\n \x01(\x08\x12$\n\x1cip_was_shared_with_nonfriend\x18\x0b \x01(\x08\x12\x1a\n\x12\x61\x63tive_connections\x18\x14 \x01(\r\x12\x36\n\x08main_cxn\x18\x1e \x01(\x0b\x32$.CGameNetworkingUI_ConnectionSummaryB\x05H\x01\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_gamenetworkingui_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\001'
  _globals['_CGAMENETWORKINGUI_GLOBALSTATE']._serialized_start=113
  _globals['_CGAMENETWORKINGUI_GLOBALSTATE']._serialized_end=144
  _globals['_CGAMENETWORKINGUI_CONNECTIONSTATE']._serialized_start=147
  _globals['_CGAMENETWORKINGUI_CONNECTIONSTATE']._serialized_end=1122
  _globals['_CGAMENETWORKINGUI_MESSAGE']._serialized_start=1124
  _globals['_CGAMENETWORKINGUI_MESSAGE']._serialized_end=1213
  _globals['_CGAMENETWORKINGUI_CONNECTIONSUMMARY']._serialized_start=1216
  _globals['_CGAMENETWORKINGUI_CONNECTIONSUMMARY']._serialized_end=1446
  _globals['_CGAMENETWORKINGUI_APPSUMMARY']._serialized_start=1449
  _globals['_CGAMENETWORKINGUI_APPSUMMARY']._serialized_end=1651
# @@protoc_insertion_point(module_scope)
