# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: content_manifest.proto
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
    'content_manifest.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63ontent_manifest.proto\"\xef\x02\n\x16\x43ontentManifestPayload\x12\x35\n\x08mappings\x18\x01 \x03(\x0b\x32#.ContentManifestPayload.FileMapping\x1a\x9d\x02\n\x0b\x46ileMapping\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\r\n\x05\x66lags\x18\x03 \x01(\r\x12\x14\n\x0csha_filename\x18\x04 \x01(\x0c\x12\x13\n\x0bsha_content\x18\x05 \x01(\x0c\x12=\n\x06\x63hunks\x18\x06 \x03(\x0b\x32-.ContentManifestPayload.FileMapping.ChunkData\x12\x12\n\nlinktarget\x18\x07 \x01(\t\x1a\x61\n\tChunkData\x12\x0b\n\x03sha\x18\x01 \x01(\x0c\x12\x0b\n\x03\x63rc\x18\x02 \x01(\x07\x12\x0e\n\x06offset\x18\x03 \x01(\x04\x12\x13\n\x0b\x63\x62_original\x18\x04 \x01(\r\x12\x15\n\rcb_compressed\x18\x05 \x01(\r\"\xec\x01\n\x17\x43ontentManifestMetadata\x12\x10\n\x08\x64\x65pot_id\x18\x01 \x01(\r\x12\x14\n\x0cgid_manifest\x18\x02 \x01(\x04\x12\x15\n\rcreation_time\x18\x03 \x01(\r\x12\x1b\n\x13\x66ilenames_encrypted\x18\x04 \x01(\x08\x12\x18\n\x10\x63\x62_disk_original\x18\x05 \x01(\x04\x12\x1a\n\x12\x63\x62_disk_compressed\x18\x06 \x01(\x04\x12\x15\n\runique_chunks\x18\x07 \x01(\r\x12\x15\n\rcrc_encrypted\x18\x08 \x01(\r\x12\x11\n\tcrc_clear\x18\t \x01(\r\"-\n\x18\x43ontentManifestSignature\x12\x11\n\tsignature\x18\x01 \x01(\x0c\"\x84\x03\n\x12\x43ontentDeltaChunks\x12\x10\n\x08\x64\x65pot_id\x18\x01 \x01(\r\x12\x1a\n\x12manifest_id_source\x18\x02 \x01(\x04\x12\x1a\n\x12manifest_id_target\x18\x03 \x01(\x04\x12\x33\n\x0b\x64\x65ltaChunks\x18\x04 \x03(\x0b\x32\x1e.ContentDeltaChunks.DeltaChunk\x12h\n\x13\x63hunk_data_location\x18\x05 \x01(\x0e\x32\x1f.EContentDeltaChunkDataLocation:*k_EContentDeltaChunkDataLocationInProtobuf\x1a\x84\x01\n\nDeltaChunk\x12\x12\n\nsha_source\x18\x01 \x01(\x0c\x12\x12\n\nsha_target\x18\x02 \x01(\x0c\x12\x15\n\rsize_original\x18\x03 \x01(\r\x12\x14\n\x0cpatch_method\x18\x04 \x01(\r\x12\r\n\x05\x63hunk\x18\x05 \x01(\x0c\x12\x12\n\nsize_delta\x18\x06 \x01(\r*\x83\x01\n\x1e\x45\x43ontentDeltaChunkDataLocation\x12.\n*k_EContentDeltaChunkDataLocationInProtobuf\x10\x00\x12\x31\n-k_EContentDeltaChunkDataLocationAfterProtobuf\x10\x01\x42\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'content_manifest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_ECONTENTDELTACHUNKDATALOCATION']._serialized_start=1074
  _globals['_ECONTENTDELTACHUNKDATALOCATION']._serialized_end=1205
  _globals['_CONTENTMANIFESTPAYLOAD']._serialized_start=27
  _globals['_CONTENTMANIFESTPAYLOAD']._serialized_end=394
  _globals['_CONTENTMANIFESTPAYLOAD_FILEMAPPING']._serialized_start=109
  _globals['_CONTENTMANIFESTPAYLOAD_FILEMAPPING']._serialized_end=394
  _globals['_CONTENTMANIFESTPAYLOAD_FILEMAPPING_CHUNKDATA']._serialized_start=297
  _globals['_CONTENTMANIFESTPAYLOAD_FILEMAPPING_CHUNKDATA']._serialized_end=394
  _globals['_CONTENTMANIFESTMETADATA']._serialized_start=397
  _globals['_CONTENTMANIFESTMETADATA']._serialized_end=633
  _globals['_CONTENTMANIFESTSIGNATURE']._serialized_start=635
  _globals['_CONTENTMANIFESTSIGNATURE']._serialized_end=680
  _globals['_CONTENTDELTACHUNKS']._serialized_start=683
  _globals['_CONTENTDELTACHUNKS']._serialized_end=1071
  _globals['_CONTENTDELTACHUNKS_DELTACHUNK']._serialized_start=939
  _globals['_CONTENTDELTACHUNKS_DELTACHUNK']._serialized_end=1071
# @@protoc_insertion_point(module_scope)
