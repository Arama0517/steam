# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: webuimessages_gamenotes.proto
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
    'webuimessages_gamenotes.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.webuimessages_base_pb2 as webuimessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dwebuimessages_gamenotes.proto\x1a\x18steammessages_base.proto\x1a\x18webuimessages_base.proto\"V\n\x1e\x43GameNotes_UploadImage_Request\x12\x13\n\x0b\x66ile_prefix\x18\x01 \x01(\t\x12\x11\n\tmime_type\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"3\n\x1f\x43GameNotes_UploadImage_Response\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t2c\n\tGameNotes\x12P\n\x0bUploadImage\x12\x1f.CGameNotes_UploadImage_Request\x1a .CGameNotes_UploadImage_Response\x1a\x04\x80\x97\"\x01\x42\x05H\x01\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'webuimessages_gamenotes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\001'
  _globals['_GAMENOTES']._loaded_options = None
  _globals['_GAMENOTES']._serialized_options = b'\200\227\"\001'
  _globals['_CGAMENOTES_UPLOADIMAGE_REQUEST']._serialized_start=85
  _globals['_CGAMENOTES_UPLOADIMAGE_REQUEST']._serialized_end=171
  _globals['_CGAMENOTES_UPLOADIMAGE_RESPONSE']._serialized_start=173
  _globals['_CGAMENOTES_UPLOADIMAGE_RESPONSE']._serialized_end=224
  _globals['_GAMENOTES']._serialized_start=226
  _globals['_GAMENOTES']._serialized_end=325
_builder.BuildServices(DESCRIPTOR, 'webuimessages_gamenotes_pb2', _globals)
# @@protoc_insertion_point(module_scope)
