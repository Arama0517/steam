# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_gamerecording_objects.proto
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
    'steammessages_gamerecording_objects.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.enums_pb2 as enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)steammessages_gamerecording_objects.proto\x1a\x0b\x65nums.proto\"\xbc\x02\n0CGameRecording_AudioSessionsChanged_Notification\x12K\n\x08sessions\x18\x01 \x03(\x0b\x32\x39.CGameRecording_AudioSessionsChanged_Notification.Session\x1a\xba\x01\n\x07Session\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tis_system\x18\x03 \x01(\x08\x12\x10\n\x08is_muted\x18\x04 \x01(\x08\x12\x11\n\tis_active\x18\x05 \x01(\x08\x12\x13\n\x0bis_captured\x18\x06 \x01(\x08\x12\x13\n\x0brecent_peak\x18\x07 \x01(\x02\x12\x0f\n\x07is_game\x18\x08 \x01(\x08\x12\x10\n\x08is_steam\x18\t \x01(\x08\x12\x10\n\x08is_saved\x18\n \x01(\x08\x42\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_gamerecording_objects_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_CGAMERECORDING_AUDIOSESSIONSCHANGED_NOTIFICATION']._serialized_start=59
  _globals['_CGAMERECORDING_AUDIOSESSIONSCHANGED_NOTIFICATION']._serialized_end=375
  _globals['_CGAMERECORDING_AUDIOSESSIONSCHANGED_NOTIFICATION_SESSION']._serialized_start=189
  _globals['_CGAMERECORDING_AUDIOSESSIONSCHANGED_NOTIFICATION_SESSION']._serialized_end=375
# @@protoc_insertion_point(module_scope)
