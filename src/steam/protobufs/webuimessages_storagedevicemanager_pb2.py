# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: webuimessages_storagedevicemanager.proto
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
    'webuimessages_storagedevicemanager.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.enums_pb2 as enums__pb2
import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.webuimessages_base_pb2 as webuimessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(webuimessages_storagedevicemanager.proto\x1a\x0b\x65nums.proto\x1a\x18steammessages_base.proto\x1a\x18webuimessages_base.proto\"2\n0CStorageDeviceManager_IsServiceAvailable_Request\"I\n1CStorageDeviceManager_IsServiceAvailable_Response\x12\x14\n\x0cis_available\x18\x01 \x01(\x08\"\xe9\x02\n\x1a\x43StorageDeviceManagerDrive\x12\r\n\x02id\x18\x01 \x01(\r:\x01\x30\x12\r\n\x05model\x18\x02 \x01(\t\x12\x0e\n\x06vendor\x18\x03 \x01(\t\x12\x0e\n\x06serial\x18\x04 \x01(\t\x12\x14\n\x0cis_ejectable\x18\x05 \x01(\x08\x12\x12\n\nsize_bytes\x18\x06 \x01(\x04\x12M\n\nmedia_type\x18\x07 \x01(\x0e\x32\x17.EStorageDriveMediaType: k_EStorageDriveMediaType_Invalid\x12\x16\n\x0eis_unformatted\x18\x08 \x01(\x08\x12H\n\x0b\x61\x64opt_stage\x18\t \x01(\x0e\x32\x14.EStorageFormatStage:\x1dk_EStorageFormatStage_Invalid\x12\x16\n\x0eis_formattable\x18\n \x01(\x08\x12\x1a\n\x12is_media_available\x18\x0b \x01(\x08\"\xce\x03\n CStorageDeviceManagerBlockDevice\x12\r\n\x02id\x18\x01 \x01(\r:\x01\x30\x12\x13\n\x08\x64rive_id\x18\x02 \x01(\r:\x01\x30\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x15\n\rfriendly_path\x18\x04 \x01(\t\x12\r\n\x05label\x18\x05 \x01(\t\x12\x12\n\nsize_bytes\x18\x06 \x01(\x04\x12\x16\n\x0eis_formattable\x18\x07 \x01(\x08\x12\x14\n\x0cis_read_only\x18\x08 \x01(\x08\x12\x16\n\x0eis_root_device\x18\t \x01(\x08\x12S\n\x0c\x63ontent_type\x18\n \x01(\x0e\x32\x19.EStorageBlockContentType:\"k_EStorageBlockContentType_Invalid\x12\\\n\x0f\x66ilesystem_type\x18\x0b \x01(\x0e\x32\x1c.EStorageBlockFileSystemType:%k_EStorageBlockFileSystemType_Invalid\x12\x13\n\x0bmount_paths\x18\x0c \x03(\t\x12\x15\n\ris_unmounting\x18\r \x01(\x08\x12\x19\n\x11has_steam_library\x18\x0e \x01(\x08\"\xf1\x01\n\x1a\x43StorageDeviceManagerState\x12+\n\x06\x64rives\x18\x01 \x03(\x0b\x32\x1b.CStorageDeviceManagerDrive\x12\x38\n\rblock_devices\x18\x02 \x03(\x0b\x32!.CStorageDeviceManagerBlockDevice\x12\x1c\n\x14is_unmount_supported\x18\x03 \x01(\x08\x12\x19\n\x11is_trim_supported\x18\x04 \x01(\x08\x12\x17\n\x0fis_trim_running\x18\x05 \x01(\x08\x12\x1a\n\x12is_adopt_supported\x18\x06 \x01(\x08\"(\n&CStorageDeviceManager_GetState_Request\"U\n\'CStorageDeviceManager_GetState_Response\x12*\n\x05state\x18\x01 \x01(\x0b\x32\x1b.CStorageDeviceManagerState\"1\n/CStorageDeviceManager_StateChanged_Notification\"7\n#CStorageDeviceManager_Eject_Request\x12\x10\n\x08\x64rive_id\x18\x01 \x01(\r\"&\n$CStorageDeviceManager_Eject_Response\"X\n#CStorageDeviceManager_Adopt_Request\x12\x10\n\x08\x64rive_id\x18\x01 \x01(\r\x12\r\n\x05label\x18\x02 \x01(\t\x12\x10\n\x08validate\x18\x03 \x01(\x08\"&\n$CStorageDeviceManager_Adopt_Response\"?\n$CStorageDeviceManager_Format_Request\x12\x17\n\x0f\x62lock_device_id\x18\x01 \x01(\r\"\'\n%CStorageDeviceManager_Format_Response\"@\n%CStorageDeviceManager_Unmount_Request\x12\x17\n\x0f\x62lock_device_id\x18\x01 \x01(\r\"(\n&CStorageDeviceManager_Unmount_Response\"\'\n%CStorageDeviceManager_TrimAll_Request\"(\n&CStorageDeviceManager_TrimAll_Response2\x8f\x06\n\x14StorageDeviceManager\x12{\n\x12IsServiceAvailable\x12\x31.CStorageDeviceManager_IsServiceAvailable_Request\x1a\x32.CStorageDeviceManager_IsServiceAvailable_Response\x12]\n\x08GetState\x12\'.CStorageDeviceManager_GetState_Request\x1a(.CStorageDeviceManager_GetState_Response\x12X\n\x12NotifyStateChanged\x12\x30.CStorageDeviceManager_StateChanged_Notification\x1a\x10.WebUINoResponse\x12T\n\x05\x41\x64opt\x12$.CStorageDeviceManager_Adopt_Request\x1a%.CStorageDeviceManager_Adopt_Response\x12T\n\x05\x45ject\x12$.CStorageDeviceManager_Eject_Request\x1a%.CStorageDeviceManager_Eject_Response\x12W\n\x06\x46ormat\x12%.CStorageDeviceManager_Format_Request\x1a&.CStorageDeviceManager_Format_Response\x12Z\n\x07Unmount\x12&.CStorageDeviceManager_Unmount_Request\x1a\'.CStorageDeviceManager_Unmount_Response\x12Z\n\x07TrimAll\x12&.CStorageDeviceManager_TrimAll_Request\x1a\'.CStorageDeviceManager_TrimAll_Response\x1a\x04\x80\x97\"\x01\x42\x05H\x01\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'webuimessages_storagedevicemanager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\001'
  _globals['_STORAGEDEVICEMANAGER']._loaded_options = None
  _globals['_STORAGEDEVICEMANAGER']._serialized_options = b'\200\227\"\001'
  _globals['_CSTORAGEDEVICEMANAGER_ISSERVICEAVAILABLE_REQUEST']._serialized_start=109
  _globals['_CSTORAGEDEVICEMANAGER_ISSERVICEAVAILABLE_REQUEST']._serialized_end=159
  _globals['_CSTORAGEDEVICEMANAGER_ISSERVICEAVAILABLE_RESPONSE']._serialized_start=161
  _globals['_CSTORAGEDEVICEMANAGER_ISSERVICEAVAILABLE_RESPONSE']._serialized_end=234
  _globals['_CSTORAGEDEVICEMANAGERDRIVE']._serialized_start=237
  _globals['_CSTORAGEDEVICEMANAGERDRIVE']._serialized_end=598
  _globals['_CSTORAGEDEVICEMANAGERBLOCKDEVICE']._serialized_start=601
  _globals['_CSTORAGEDEVICEMANAGERBLOCKDEVICE']._serialized_end=1063
  _globals['_CSTORAGEDEVICEMANAGERSTATE']._serialized_start=1066
  _globals['_CSTORAGEDEVICEMANAGERSTATE']._serialized_end=1307
  _globals['_CSTORAGEDEVICEMANAGER_GETSTATE_REQUEST']._serialized_start=1309
  _globals['_CSTORAGEDEVICEMANAGER_GETSTATE_REQUEST']._serialized_end=1349
  _globals['_CSTORAGEDEVICEMANAGER_GETSTATE_RESPONSE']._serialized_start=1351
  _globals['_CSTORAGEDEVICEMANAGER_GETSTATE_RESPONSE']._serialized_end=1436
  _globals['_CSTORAGEDEVICEMANAGER_STATECHANGED_NOTIFICATION']._serialized_start=1438
  _globals['_CSTORAGEDEVICEMANAGER_STATECHANGED_NOTIFICATION']._serialized_end=1487
  _globals['_CSTORAGEDEVICEMANAGER_EJECT_REQUEST']._serialized_start=1489
  _globals['_CSTORAGEDEVICEMANAGER_EJECT_REQUEST']._serialized_end=1544
  _globals['_CSTORAGEDEVICEMANAGER_EJECT_RESPONSE']._serialized_start=1546
  _globals['_CSTORAGEDEVICEMANAGER_EJECT_RESPONSE']._serialized_end=1584
  _globals['_CSTORAGEDEVICEMANAGER_ADOPT_REQUEST']._serialized_start=1586
  _globals['_CSTORAGEDEVICEMANAGER_ADOPT_REQUEST']._serialized_end=1674
  _globals['_CSTORAGEDEVICEMANAGER_ADOPT_RESPONSE']._serialized_start=1676
  _globals['_CSTORAGEDEVICEMANAGER_ADOPT_RESPONSE']._serialized_end=1714
  _globals['_CSTORAGEDEVICEMANAGER_FORMAT_REQUEST']._serialized_start=1716
  _globals['_CSTORAGEDEVICEMANAGER_FORMAT_REQUEST']._serialized_end=1779
  _globals['_CSTORAGEDEVICEMANAGER_FORMAT_RESPONSE']._serialized_start=1781
  _globals['_CSTORAGEDEVICEMANAGER_FORMAT_RESPONSE']._serialized_end=1820
  _globals['_CSTORAGEDEVICEMANAGER_UNMOUNT_REQUEST']._serialized_start=1822
  _globals['_CSTORAGEDEVICEMANAGER_UNMOUNT_REQUEST']._serialized_end=1886
  _globals['_CSTORAGEDEVICEMANAGER_UNMOUNT_RESPONSE']._serialized_start=1888
  _globals['_CSTORAGEDEVICEMANAGER_UNMOUNT_RESPONSE']._serialized_end=1928
  _globals['_CSTORAGEDEVICEMANAGER_TRIMALL_REQUEST']._serialized_start=1930
  _globals['_CSTORAGEDEVICEMANAGER_TRIMALL_REQUEST']._serialized_end=1969
  _globals['_CSTORAGEDEVICEMANAGER_TRIMALL_RESPONSE']._serialized_start=1971
  _globals['_CSTORAGEDEVICEMANAGER_TRIMALL_RESPONSE']._serialized_end=2011
  _globals['_STORAGEDEVICEMANAGER']._serialized_start=2014
  _globals['_STORAGEDEVICEMANAGER']._serialized_end=2797
_builder.BuildServices(DESCRIPTOR, 'webuimessages_storagedevicemanager_pb2', _globals)
# @@protoc_insertion_point(module_scope)
