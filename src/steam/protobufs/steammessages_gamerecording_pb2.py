# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_gamerecording.proto
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
    'steammessages_gamerecording.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2
import steam.protobufs.steammessages_clientserver_video_pb2 as steammessages__clientserver__video__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!steammessages_gamerecording.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\x1a&steammessages_clientserver_video.proto\"\xb4\x01\n\x13\x43VideoManagerClipID\x12\x1d\n\x15video_manager_clip_id\x18\x01 \x01(\x06\x12\x1e\n\x16video_manager_video_id\x18\x02 \x01(\x06\x12\x1a\n\x12server_timeline_id\x18\x03 \x01(\x06\x12\x14\n\x0cmanifest_url\x18\x04 \x01(\t\x12\x13\n\x0b\x64uration_ms\x18\x05 \x01(\r\x12\x17\n\x0fstart_offset_ms\x18\x06 \x01(\r\"\xd9\x01\n\x12\x43GameRecordingClip\x12\x0f\n\x07\x63lip_id\x18\x01 \x01(\x06\x12\x0e\n\x06gameid\x18\x02 \x01(\x04\x12\x15\n\rdate_recorded\x18\x04 \x01(\r\x12\x1d\n\x15total_file_size_bytes\x18\x07 \x01(\x04\x12\'\n\tvideo_ids\x18\t \x03(\x0b\x32\x14.CVideoManagerClipID\x12\x15\n\rowner_steamid\x18\n \x01(\x06\x12\x17\n\x0fupload_complete\x18\x0b \x01(\x08\x12\x13\n\x0b\x64uration_ms\x18\x0c \x01(\r\"z\n&CGameRecording_CreateShareClip_Request\x12!\n\x04\x63lip\x18\x02 \x01(\x0b\x32\x13.CGameRecordingClip\x12-\n\tvideo_def\x18\x03 \x03(\x0b\x32\x1a.CMsgVideoGameRecordingDef\"L\n\'CGameRecording_CreateShareClip_Response\x12!\n\x04\x63lip\x18\x01 \x01(\x0b\x32\x13.CGameRecordingClip\":\n\'CGameRecording_DeleteSharedClip_Request\x12\x0f\n\x07\x63lip_id\x18\x02 \x01(\x06\"*\n(CGameRecording_DeleteSharedClip_Response\"=\n*CGameRecording_GetSingleSharedClip_Request\x12\x0f\n\x07\x63lip_id\x18\x02 \x01(\x06\"P\n+CGameRecording_GetSingleSharedClip_Response\x12!\n\x04\x63lip\x18\x01 \x01(\x0b\x32\x13.CGameRecordingClip\"\xb9\x01\n/CVideo_BeginGameRecordingSegmentsUpload_Request\x12\x14\n\x0crecording_id\x18\x01 \x01(\x04\x12\x16\n\x0e\x63omponent_name\x18\x02 \x01(\t\x12\x1b\n\x13representation_name\x18\x03 \x01(\t\x12;\n\x11segments_to_store\x18\x04 \x03(\x0b\x32 .CVideo_GameRecordingSegmentInfo\"\x87\x01\n0CVideo_BeginGameRecordingSegmentsUpload_Response\x12?\n\x0fsegments_needed\x18\x01 \x03(\x0b\x32&.CVideo_GameRecordingSegmentUploadInfo\x12\x12\n\ncall_again\x18\x02 \x01(\x08\"\xc8\x01\n0CVideo_CommitGameRecordingSegmentsUpload_Request\x12\x14\n\x0crecording_id\x18\x01 \x01(\x04\x12\x16\n\x0e\x63omponent_name\x18\x02 \x01(\t\x12\x1b\n\x13representation_name\x18\x03 \x01(\t\x12\x1c\n\x14\x66irst_segment_number\x18\x04 \x01(\r\x12\x14\n\x0cnum_segments\x18\x05 \x01(\r\x12\x15\n\rupload_result\x18\x06 \x01(\r\"3\n1CVideo_CommitGameRecordingSegmentsUpload_Response\"R\n:CVideo_GameRecordingGetNextBatchOfSegmentsToUpload_Request\x12\x14\n\x0crecording_id\x18\x01 \x01(\x04\"~\n;CVideo_GameRecordingGetNextBatchOfSegmentsToUpload_Response\x12?\n\x0fsegments_needed\x18\x01 \x03(\x0b\x32&.CVideo_GameRecordingSegmentUploadInfo\"\x85\x01\n0CVideo_GameRecordingCommitSegmentUploads_Request\x12\x14\n\x0crecording_id\x18\x01 \x01(\x04\x12;\n\x11segments_uploaded\x18\x02 \x03(\x0b\x32 .CVideo_GameRecordingSegmentInfo\"3\n1CVideo_GameRecordingCommitSegmentUploads_Response2\xd4\x02\n\x11GameRecordingClip\x12\x64\n\x0f\x43reateShareClip\x12\'.CGameRecording_CreateShareClip_Request\x1a(.CGameRecording_CreateShareClip_Response\x12g\n\x10\x44\x65leteSharedClip\x12(.CGameRecording_DeleteSharedClip_Request\x1a).CGameRecording_DeleteSharedClip_Response\x12p\n\x13GetSingleSharedClip\x12+.CGameRecording_GetSingleSharedClip_Request\x1a,.CGameRecording_GetSingleSharedClip_Response2\xbf\x04\n\tVideoClip\x12\x87\x01\n BeginGameRecordingSegmentsUpload\x12\x30.CVideo_BeginGameRecordingSegmentsUpload_Request\x1a\x31.CVideo_BeginGameRecordingSegmentsUpload_Response\x12\x8a\x01\n!CommitGameRecordingSegmentsUpload\x12\x31.CVideo_CommitGameRecordingSegmentsUpload_Request\x1a\x32.CVideo_CommitGameRecordingSegmentsUpload_Response\x12\x9b\x01\n\x1eGetNextBatchOfSegmentsToUpload\x12;.CVideo_GameRecordingGetNextBatchOfSegmentsToUpload_Request\x1a<.CVideo_GameRecordingGetNextBatchOfSegmentsToUpload_Response\x12}\n\x14\x43ommitSegmentUploads\x12\x31.CVideo_GameRecordingCommitSegmentUploads_Request\x1a\x32.CVideo_GameRecordingCommitSegmentUploads_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_gamerecording_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CVIDEOMANAGERCLIPID']._serialized_start=138
  _globals['_CVIDEOMANAGERCLIPID']._serialized_end=318
  _globals['_CGAMERECORDINGCLIP']._serialized_start=321
  _globals['_CGAMERECORDINGCLIP']._serialized_end=538
  _globals['_CGAMERECORDING_CREATESHARECLIP_REQUEST']._serialized_start=540
  _globals['_CGAMERECORDING_CREATESHARECLIP_REQUEST']._serialized_end=662
  _globals['_CGAMERECORDING_CREATESHARECLIP_RESPONSE']._serialized_start=664
  _globals['_CGAMERECORDING_CREATESHARECLIP_RESPONSE']._serialized_end=740
  _globals['_CGAMERECORDING_DELETESHAREDCLIP_REQUEST']._serialized_start=742
  _globals['_CGAMERECORDING_DELETESHAREDCLIP_REQUEST']._serialized_end=800
  _globals['_CGAMERECORDING_DELETESHAREDCLIP_RESPONSE']._serialized_start=802
  _globals['_CGAMERECORDING_DELETESHAREDCLIP_RESPONSE']._serialized_end=844
  _globals['_CGAMERECORDING_GETSINGLESHAREDCLIP_REQUEST']._serialized_start=846
  _globals['_CGAMERECORDING_GETSINGLESHAREDCLIP_REQUEST']._serialized_end=907
  _globals['_CGAMERECORDING_GETSINGLESHAREDCLIP_RESPONSE']._serialized_start=909
  _globals['_CGAMERECORDING_GETSINGLESHAREDCLIP_RESPONSE']._serialized_end=989
  _globals['_CVIDEO_BEGINGAMERECORDINGSEGMENTSUPLOAD_REQUEST']._serialized_start=992
  _globals['_CVIDEO_BEGINGAMERECORDINGSEGMENTSUPLOAD_REQUEST']._serialized_end=1177
  _globals['_CVIDEO_BEGINGAMERECORDINGSEGMENTSUPLOAD_RESPONSE']._serialized_start=1180
  _globals['_CVIDEO_BEGINGAMERECORDINGSEGMENTSUPLOAD_RESPONSE']._serialized_end=1315
  _globals['_CVIDEO_COMMITGAMERECORDINGSEGMENTSUPLOAD_REQUEST']._serialized_start=1318
  _globals['_CVIDEO_COMMITGAMERECORDINGSEGMENTSUPLOAD_REQUEST']._serialized_end=1518
  _globals['_CVIDEO_COMMITGAMERECORDINGSEGMENTSUPLOAD_RESPONSE']._serialized_start=1520
  _globals['_CVIDEO_COMMITGAMERECORDINGSEGMENTSUPLOAD_RESPONSE']._serialized_end=1571
  _globals['_CVIDEO_GAMERECORDINGGETNEXTBATCHOFSEGMENTSTOUPLOAD_REQUEST']._serialized_start=1573
  _globals['_CVIDEO_GAMERECORDINGGETNEXTBATCHOFSEGMENTSTOUPLOAD_REQUEST']._serialized_end=1655
  _globals['_CVIDEO_GAMERECORDINGGETNEXTBATCHOFSEGMENTSTOUPLOAD_RESPONSE']._serialized_start=1657
  _globals['_CVIDEO_GAMERECORDINGGETNEXTBATCHOFSEGMENTSTOUPLOAD_RESPONSE']._serialized_end=1783
  _globals['_CVIDEO_GAMERECORDINGCOMMITSEGMENTUPLOADS_REQUEST']._serialized_start=1786
  _globals['_CVIDEO_GAMERECORDINGCOMMITSEGMENTUPLOADS_REQUEST']._serialized_end=1919
  _globals['_CVIDEO_GAMERECORDINGCOMMITSEGMENTUPLOADS_RESPONSE']._serialized_start=1921
  _globals['_CVIDEO_GAMERECORDINGCOMMITSEGMENTUPLOADS_RESPONSE']._serialized_end=1972
  _globals['_GAMERECORDINGCLIP']._serialized_start=1975
  _globals['_GAMERECORDINGCLIP']._serialized_end=2315
  _globals['_VIDEOCLIP']._serialized_start=2318
  _globals['_VIDEOCLIP']._serialized_end=2893
_builder.BuildServices(DESCRIPTOR, 'steammessages_gamerecording_pb2', _globals)
# @@protoc_insertion_point(module_scope)
