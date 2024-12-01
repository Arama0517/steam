# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: webuimessages_steamengine.proto
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
    'webuimessages_steamengine.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.webuimessages_base_pb2 as webuimessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwebuimessages_steamengine.proto\x1a\x18steammessages_base.proto\x1a\x18webuimessages_base.proto\"V\n4CSteamEngine_UpdateTextFilterDictionary_Notification\x12\x10\n\x08language\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\t\"N\n,CSteamEngine_GetTextFilterDictionary_Request\x12\x10\n\x08language\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\t\"C\n-CSteamEngine_GetTextFilterDictionary_Response\x12\x12\n\ndictionary\x18\x01 \x01(\t\"W\n5CSteamEngine_TextFilterDictionaryChanged_Notification\x12\x10\n\x08language\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\t\"3\n$CSteamEngine_GetGameIDForPID_Request\x12\x0b\n\x03pid\x18\x01 \x01(\r\"7\n%CSteamEngine_GetGameIDForPID_Response\x12\x0e\n\x06gameid\x18\x01 \x01(\x04\"^\n5CSteamEngine_SetOverlayEscapeKeyHandling_Notification\x12\x0e\n\x06gameid\x18\x01 \x02(\x04\x12\x15\n\rshould_handle\x18\x02 \x02(\x08\x32\xae\x04\n\x0bSteamEngine\x12\x65\n\x1aUpdateTextFilterDictionary\x12\x35.CSteamEngine_UpdateTextFilterDictionary_Notification\x1a\x10.WebUINoResponse\x12x\n\x17GetTextFilterDictionary\x12-.CSteamEngine_GetTextFilterDictionary_Request\x1a..CSteamEngine_GetTextFilterDictionary_Response\x12m\n!NotifyTextFilterDictionaryChanged\x12\x36.CSteamEngine_TextFilterDictionaryChanged_Notification\x1a\x10.WebUINoResponse\x12`\n\x0fGetGameIDForPID\x12%.CSteamEngine_GetGameIDForPID_Request\x1a&.CSteamEngine_GetGameIDForPID_Response\x12g\n\x1bSetOverlayEscapeKeyHandling\x12\x36.CSteamEngine_SetOverlayEscapeKeyHandling_Notification\x1a\x10.WebUINoResponse\x1a\x04\x80\x97\"\x02\x42\x05H\x01\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'webuimessages_steamengine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\001'
  _globals['_STEAMENGINE']._loaded_options = None
  _globals['_STEAMENGINE']._serialized_options = b'\200\227\"\002'
  _globals['_CSTEAMENGINE_UPDATETEXTFILTERDICTIONARY_NOTIFICATION']._serialized_start=87
  _globals['_CSTEAMENGINE_UPDATETEXTFILTERDICTIONARY_NOTIFICATION']._serialized_end=173
  _globals['_CSTEAMENGINE_GETTEXTFILTERDICTIONARY_REQUEST']._serialized_start=175
  _globals['_CSTEAMENGINE_GETTEXTFILTERDICTIONARY_REQUEST']._serialized_end=253
  _globals['_CSTEAMENGINE_GETTEXTFILTERDICTIONARY_RESPONSE']._serialized_start=255
  _globals['_CSTEAMENGINE_GETTEXTFILTERDICTIONARY_RESPONSE']._serialized_end=322
  _globals['_CSTEAMENGINE_TEXTFILTERDICTIONARYCHANGED_NOTIFICATION']._serialized_start=324
  _globals['_CSTEAMENGINE_TEXTFILTERDICTIONARYCHANGED_NOTIFICATION']._serialized_end=411
  _globals['_CSTEAMENGINE_GETGAMEIDFORPID_REQUEST']._serialized_start=413
  _globals['_CSTEAMENGINE_GETGAMEIDFORPID_REQUEST']._serialized_end=464
  _globals['_CSTEAMENGINE_GETGAMEIDFORPID_RESPONSE']._serialized_start=466
  _globals['_CSTEAMENGINE_GETGAMEIDFORPID_RESPONSE']._serialized_end=521
  _globals['_CSTEAMENGINE_SETOVERLAYESCAPEKEYHANDLING_NOTIFICATION']._serialized_start=523
  _globals['_CSTEAMENGINE_SETOVERLAYESCAPEKEYHANDLING_NOTIFICATION']._serialized_end=617
  _globals['_STEAMENGINE']._serialized_start=620
  _globals['_STEAMENGINE']._serialized_end=1178
_builder.BuildServices(DESCRIPTOR, 'webuimessages_steamengine_pb2', _globals)
# @@protoc_insertion_point(module_scope)
