# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_market.proto
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
    'steammessages_market.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asteammessages_market.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"=\n(CEconMarket_IsMarketplaceAllowed_Request\x12\x11\n\twebcookie\x18\x01 \x01(\t\"\xe6\x01\n)CEconMarket_IsMarketplaceAllowed_Response\x12\x0f\n\x07\x61llowed\x18\x01 \x01(\x08\x12\x0e\n\x06reason\x18\x02 \x01(\r\x12\x17\n\x0f\x61llowed_at_time\x18\x03 \x01(\r\x12 \n\x18steamguard_required_days\x18\x04 \x01(\r\x12\x17\n\x0f\x66orms_requested\x18\x07 \x01(\x08\x12\"\n\x1a\x66orms_require_verification\x18\x08 \x01(\x08\x12 \n\x18new_device_cooldown_days\x18\t \x01(\r2{\n\nEconMarket\x12m\n\x14IsMarketplaceAllowed\x12).CEconMarket_IsMarketplaceAllowed_Request\x1a*.CEconMarket_IsMarketplaceAllowed_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_market_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_REQUEST']._serialized_start=90
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_REQUEST']._serialized_end=151
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE']._serialized_start=154
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE']._serialized_end=384
  _globals['_ECONMARKET']._serialized_start=386
  _globals['_ECONMARKET']._serialized_end=509
_builder.BuildServices(DESCRIPTOR, 'steammessages_market_pb2', _globals)
# @@protoc_insertion_point(module_scope)
