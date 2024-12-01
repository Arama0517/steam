# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_clientmetrics.proto
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
    'steammessages_clientmetrics.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2
import steam.protobufs.clientmetrics_pb2 as clientmetrics__pb2
import steam.protobufs.enums_pb2 as enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!steammessages_clientmetrics.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\x1a\x13\x63lientmetrics.proto\x1a\x0b\x65nums.proto\"\\\n#CClientMetrics_AppInterfaceCreation\x12\x13\n\x0braw_version\x18\x01 \x01(\t\x12 \n\x18requested_interface_type\x18\x02 \x01(\t\"j\n\'CClientMetrics_AppInterfaceMethodCounts\x12\x16\n\x0einterface_name\x18\x01 \x01(\t\x12\x13\n\x0bmethod_name\x18\x02 \x01(\t\x12\x12\n\ncall_count\x18\x03 \x01(\r\"\xe4\x01\n-CClientMetrics_AppInterfaceStats_Notification\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12@\n\x12interfaces_created\x18\x02 \x03(\x0b\x32$.CClientMetrics_AppInterfaceCreation\x12@\n\x0emethods_called\x18\x03 \x03(\x0b\x32(.CClientMetrics_AppInterfaceMethodCounts\x12\x1e\n\x16session_length_seconds\x18\x04 \x01(\r\"]\n&CClientMetrics_IPv6Connectivity_Result\x12\x17\n\x0fprotocol_tested\x18\x01 \x01(\r\x12\x1a\n\x12\x63onnectivity_state\x18\x02 \x01(\r\"\x98\x01\n,CClientMetrics_IPv6Connectivity_Notification\x12\x0f\n\x07\x63\x65ll_id\x18\x01 \x01(\r\x12\x38\n\x07results\x18\x02 \x03(\x0b\x32\'.CClientMetrics_IPv6Connectivity_Result\x12\x1d\n\x15private_ip_is_rfc6598\x18\x03 \x01(\x08\"\xfb\x01\n+CClientMetrics_SteamPipeWorkStats_Operation\x12I\n\x04type\x18\x01 \x01(\x0e\x32\x18.ESteamPipeOperationType:!k_ESteamPipeOperationType_Invalid\x12\x0f\n\x07num_ops\x18\x02 \x01(\r\x12\x11\n\tnum_bytes\x18\x03 \x01(\x04\x12\x14\n\x0c\x62usy_time_ms\x18\x04 \x01(\x04\x12\x14\n\x0cidle_time_ms\x18\x05 \x01(\x04\x12\x17\n\x0fsum_run_time_ms\x18\x06 \x01(\x04\x12\x18\n\x10sum_wait_time_ms\x18\x07 \x01(\x04\"\xf5\x01\n.CClientMetrics_SteamPipeWorkStats_Notification\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12J\n\twork_type\x18\x03 \x01(\x0e\x32\x13.ESteamPipeWorkType:\"k_ESteamPipeClientWorkType_Invalid\x12@\n\noperations\x18\x04 \x03(\x0b\x32,.CClientMetrics_SteamPipeWorkStats_Operation\x12\x15\n\rhardware_type\x18\x05 \x01(\r\"\xc0\x03\n,CClientMetrics_ReportReactUsage_Notification\x12\x0f\n\x07product\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12G\n\x06routes\x18\x03 \x03(\x0b\x32\x37.CClientMetrics_ReportReactUsage_Notification.RouteData\x12O\n\ncomponents\x18\x04 \x03(\x0b\x32;.CClientMetrics_ReportReactUsage_Notification.ComponentData\x12I\n\x07\x61\x63tions\x18\x05 \x03(\x0b\x32\x38.CClientMetrics_ReportReactUsage_Notification.ActionData\x1a)\n\tRouteData\x12\r\n\x05route\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x1a\x31\n\rComponentData\x12\x11\n\tcomponent\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x1a+\n\nActionData\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"\xd4\x01\n-CClientMetrics_ReportClientError_Notification\x12\x0f\n\x07product\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x44\n\x06\x65rrors\x18\x03 \x03(\x0b\x32\x34.CClientMetrics_ReportClientError_Notification.Error\x1a;\n\x05\x45rror\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\r\"g\n+CClientMetrics_ClientBootstrap_Notification\x12\x38\n\x07summary\x18\x01 \x01(\x0b\x32\'.CClientMetrics_ClientBootstrap_Summary\"\xb7\x03\n)CClientMetrics_DownloadRates_Notification\x12\x0f\n\x07\x63\x65ll_id\x18\x01 \x01(\r\x12\x43\n\x05stats\x18\x02 \x03(\x0b\x32\x34.CClientMetrics_DownloadRates_Notification.StatsInfo\x12\x17\n\x0fthrottling_kbps\x18\x03 \x01(\r\x12\x0f\n\x07os_type\x18\x04 \x01(\r\x12\x13\n\x0b\x64\x65vice_type\x18\x05 \x01(\r\x1a\xf4\x01\n\tStatsInfo\x12\x13\n\x0bsource_type\x18\x01 \x01(\r\x12\x11\n\tsource_id\x18\x02 \x01(\r\x12\r\n\x05\x62ytes\x18\x03 \x01(\x04\x12\x11\n\thost_name\x18\x04 \x01(\t\x12\x14\n\x0cmicroseconds\x18\x05 \x01(\x04\x12\x11\n\tused_ipv6\x18\x06 \x01(\x08\x12\x0f\n\x07proxied\x18\x07 \x01(\x08\x12\x12\n\nused_http2\x18\x08 \x01(\x08\x12\x12\n\ncache_hits\x18\t \x01(\r\x12\x14\n\x0c\x63\x61\x63he_misses\x18\n \x01(\r\x12\x11\n\thit_bytes\x18\x0b \x01(\x04\x12\x12\n\nmiss_bytes\x18\x0c \x01(\x04\"\xa0\x02\n-CClientMetrics_ContentValidation_Notification\x12\x19\n\x11validation_result\x18\x01 \x01(\x05\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12\x14\n\x0cstaged_files\x18\x03 \x01(\x08\x12\x16\n\x0euser_initiated\x18\x04 \x01(\x08\x12\x11\n\tearly_out\x18\x05 \x01(\x08\x12\x16\n\x0e\x63hunks_scanned\x18\x06 \x01(\r\x12\x16\n\x0e\x63hunks_corrupt\x18\x07 \x01(\r\x12\x15\n\rbytes_scanned\x18\x08 \x01(\x04\x12\x1b\n\x13\x63hunk_bytes_corrupt\x18\t \x01(\x04\x12\x1f\n\x17total_file_size_corrupt\x18\n \x01(\x04\"\xe0\x04\n-CClientMetrics_CloudAppSyncStats_Notification\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x15\n\rplatform_type\x18\x02 \x01(\r\x12\x0f\n\x07preload\x18\x03 \x01(\x08\x12\x1b\n\x13\x62locking_app_launch\x18\x04 \x01(\x08\x12\x16\n\x0e\x66iles_uploaded\x18\x05 \x01(\r\x12\x18\n\x10\x66iles_downloaded\x18\x06 \x01(\r\x12\x15\n\rfiles_deleted\x18\x07 \x01(\r\x12\x16\n\x0e\x62ytes_uploaded\x18\x08 \x01(\x04\x12\x18\n\x10\x62ytes_downloaded\x18\t \x01(\x04\x12\x16\n\x0emicrosec_total\x18\n \x01(\x04\x12\x1c\n\x14microsec_init_caches\x18\x0b \x01(\x04\x12\x1f\n\x17microsec_validate_state\x18\x0c \x01(\x04\x12\x1a\n\x12microsec_ac_launch\x18\r \x01(\x04\x12#\n\x1bmicrosec_ac_prep_user_files\x18\x0e \x01(\x04\x12\x18\n\x10microsec_ac_exit\x18\x0f \x01(\x04\x12 \n\x18microsec_build_sync_list\x18\x10 \x01(\x04\x12\x1d\n\x15microsec_delete_files\x18\x11 \x01(\x04\x12\x1f\n\x17microsec_download_files\x18\x12 \x01(\x04\x12\x1d\n\x15microsec_upload_files\x18\x13 \x01(\x04\x12\x15\n\rhardware_type\x18\x14 \x01(\r\x12\x15\n\rfiles_managed\x18\x15 \x01(\r\"\x8a\x01\n:CClientMetrics_ContentDownloadResponse_Counts_Notification\x12\x0f\n\x07\x63\x65ll_id\x18\x01 \x01(\r\x12;\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32-.CClientMetrics_ContentDownloadResponse_Hosts\"\xe8\x02\n,CClientMetrics_ReportClientArgs_Notification\x12\x13\n\x0b\x63lient_args\x18\x01 \x03(\t\x12#\n\x1bgpu_webview_regkey_disabled\x18\x02 \x01(\x08\x12\x1b\n\x13suppress_gpu_chrome\x18\x03 \x01(\x08\x12\x1d\n\x15\x62rowser_not_supported\x18\x04 \x01(\x08\x12&\n\x1ehw_accel_video_regkey_disabled\x18\x05 \x01(\x08\x12\x19\n\x11mini_mode_enabled\x18\x06 \x01(\x08\x12\x1b\n\x13\x66ps_counter_enabled\x18\x07 \x01(\x08\x12*\n\"library_low_bandwidth_mode_enabled\x18\x08 \x01(\x08\x12%\n\x1dlibrary_low_perf_mode_enabled\x18\t \x01(\x08\x12\x0f\n\x07gr_mode\x18\n \x01(\x05\"\xad\x01\n%CClientMetrics_ClipShare_Notification\x12\x12\n\x07\x65result\x18\x01 \x01(\r:\x01\x32\x12@\n\x0cshare_method\x18\x02 \x01(\x0e\x32\x11.EClipShareMethod:\x17k_EClipShareMethod_Chat\x12\x0f\n\x07seconds\x18\x03 \x01(\x02\x12\r\n\x05\x62ytes\x18\x04 \x01(\x04\x12\x0e\n\x06gameid\x18\x05 \x01(\x06\"\x83\x04\n%CClientMetrics_ClipRange_Notification\x12U\n\x15original_range_method\x18\x01 \x01(\x0e\x32\x11.EClipRangeMethod:#k_EClipRangeMethod_CreateClipButton\x12G\n\x05start\x18\x02 \x01(\x0b\x32\x38.CClientMetrics_ClipRange_Notification.RelativeRangeEdge\x12\x45\n\x03\x65nd\x18\x03 \x01(\x0b\x32\x38.CClientMetrics_ClipRange_Notification.RelativeRangeEdge\x12\x0f\n\x07seconds\x18\x04 \x01(\x02\x12\x0e\n\x06gameid\x18\x05 \x01(\x06\x1a\xd1\x01\n\x11RelativeRangeEdge\x12U\n\x15original_range_method\x18\x01 \x01(\x0e\x32\x11.EClipRangeMethod:#k_EClipRangeMethod_CreateClipButton\x12S\n\x13latest_range_method\x18\x02 \x01(\x0e\x32\x11.EClipRangeMethod:#k_EClipRangeMethod_CreateClipButton\x12\x10\n\x08\x64\x65lta_ms\x18\x03 \x01(\x05\"\xbf\x01\n,CClientMetrics_EndGameRecording_Notification\x12I\n\x0erecording_type\x18\x01 \x01(\x0e\x32\x13.EGameRecordingType:\x1ck_EGameRecordingType_Unknown\x12\x0f\n\x07seconds\x18\x02 \x01(\x02\x12\r\n\x05\x62ytes\x18\x03 \x01(\x04\x12\x0e\n\x06gameid\x18\x04 \x01(\x06\x12\x14\n\x0cinstant_clip\x18\x05 \x01(\x08*q\n\x12\x45SteamPipeWorkType\x12&\n\"k_ESteamPipeClientWorkType_Invalid\x10\x00\x12\x33\n/k_ESteamPipeClientWorkType_StageFromChunkStores\x10\x01*\xbb\x01\n\x17\x45SteamPipeOperationType\x12%\n!k_ESteamPipeOperationType_Invalid\x10\x00\x12(\n$k_ESteamPipeOperationType_DecryptCPU\x10\x01\x12&\n\"k_ESteamPipeOperationType_DiskRead\x10\x02\x12\'\n#k_ESteamPipeOperationType_DiskWrite\x10\x03*\xd6\x01\n\x10\x45\x43lipShareMethod\x12\x1b\n\x17k_EClipShareMethod_Chat\x10\x01\x12 \n\x1ck_EClipShareMethod_Clipboard\x10\x02\x12\x1b\n\x17k_EClipShareMethod_File\x10\x03\x12\x1f\n\x1bk_EClipShareMethod_SendClip\x10\x04\x12\"\n\x1ek_EClipShareMethod_SaveToMedia\x10\x05\x12!\n\x1dk_EClipShareMethod_CreateLink\x10\x06*\x90\x02\n\x10\x45\x43lipRangeMethod\x12\'\n#k_EClipRangeMethod_CreateClipButton\x10\x01\x12 \n\x1ck_EClipRangeMethod_Highlight\x10\x02\x12&\n\"k_EClipRangeMethod_BeginEndButtons\x10\x03\x12\"\n\x1ek_EClipRangeMethod_ContextMenu\x10\x04\x12\x1b\n\x17k_EClipRangeMethod_Drag\x10\x05\x12!\n\x1dk_EClipRangeMethod_EntireClip\x10\x06\x12%\n!k_EClipRangeMethod_PhaseRecording\x10\x07\x32\xc9\t\n\rClientMetrics\x12\\\n\x1d\x43lientAppInterfaceStatsReport\x12..CClientMetrics_AppInterfaceStats_Notification\x1a\x0b.NoResponse\x12Z\n\x1c\x43lientIPv6ConnectivityReport\x12-.CClientMetrics_IPv6Connectivity_Notification\x1a\x0b.NoResponse\x12X\n\x18SteamPipeWorkStatsReport\x12/.CClientMetrics_SteamPipeWorkStats_Notification\x1a\x0b.NoResponse\x12N\n\x10ReportReactUsage\x12-.CClientMetrics_ReportReactUsage_Notification\x1a\x0b.NoResponse\x12P\n\x11ReportClientError\x12..CClientMetrics_ReportClientError_Notification\x1a\x0b.NoResponse\x12R\n\x15\x43lientBootstrapReport\x12,.CClientMetrics_ClientBootstrap_Notification\x1a\x0b.NoResponse\x12T\n\x19\x43lientDownloadRatesReport\x12*.CClientMetrics_DownloadRates_Notification\x1a\x0b.NoResponse\x12\\\n\x1d\x43lientContentValidationReport\x12..CClientMetrics_ContentValidation_Notification\x1a\x0b.NoResponse\x12V\n\x17\x43lientCloudAppSyncStats\x12..CClientMetrics_CloudAppSyncStats_Notification\x1a\x0b.NoResponse\x12l\n ClientDownloadResponseCodeCounts\x12;.CClientMetrics_ContentDownloadResponse_Counts_Notification\x1a\x0b.NoResponse\x12N\n\x10ReportClientArgs\x12-.CClientMetrics_ReportClientArgs_Notification\x1a\x0b.NoResponse\x12\x46\n\x0fReportClipShare\x12&.CClientMetrics_ClipShare_Notification\x1a\x0b.NoResponse\x12\x46\n\x0fReportClipRange\x12&.CClientMetrics_ClipRange_Notification\x1a\x0b.NoResponse\x12T\n\x16ReportEndGameRecording\x12-.CClientMetrics_EndGameRecording_Notification\x1a\x0b.NoResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_clientmetrics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_ESTEAMPIPEWORKTYPE']._serialized_start=4823
  _globals['_ESTEAMPIPEWORKTYPE']._serialized_end=4936
  _globals['_ESTEAMPIPEOPERATIONTYPE']._serialized_start=4939
  _globals['_ESTEAMPIPEOPERATIONTYPE']._serialized_end=5126
  _globals['_ECLIPSHAREMETHOD']._serialized_start=5129
  _globals['_ECLIPSHAREMETHOD']._serialized_end=5343
  _globals['_ECLIPRANGEMETHOD']._serialized_start=5346
  _globals['_ECLIPRANGEMETHOD']._serialized_end=5618
  _globals['_CCLIENTMETRICS_APPINTERFACECREATION']._serialized_start=131
  _globals['_CCLIENTMETRICS_APPINTERFACECREATION']._serialized_end=223
  _globals['_CCLIENTMETRICS_APPINTERFACEMETHODCOUNTS']._serialized_start=225
  _globals['_CCLIENTMETRICS_APPINTERFACEMETHODCOUNTS']._serialized_end=331
  _globals['_CCLIENTMETRICS_APPINTERFACESTATS_NOTIFICATION']._serialized_start=334
  _globals['_CCLIENTMETRICS_APPINTERFACESTATS_NOTIFICATION']._serialized_end=562
  _globals['_CCLIENTMETRICS_IPV6CONNECTIVITY_RESULT']._serialized_start=564
  _globals['_CCLIENTMETRICS_IPV6CONNECTIVITY_RESULT']._serialized_end=657
  _globals['_CCLIENTMETRICS_IPV6CONNECTIVITY_NOTIFICATION']._serialized_start=660
  _globals['_CCLIENTMETRICS_IPV6CONNECTIVITY_NOTIFICATION']._serialized_end=812
  _globals['_CCLIENTMETRICS_STEAMPIPEWORKSTATS_OPERATION']._serialized_start=815
  _globals['_CCLIENTMETRICS_STEAMPIPEWORKSTATS_OPERATION']._serialized_end=1066
  _globals['_CCLIENTMETRICS_STEAMPIPEWORKSTATS_NOTIFICATION']._serialized_start=1069
  _globals['_CCLIENTMETRICS_STEAMPIPEWORKSTATS_NOTIFICATION']._serialized_end=1314
  _globals['_CCLIENTMETRICS_REPORTREACTUSAGE_NOTIFICATION']._serialized_start=1317
  _globals['_CCLIENTMETRICS_REPORTREACTUSAGE_NOTIFICATION']._serialized_end=1765
  _globals['_CCLIENTMETRICS_REPORTREACTUSAGE_NOTIFICATION_ROUTEDATA']._serialized_start=1628
  _globals['_CCLIENTMETRICS_REPORTREACTUSAGE_NOTIFICATION_ROUTEDATA']._serialized_end=1669
  _globals['_CCLIENTMETRICS_REPORTREACTUSAGE_NOTIFICATION_COMPONENTDATA']._serialized_start=1671
  _globals['_CCLIENTMETRICS_REPORTREACTUSAGE_NOTIFICATION_COMPONENTDATA']._serialized_end=1720
  _globals['_CCLIENTMETRICS_REPORTREACTUSAGE_NOTIFICATION_ACTIONDATA']._serialized_start=1722
  _globals['_CCLIENTMETRICS_REPORTREACTUSAGE_NOTIFICATION_ACTIONDATA']._serialized_end=1765
  _globals['_CCLIENTMETRICS_REPORTCLIENTERROR_NOTIFICATION']._serialized_start=1768
  _globals['_CCLIENTMETRICS_REPORTCLIENTERROR_NOTIFICATION']._serialized_end=1980
  _globals['_CCLIENTMETRICS_REPORTCLIENTERROR_NOTIFICATION_ERROR']._serialized_start=1921
  _globals['_CCLIENTMETRICS_REPORTCLIENTERROR_NOTIFICATION_ERROR']._serialized_end=1980
  _globals['_CCLIENTMETRICS_CLIENTBOOTSTRAP_NOTIFICATION']._serialized_start=1982
  _globals['_CCLIENTMETRICS_CLIENTBOOTSTRAP_NOTIFICATION']._serialized_end=2085
  _globals['_CCLIENTMETRICS_DOWNLOADRATES_NOTIFICATION']._serialized_start=2088
  _globals['_CCLIENTMETRICS_DOWNLOADRATES_NOTIFICATION']._serialized_end=2527
  _globals['_CCLIENTMETRICS_DOWNLOADRATES_NOTIFICATION_STATSINFO']._serialized_start=2283
  _globals['_CCLIENTMETRICS_DOWNLOADRATES_NOTIFICATION_STATSINFO']._serialized_end=2527
  _globals['_CCLIENTMETRICS_CONTENTVALIDATION_NOTIFICATION']._serialized_start=2530
  _globals['_CCLIENTMETRICS_CONTENTVALIDATION_NOTIFICATION']._serialized_end=2818
  _globals['_CCLIENTMETRICS_CLOUDAPPSYNCSTATS_NOTIFICATION']._serialized_start=2821
  _globals['_CCLIENTMETRICS_CLOUDAPPSYNCSTATS_NOTIFICATION']._serialized_end=3429
  _globals['_CCLIENTMETRICS_CONTENTDOWNLOADRESPONSE_COUNTS_NOTIFICATION']._serialized_start=3432
  _globals['_CCLIENTMETRICS_CONTENTDOWNLOADRESPONSE_COUNTS_NOTIFICATION']._serialized_end=3570
  _globals['_CCLIENTMETRICS_REPORTCLIENTARGS_NOTIFICATION']._serialized_start=3573
  _globals['_CCLIENTMETRICS_REPORTCLIENTARGS_NOTIFICATION']._serialized_end=3933
  _globals['_CCLIENTMETRICS_CLIPSHARE_NOTIFICATION']._serialized_start=3936
  _globals['_CCLIENTMETRICS_CLIPSHARE_NOTIFICATION']._serialized_end=4109
  _globals['_CCLIENTMETRICS_CLIPRANGE_NOTIFICATION']._serialized_start=4112
  _globals['_CCLIENTMETRICS_CLIPRANGE_NOTIFICATION']._serialized_end=4627
  _globals['_CCLIENTMETRICS_CLIPRANGE_NOTIFICATION_RELATIVERANGEEDGE']._serialized_start=4418
  _globals['_CCLIENTMETRICS_CLIPRANGE_NOTIFICATION_RELATIVERANGEEDGE']._serialized_end=4627
  _globals['_CCLIENTMETRICS_ENDGAMERECORDING_NOTIFICATION']._serialized_start=4630
  _globals['_CCLIENTMETRICS_ENDGAMERECORDING_NOTIFICATION']._serialized_end=4821
  _globals['_CLIENTMETRICS']._serialized_start=5621
  _globals['_CLIENTMETRICS']._serialized_end=6846
_builder.BuildServices(DESCRIPTOR, 'steammessages_clientmetrics_pb2', _globals)
# @@protoc_insertion_point(module_scope)
