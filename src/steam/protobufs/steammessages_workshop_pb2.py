# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_workshop.proto
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
    'steammessages_workshop.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1csteammessages_workshop.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"0\n\x1f\x43Workshop_GetEULAStatus_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"u\n CWorkshop_GetEULAStatus_Response\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x18\n\x10timestamp_action\x18\x02 \x01(\r\x12\x10\n\x08\x61\x63\x63\x65pted\x18\x03 \x01(\x08\x12\x14\n\x0cneeds_action\x18\x04 \x01(\x08\x32`\n\x08Workshop\x12T\n\rGetEULAStatus\x12 .CWorkshop_GetEULAStatus_Request\x1a!.CWorkshop_GetEULAStatus_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_workshop_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CWORKSHOP_GETEULASTATUS_REQUEST']._serialized_start=92
  _globals['_CWORKSHOP_GETEULASTATUS_REQUEST']._serialized_end=140
  _globals['_CWORKSHOP_GETEULASTATUS_RESPONSE']._serialized_start=142
  _globals['_CWORKSHOP_GETEULASTATUS_RESPONSE']._serialized_end=259
  _globals['_WORKSHOP']._serialized_start=261
  _globals['_WORKSHOP']._serialized_end=357
_builder.BuildServices(DESCRIPTOR, 'steammessages_workshop_pb2', _globals)
# @@protoc_insertion_point(module_scope)
