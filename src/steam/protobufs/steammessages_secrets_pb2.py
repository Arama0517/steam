# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_secrets.proto
# Protobuf Python Version: 5.29.1
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
    1,
    '',
    'steammessages_secrets.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bsteammessages_secrets.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"\x9b\x01\n\x12\x43KeyEscrow_Request\x12\x1b\n\x13rsa_oaep_sha_ticket\x18\x01 \x01(\x0c\x12\x10\n\x08password\x18\x02 \x01(\x0c\x12\x41\n\x05usage\x18\x03 \x01(\x0e\x32\x10.EKeyEscrowUsage: k_EKeyEscrowUsageStreamingDevice\x12\x13\n\x0b\x64\x65vice_name\x18\x04 \x01(\t\"\x82\x02\n\x11\x43KeyEscrow_Ticket\x12\x10\n\x08password\x18\x01 \x01(\x0c\x12\x12\n\nidentifier\x18\x02 \x01(\x04\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\r\x12\x41\n\x05usage\x18\x05 \x01(\x0e\x32\x10.EKeyEscrowUsage: k_EKeyEscrowUsageStreamingDevice\x12\x13\n\x0b\x64\x65vice_name\x18\x06 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x07 \x01(\t\x12\x15\n\rdevice_serial\x18\x08 \x01(\t\x12\x1e\n\x16\x64\x65vice_provisioning_id\x18\t \x01(\r\"9\n\x13\x43KeyEscrow_Response\x12\"\n\x06ticket\x18\x01 \x01(\x0b\x32\x12.CKeyEscrow_Ticket*7\n\x0f\x45KeyEscrowUsage\x12$\n k_EKeyEscrowUsageStreamingDevice\x10\x00\x32\x41\n\x07Secrets\x12\x36\n\tKeyEscrow\x12\x13.CKeyEscrow_Request\x1a\x14.CKeyEscrow_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_secrets_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_EKEYESCROWUSAGE']._serialized_start=569
  _globals['_EKEYESCROWUSAGE']._serialized_end=624
  _globals['_CKEYESCROW_REQUEST']._serialized_start=92
  _globals['_CKEYESCROW_REQUEST']._serialized_end=247
  _globals['_CKEYESCROW_TICKET']._serialized_start=250
  _globals['_CKEYESCROW_TICKET']._serialized_end=508
  _globals['_CKEYESCROW_RESPONSE']._serialized_start=510
  _globals['_CKEYESCROW_RESPONSE']._serialized_end=567
  _globals['_SECRETS']._serialized_start=626
  _globals['_SECRETS']._serialized_end=691
_builder.BuildServices(DESCRIPTOR, 'steammessages_secrets_pb2', _globals)
# @@protoc_insertion_point(module_scope)
