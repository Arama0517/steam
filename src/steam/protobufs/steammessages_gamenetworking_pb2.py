# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_gamenetworking.proto
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
    'steammessages_gamenetworking.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"steammessages_gamenetworking.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"P\n&CGameNetworking_AllocateFakeIP_Request\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x16\n\x0enum_fake_ports\x18\x02 \x01(\r\"N\n\'CGameNetworking_AllocateFakeIP_Response\x12\x0f\n\x07\x66\x61ke_ip\x18\x01 \x01(\x07\x12\x12\n\nfake_ports\x18\x02 \x03(\r\"a\n*CGameNetworking_ReleaseFakeIP_Notification\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x0f\n\x07\x66\x61ke_ip\x18\x02 \x01(\x07\x12\x12\n\nfake_ports\x18\x03 \x03(\r2\xc6\x01\n\x0eGameNetworking\x12\x63\n\x0e\x41llocateFakeIP\x12\'.CGameNetworking_AllocateFakeIP_Request\x1a(.CGameNetworking_AllocateFakeIP_Response\x12O\n\x13NotifyReleaseFakeIP\x12+.CGameNetworking_ReleaseFakeIP_Notification\x1a\x0b.NoResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_gamenetworking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CGAMENETWORKING_ALLOCATEFAKEIP_REQUEST']._serialized_start=98
  _globals['_CGAMENETWORKING_ALLOCATEFAKEIP_REQUEST']._serialized_end=178
  _globals['_CGAMENETWORKING_ALLOCATEFAKEIP_RESPONSE']._serialized_start=180
  _globals['_CGAMENETWORKING_ALLOCATEFAKEIP_RESPONSE']._serialized_end=258
  _globals['_CGAMENETWORKING_RELEASEFAKEIP_NOTIFICATION']._serialized_start=260
  _globals['_CGAMENETWORKING_RELEASEFAKEIP_NOTIFICATION']._serialized_end=357
  _globals['_GAMENETWORKING']._serialized_start=360
  _globals['_GAMENETWORKING']._serialized_end=558
_builder.BuildServices(DESCRIPTOR, 'steammessages_gamenetworking_pb2', _globals)
# @@protoc_insertion_point(module_scope)