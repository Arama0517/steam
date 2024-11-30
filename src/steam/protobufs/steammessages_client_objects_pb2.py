# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_client_objects.proto
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
    'steammessages_client_objects.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.enums_pb2 as enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"steammessages_client_objects.proto\x1a\x0b\x65nums.proto\"\xcb\x02\n0SteamMessagesClientIClientForcedEnumDependencies\x12?\n\x01\x61\x18\x01 \x01(\x0e\x32\x15.EBluetoothDeviceType:\x1dk_BluetoothDeviceType_Invalid\x12H\n\x01\x62\x18\x02 \x01(\x0e\x32\x19.EStorageBlockContentType:\"k_EStorageBlockContentType_Invalid\x12N\n\x01\x63\x18\x03 \x01(\x0e\x32\x1c.EStorageBlockFileSystemType:%k_EStorageBlockFileSystemType_Invalid\x12<\n\x01\x64\x18\x04 \x01(\x0e\x32\x13.ESDCardFormatStage:\x1ck_ESDCardFormatStage_Invalid\"=\n\x1b\x43MsgNetworkDeviceIP4Address\x12\r\n\x02ip\x18\x01 \x01(\x05:\x01\x30\x12\x0f\n\x07netmask\x18\x02 \x01(\x05\"\xbf\x01\n\x1a\x43MsgNetworkDeviceIP4Config\x12/\n\taddresses\x18\x01 \x03(\x0b\x32\x1c.CMsgNetworkDeviceIP4Address\x12\x0e\n\x06\x64ns_ip\x18\x02 \x03(\x05\x12\x12\n\ngateway_ip\x18\x03 \x01(\x05\x12\x17\n\x0fis_dhcp_enabled\x18\x04 \x01(\x08\x12\x18\n\x10is_default_route\x18\x05 \x01(\x08\x12\x19\n\nis_enabled\x18\x06 \x01(\x08:\x05\x66\x61lse\")\n\x1b\x43MsgNetworkDeviceIP6Address\x12\n\n\x02ip\x18\x01 \x01(\t\"\xbf\x01\n\x1a\x43MsgNetworkDeviceIP6Config\x12/\n\taddresses\x18\x01 \x03(\x0b\x32\x1c.CMsgNetworkDeviceIP6Address\x12\x0e\n\x06\x64ns_ip\x18\x02 \x03(\t\x12\x12\n\ngateway_ip\x18\x03 \x01(\t\x12\x17\n\x0fis_dhcp_enabled\x18\x04 \x01(\x08\x12\x18\n\x10is_default_route\x18\x05 \x01(\x08\x12\x19\n\nis_enabled\x18\x06 \x01(\x08:\x05\x66\x61lse\"\x97\x06\n\x16\x43MsgNetworkDevicesData\x12/\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x1e.CMsgNetworkDevicesData.Device\x12\x17\n\x0fis_wifi_enabled\x18\x02 \x01(\x08\x12 \n\x18is_wifi_scanning_enabled\x18\x03 \x01(\x08\x1a\x90\x05\n\x06\x44\x65vice\x12\r\n\x02id\x18\x01 \x01(\r:\x01\x30\x12\r\n\x05\x65type\x18\x02 \x01(\x05\x12\x0e\n\x06\x65state\x18\x03 \x01(\x05\x12\x0b\n\x03mac\x18\x04 \x01(\t\x12\x0e\n\x06vendor\x18\x05 \x01(\t\x12\x0f\n\x07product\x18\x06 \x01(\t\x12(\n\x03ip4\x18\x07 \x01(\x0b\x32\x1b.CMsgNetworkDeviceIP4Config\x12(\n\x03ip6\x18\x08 \x01(\x0b\x32\x1b.CMsgNetworkDeviceIP6Config\x12\x33\n\x05wired\x18\t \x01(\x0b\x32$.CMsgNetworkDevicesData.Device.Wired\x12\x39\n\x08wireless\x18\n \x01(\x0b\x32\'.CMsgNetworkDevicesData.Device.Wireless\x1aS\n\x05Wired\x12\x1f\n\x10is_cable_present\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x12\n\nspeed_mbit\x18\x02 \x01(\r\x12\x15\n\rfriendly_name\x18\x03 \x01(\t\x1a\x90\x02\n\x08Wireless\x12\x37\n\x03\x61ps\x18\x01 \x03(\x0b\x32*.CMsgNetworkDevicesData.Device.Wireless.AP\x12\x1b\n\x13\x65security_supported\x18\x02 \x01(\x05\x1a\xad\x01\n\x02\x41P\x12\r\n\x02id\x18\x01 \x01(\r:\x01\x30\x12\x11\n\testrength\x18\x02 \x01(\x05\x12\x0c\n\x04ssid\x18\x03 \x01(\t\x12\x11\n\tis_active\x18\x04 \x01(\x08\x12\x16\n\x0eis_autoconnect\x18\x05 \x01(\x08\x12\x11\n\tesecurity\x18\x06 \x01(\x05\x12\x11\n\tuser_name\x18\x07 \x01(\t\x12\x10\n\x08password\x18\x08 \x01(\t\x12\x14\n\x0cstrength_raw\x18\t \x01(\x05\"\xb5\x03\n\x18\x43MsgNetworkDeviceConnect\x12\x14\n\tdevice_id\x18\x01 \x01(\r:\x01\x30\x12:\n\x0b\x63redentials\x18\x04 \x01(\x0b\x32%.CMsgNetworkDeviceConnect.Credentials\x12(\n\x03ip4\x18\x05 \x01(\x0b\x32\x1b.CMsgNetworkDeviceIP4Config\x12(\n\x03ip6\x18\x06 \x01(\x0b\x32\x1b.CMsgNetworkDeviceIP6Config\x12\x35\n\x08\x61p_known\x18\x02 \x01(\x0b\x32!.CMsgNetworkDeviceConnect.KnownAPH\x00\x12\x37\n\tap_custom\x18\x03 \x01(\x0b\x32\".CMsgNetworkDeviceConnect.CustomAPH\x00\x1a\x18\n\x07KnownAP\x12\r\n\x05\x61p_id\x18\x01 \x01(\r\x1a+\n\x08\x43ustomAP\x12\x0c\n\x04ssid\x18\x01 \x01(\t\x12\x11\n\tesecurity\x18\x02 \x01(\x05\x1a\x31\n\x0b\x43redentials\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\tB\t\n\x07\x61p_info\"\x9f\x06\n\x16\x43MsgStorageDevicesData\x12-\n\x06\x64rives\x18\x01 \x03(\x0b\x32\x1d.CMsgStorageDevicesData.Drive\x12:\n\rblock_devices\x18\x02 \x03(\x0b\x32#.CMsgStorageDevicesData.BlockDevice\x12\x1c\n\x14is_unmount_supported\x18\x03 \x01(\x08\x12\x19\n\x11is_trim_supported\x18\x04 \x01(\x08\x12\x17\n\x0fis_trim_running\x18\x05 \x01(\x08\x1a\xbe\x01\n\x05\x44rive\x12\r\n\x02id\x18\x01 \x01(\r:\x01\x30\x12\r\n\x05model\x18\x02 \x01(\t\x12\x0e\n\x06vendor\x18\x03 \x01(\t\x12\x0e\n\x06serial\x18\x04 \x01(\t\x12\x14\n\x0cis_ejectable\x18\x05 \x01(\x08\x12\x12\n\nsize_bytes\x18\x06 \x01(\x04\x12M\n\nmedia_type\x18\x07 \x01(\x0e\x32\x17.EStorageDriveMediaType: k_EStorageDriveMediaType_Invalid\x1a\x86\x03\n\x0b\x42lockDevice\x12\r\n\x02id\x18\x01 \x01(\r:\x01\x30\x12\x13\n\x08\x64rive_id\x18\x02 \x01(\r:\x01\x30\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x15\n\rfriendly_path\x18\x04 \x01(\t\x12\r\n\x05label\x18\x05 \x01(\t\x12\x12\n\nsize_bytes\x18\x06 \x01(\x04\x12\x16\n\x0eis_formattable\x18\x07 \x01(\x08\x12\x14\n\x0cis_read_only\x18\x08 \x01(\x08\x12\x16\n\x0eis_root_device\x18\t \x01(\x08\x12S\n\x0c\x63ontent_type\x18\n \x01(\x0e\x32\x19.EStorageBlockContentType:\"k_EStorageBlockContentType_Invalid\x12\\\n\x0f\x66ilesystem_type\x18\x0b \x01(\x0e\x32\x1c.EStorageBlockFileSystemType:%k_EStorageBlockFileSystemType_Invalid\x12\x12\n\nmount_path\x18\x0c \x01(\t\"\xdf\x01\n\x1d\x43\x43loud_PendingRemoteOperation\x12T\n\toperation\x18\x01 \x01(\x0e\x32\x1d.ECloudPendingRemoteOperation:\"k_ECloudPendingRemoteOperationNone\x12\x14\n\x0cmachine_name\x18\x02 \x01(\t\x12\x11\n\tclient_id\x18\x03 \x01(\x04\x12\x19\n\x11time_last_updated\x18\x04 \x01(\r\x12\x0f\n\x07os_type\x18\x05 \x01(\x05\x12\x13\n\x0b\x64\x65vice_type\x18\x06 \x01(\x05\"V\n CMsgCloudPendingRemoteOperations\x12\x32\n\noperations\x18\x01 \x03(\x0b\x32\x1e.CCloud_PendingRemoteOperation\"\xdf\x04\n\x18\x43MsgBluetoothDevicesData\x12\x33\n\x08\x61\x64\x61pters\x18\x01 \x03(\x0b\x32!.CMsgBluetoothDevicesData.Adapter\x12\x31\n\x07\x64\x65vices\x18\x02 \x03(\x0b\x32 .CMsgBluetoothDevicesData.Device\x12\x32\n\x07manager\x18\x03 \x01(\x0b\x32!.CMsgBluetoothDevicesData.Manager\x1a_\n\x07\x41\x64\x61pter\x12\r\n\x02id\x18\x01 \x01(\r:\x01\x30\x12\x0b\n\x03mac\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\nis_enabled\x18\x04 \x01(\x08\x12\x16\n\x0eis_discovering\x18\x05 \x01(\x08\x1a\x9c\x02\n\x06\x44\x65vice\x12\r\n\x02id\x18\x01 \x01(\r:\x01\x30\x12\x15\n\nadapter_id\x18\x02 \x01(\r:\x01\x30\x12\x43\n\x05\x65type\x18\x03 \x01(\x0e\x32\x15.EBluetoothDeviceType:\x1dk_BluetoothDeviceType_Invalid\x12\x0b\n\x03mac\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x14\n\x0cis_connected\x18\x06 \x01(\x08\x12\x11\n\tis_paired\x18\x07 \x01(\x08\x12\x14\n\x0cstrength_raw\x18\x08 \x01(\x05\x12\x14\n\x0cwake_allowed\x18\t \x01(\x08\x12\x1e\n\x16wake_allowed_supported\x18\n \x01(\x08\x12\x17\n\x0f\x62\x61ttery_percent\x18\x0b \x01(\x05\x1a\'\n\x07Manager\x12\x1c\n\x14is_bluetooth_enabled\x18\x01 \x01(\x08\"<\n\x1d\x43MsgSystemPerfDiagnosticEntry\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xa5\x01\n\x1e\x43MsgSystemPerfNetworkInterface\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x16\n\x0etx_bytes_total\x18\x03 \x01(\x03\x12\x16\n\x0erx_bytes_total\x18\x04 \x01(\x03\x12\x18\n\x10tx_bytes_per_sec\x18\x05 \x01(\x05\x12\x18\n\x10rx_bytes_per_sec\x18\x06 \x01(\x05\"\x9c\x01\n\x1c\x43MsgSystemPerfDiagnosticInfo\x12/\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1e.CMsgSystemPerfDiagnosticEntry\x12\x33\n\ninterfaces\x18\x02 \x03(\x0b\x32\x1f.CMsgSystemPerfNetworkInterface\x12\x16\n\x0e\x62\x61ttery_temp_c\x18\x03 \x01(\x02\"\xf5\x08\n\x14\x43MsgSystemPerfLimits\x12#\n\x1b\x63pu_governor_manual_min_mhz\x18\x01 \x01(\x05\x12#\n\x1b\x63pu_governor_manual_max_mhz\x18\x02 \x01(\x05\x12\x19\n\x11\x66sr_sharpness_min\x18\x03 \x01(\x05\x12\x19\n\x11\x66sr_sharpness_max\x18\x04 \x01(\x05\x12&\n\x1egpu_performance_manual_min_mhz\x18\x05 \x01(\x05\x12&\n\x1egpu_performance_manual_max_mhz\x18\x06 \x01(\x05\x12\"\n\x1aperf_overlay_is_standalone\x18\x07 \x01(\x08\x12 \n\x18is_dynamic_vrs_available\x18\x08 \x01(\x08\x12\x30\n(is_manual_display_refresh_rate_available\x18\t \x01(\x08\x12?\n gpu_performance_levels_available\x18\n \x03(\x0e\x32\x15.EGPUPerformanceLevel\x12%\n\x1d\x64isplay_refresh_manual_hz_min\x18\x0b \x01(\x05\x12%\n\x1d\x64isplay_refresh_manual_hz_max\x18\x0c \x01(\x05\x12\x19\n\x11\x66ps_limit_options\x18\r \x03(\x05\x12\x15\n\rtdp_limit_min\x18\x0e \x01(\x05\x12\x15\n\rtdp_limit_max\x18\x0f \x01(\x05\x12\x18\n\x10is_nis_supported\x18\x10 \x01(\x08\x12\x19\n\x11nis_sharpness_min\x18\x11 \x01(\x05\x12\x19\n\x11nis_sharpness_max\x18\x12 \x01(\x05\x12.\n&display_external_refresh_manual_hz_min\x18\x13 \x01(\x05\x12.\n&display_external_refresh_manual_hz_max\x18\x14 \x01(\x05\x12\"\n\x1a\x66ps_limit_options_external\x18\x15 \x03(\x05\x12\x18\n\x10is_vrr_supported\x18\x17 \x01(\x08\x12\x32\n*is_dynamic_refresh_rate_in_steam_supported\x18\x18 \x01(\x08\x12\x30\n(is_split_scaling_and_filtering_supported\x18\x19 \x01(\x08\x12=\n\x1fsplit_scaling_filters_available\x18\x1a \x03(\x0e\x32\x14.ESplitScalingFilter\x12=\n\x1fsplit_scaling_scalers_available\x18\x1b \x03(\x0e\x32\x14.ESplitScalingScaler\x12\x18\n\x10is_hdr_supported\x18\x1c \x01(\x08\x12(\n display_refresh_manual_hz_oc_max\x18\x1d \x01(\x05\x12\'\n\x1f\x64isable_refresh_rate_management\x18\x1e \x01(\x08\"\xcc\x07\n\x1c\x43MsgSystemPerfSettingsGlobal\x12\x1e\n\x16\x64iagnostic_update_rate\x18\x01 \x01(\x02\x12[\n\x1asystem_trace_service_state\x18\x02 \x01(\x0e\x32\x14.ESystemServiceState:!k_ESystemServiceState_Unavailable\x12\x61\n graphics_profiling_service_state\x18\x03 \x01(\x0e\x32\x14.ESystemServiceState:!k_ESystemServiceState_Unavailable\x12[\n\x1aperf_overlay_service_state\x18\x04 \x01(\x0e\x32\x14.ESystemServiceState:!k_ESystemServiceState_Unavailable\x12Z\n\x12perf_overlay_level\x18\x05 \x01(\x0e\x32\x1a.EGraphicsPerfOverlayLevel:\"k_EGraphicsPerfOverlayLevel_Hidden\x12/\n\'is_show_perf_overlay_over_steam_enabled\x18\x06 \x01(\x08\x12$\n\x1cis_advanced_settings_enabled\x18\x07 \x01(\x08\x12.\n&allow_external_display_refresh_control\x18\x08 \x01(\x08\x12\x16\n\x0eis_hdr_enabled\x18\t \x01(\x08\x12X\n\x1bhdr_on_sdr_tonemap_operator\x18\x0c \x01(\x0e\x32\x14.EHDRToneMapOperator:\x1dk_EHDRToneMapOperator_Invalid\x12$\n\x1cis_hdr_debug_heatmap_enabled\x18\r \x01(\x08\x12+\n\x1d\x66orce_hdr_wide_gammut_for_sdr\x18\x0f \x01(\x08:\x04true\x12\x1e\n\x16\x61llow_experimental_hdr\x18\x10 \x01(\x08\x12\x1d\n\x15sdr_to_hdr_brightness\x18\x16 \x01(\x02\x12\x1f\n\x17\x64\x65\x62ug_force_hdr_support\x18\x12 \x01(\x08\x12#\n\x1b\x66orce_hdr_10pq_output_debug\x18\x13 \x01(\x08\x12\x1d\n\x15is_display_oc_enabled\x18\x14 \x01(\x08\x12#\n\x1bis_color_management_enabled\x18\x15 \x01(\x08\"\xaa\x07\n\x1c\x43MsgSystemPerfSettingsPerApp\x12\"\n\x1agpu_performance_manual_mhz\x18\x01 \x01(\x05\x12\x11\n\tfps_limit\x18\x02 \x01(\x05\x12&\n\x1eis_variable_resolution_enabled\x18\x03 \x01(\x08\x12\'\n\x1fis_dynamic_refresh_rate_enabled\x18\x04 \x01(\x08\x12\x11\n\ttdp_limit\x18\x05 \x01(\x05\x12;\n\x0c\x63pu_governor\x18\x06 \x01(\x0e\x32\r.ECPUGovernor:\x16k_ECPUGovernor_Invalid\x12\x1f\n\x17\x63pu_governor_manual_mhz\x18\x07 \x01(\x05\x12\x16\n\x0escaling_filter\x18\x08 \x01(\x05\x12\x15\n\rfsr_sharpness\x18\t \x01(\x05\x12\x1c\n\x14is_fps_limit_enabled\x18\n \x01(\x08\x12\x1c\n\x14is_tdp_limit_enabled\x18\x0b \x01(\x08\x12#\n\x1bis_low_latency_mode_enabled\x18\x0c \x01(\x08\x12!\n\x19\x64isplay_refresh_manual_hz\x18\r \x01(\x05\x12$\n\x1cis_game_perf_profile_enabled\x18\x0e \x01(\x08\x12T\n\x15gpu_performance_level\x18\x0f \x01(\x0e\x32\x15.EGPUPerformanceLevel:\x1ek_EGPUPerformanceLevel_Invalid\x12\x15\n\rnis_sharpness\x18\x10 \x01(\x05\x12*\n\"display_external_refresh_manual_hz\x18\x11 \x01(\x05\x12\x1a\n\x12\x66ps_limit_external\x18\x12 \x01(\x05\x12\x1a\n\x12is_tearing_enabled\x18\x13 \x01(\x08\x12\x16\n\x0eis_vrr_enabled\x18\x14 \x01(\x08\x12)\n!use_dynamic_refresh_rate_in_steam\x18\x17 \x01(\x08\x12Q\n\x14split_scaling_filter\x18\x18 \x01(\x0e\x32\x14.ESplitScalingFilter:\x1dk_ESplitScalingFilter_Invalid\x12Q\n\x14split_scaling_scaler\x18\x19 \x01(\x0e\x32\x14.ESplitScalingScaler:\x1dk_ESplitScalingScaler_Invalid\"w\n\x16\x43MsgSystemPerfSettings\x12-\n\x06global\x18\x01 \x01(\x0b\x32\x1d.CMsgSystemPerfSettingsGlobal\x12.\n\x07per_app\x18\x02 \x01(\x0b\x32\x1d.CMsgSystemPerfSettingsPerApp\"\x8c\x08\n\x18\x43MsgSystemPerfSettingsV1\x12\x1e\n\x16\x64iagnostic_update_rate\x18\x01 \x01(\x02\x12[\n\x1asystem_trace_service_state\x18\x02 \x01(\x0e\x32\x14.ESystemServiceState:!k_ESystemServiceState_Unavailable\x12\x61\n graphics_profiling_service_state\x18\x03 \x01(\x0e\x32\x14.ESystemServiceState:!k_ESystemServiceState_Unavailable\x12[\n\x1aperf_overlay_service_state\x18\x04 \x01(\x0e\x32\x14.ESystemServiceState:!k_ESystemServiceState_Unavailable\x12Z\n\x12perf_overlay_level\x18\x05 \x01(\x0e\x32\x1a.EGraphicsPerfOverlayLevel:\"k_EGraphicsPerfOverlayLevel_Hidden\x12T\n\x15gpu_performance_level\x18\x06 \x01(\x0e\x32\x15.EGPUPerformanceLevel:\x1ek_EGPUPerformanceLevel_Invalid\x12\"\n\x1agpu_performance_manual_mhz\x18\x07 \x01(\x05\x12\x11\n\tfps_limit\x18\x08 \x01(\x05\x12&\n\x1eis_variable_resolution_enabled\x18\t \x01(\x08\x12\'\n\x1fis_dynamic_refresh_rate_enabled\x18\n \x01(\x08\x12\x11\n\ttdp_limit\x18\x0b \x01(\x05\x12;\n\x0c\x63pu_governor\x18\x0c \x01(\x0e\x32\r.ECPUGovernor:\x16k_ECPUGovernor_Invalid\x12\x1f\n\x17\x63pu_governor_manual_mhz\x18\r \x01(\x05\x12\x16\n\x0escaling_filter\x18\x0e \x01(\x05\x12\x15\n\rfsr_sharpness\x18\x0f \x01(\x05\x12\x1c\n\x14is_fps_limit_enabled\x18\x10 \x01(\x08\x12\x1c\n\x14is_tdp_limit_enabled\x18\x11 \x01(\x08\x12/\n\'is_show_perf_overlay_over_steam_enabled\x18\x12 \x01(\x08\x12#\n\x1bis_low_latency_mode_enabled\x18\x13 \x01(\x08\x12!\n\x19\x64isplay_refresh_manual_hz\x18\x14 \x01(\x05\x12$\n\x1cis_game_perf_profile_enabled\x18\x15 \x01(\x08\"\xa0\x01\n\x13\x43MsgSystemPerfState\x12%\n\x06limits\x18\x01 \x01(\x0b\x32\x15.CMsgSystemPerfLimits\x12)\n\x08settings\x18\x02 \x01(\x0b\x32\x17.CMsgSystemPerfSettings\x12\x17\n\x0f\x63urrent_game_id\x18\x03 \x01(\x04\x12\x1e\n\x16\x61\x63tive_profile_game_id\x18\x04 \x01(\x04\"\xa4\x01\n\x1c\x43MsgSystemPerfUpdateSettings\x12\x0e\n\x06gameid\x18\x01 \x01(\x04\x12\x1b\n\x13skip_storage_update\x18\x04 \x01(\x08\x12\x1a\n\x10reset_to_default\x18\x02 \x01(\x08H\x00\x12\x31\n\x0esettings_delta\x18\x03 \x01(\x0b\x32\x17.CMsgSystemPerfSettingsH\x00\x42\x08\n\x06update\"l\n CMsgSystemPerfLegacySettingEntry\x12\x17\n\x0fprofile_game_id\x18\x01 \x01(\x04\x12/\n\x08settings\x18\x02 \x01(\x0b\x32\x1d.CMsgSystemPerfSettingsPerApp\"\x8a\x01\n\x1c\x43MsgSystemPerfLegacySettings\x12-\n\x06global\x18\x01 \x01(\x0b\x32\x1d.CMsgSystemPerfSettingsGlobal\x12;\n\x10per_app_settings\x18\x02 \x03(\x0b\x32!.CMsgSystemPerfLegacySettingEntry\"\xfa\x01\n\x19\x43MsgSystemDockUpdateState\x12\x36\n\x05state\x18\x01 \x01(\x0e\x32\x0e.EUpdaterState:\x17k_EUpdaterState_Invalid\x12\x1a\n\x12rtime_last_checked\x18\x02 \x01(\x07\x12\x17\n\x0fversion_current\x18\x03 \x01(\t\x12\x19\n\x11version_available\x18\x04 \x01(\t\x12\x16\n\x0estage_progress\x18\x05 \x01(\x02\x12\"\n\x1artime_estimated_completion\x18\x06 \x01(\x07\x12\x19\n\x11old_fw_workaround\x18\x07 \x01(\x05\"G\n\x13\x43MsgSystemDockState\x12\x30\n\x0cupdate_state\x18\x01 \x01(\x0b\x32\x1a.CMsgSystemDockUpdateState\"2\n\x1c\x43MsgSystemDockUpdateFirmware\x12\x12\n\ncheck_only\x18\x01 \x01(\x08\"\xc5\x01\n\x15\x43MsgSystemAudioVolume\x12\x34\n\x07\x65ntries\x18\x01 \x03(\x0b\x32#.CMsgSystemAudioVolume.ChannelEntry\x12\x10\n\x08is_muted\x18\x02 \x01(\x08\x1a\x64\n\x0c\x43hannelEntry\x12\x44\n\x08\x65\x63hannel\x18\x01 \x01(\x0e\x32\x14.ESystemAudioChannel:\x1ck_SystemAudioChannel_Invalid\x12\x0e\n\x06volume\x18\x02 \x01(\x02\"E\n\x1c\x43MsgSystemAudioManagerObject\x12\n\n\x02id\x18\x01 \x01(\r\x12\x19\n\x11rtime_last_update\x18\x02 \x01(\x07\"\x89\x01\n\x1c\x43MsgSystemAudioManagerDevice\x12+\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1d.CMsgSystemAudioManagerObject\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04nick\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0b\n\x03\x61pi\x18\x05 \x01(\t\"\x81\x02\n\x1a\x43MsgSystemAudioManagerNode\x12+\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1d.CMsgSystemAudioManagerObject\x12\x11\n\tdevice_id\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04nick\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12J\n\nedirection\x18\x06 \x01(\x0e\x32\x16.ESystemAudioDirection:\x1ek_SystemAudioDirection_Invalid\x12&\n\x06volume\x18\x07 \x01(\x0b\x32\x16.CMsgSystemAudioVolume\"\xe2\x02\n\x1a\x43MsgSystemAudioManagerPort\x12+\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1d.CMsgSystemAudioManagerObject\x12\x0f\n\x07node_id\x18\x03 \x01(\r\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\r\n\x05\x61lias\x18\x05 \x01(\t\x12\x43\n\x05\x65type\x18\x06 \x01(\x0e\x32\x15.ESystemAudioPortType:\x1dk_SystemAudioPortType_Invalid\x12R\n\nedirection\x18\x07 \x01(\x0e\x32\x1a.ESystemAudioPortDirection:\"k_SystemAudioPortDirection_Invalid\x12\x13\n\x0bis_physical\x18\x08 \x01(\x08\x12\x13\n\x0bis_terminal\x18\t \x01(\x08\x12\x12\n\nis_control\x18\n \x01(\x08\x12\x12\n\nis_monitor\x18\x0b \x01(\x08\"\xa7\x01\n\x1a\x43MsgSystemAudioManagerLink\x12+\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1d.CMsgSystemAudioManagerObject\x12\x16\n\x0eoutput_node_id\x18\x02 \x01(\r\x12\x16\n\x0eoutput_port_id\x18\x03 \x01(\r\x12\x15\n\rinput_node_id\x18\x04 \x01(\r\x12\x15\n\rinput_port_id\x18\x05 \x01(\r\"\xd3\x01\n\x1d\x43MsgSystemAudioManagerStateHW\x12.\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x1d.CMsgSystemAudioManagerDevice\x12*\n\x05nodes\x18\x02 \x03(\x0b\x32\x1b.CMsgSystemAudioManagerNode\x12*\n\x05ports\x18\x03 \x03(\x0b\x32\x1b.CMsgSystemAudioManagerPort\x12*\n\x05links\x18\x04 \x03(\x0b\x32\x1b.CMsgSystemAudioManagerLink\"p\n\x1b\x43MsgSystemAudioManagerState\x12\x14\n\x0crtime_filter\x18\x01 \x01(\x07\x12\x0f\n\x07\x63ounter\x18\x02 \x01(\x05\x12*\n\x02hw\x18\x03 \x01(\x0b\x32\x1e.CMsgSystemAudioManagerStateHW\"8\n%CMsgSystemAudioManagerUpdateSomething\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x05\"V\n\x15\x43MsgSystemDisplayMode\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x12\n\nrefresh_hz\x18\x04 \x01(\x05\"\xb4\x03\n\x11\x43MsgSystemDisplay\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\nis_primary\x18\x04 \x01(\x08\x12\x12\n\nis_enabled\x18\x05 \x01(\x08\x12\x13\n\x0bis_internal\x18\x06 \x01(\x08\x12\x19\n\x11has_mode_override\x18\x07 \x01(\x08\x12\x10\n\x08width_mm\x18\x08 \x01(\x05\x12\x11\n\theight_mm\x18\t \x01(\x05\x12\x17\n\x0f\x63urrent_mode_id\x18\n \x01(\x05\x12%\n\x05modes\x18\x0b \x03(\x0b\x32\x16.CMsgSystemDisplayMode\x12\x18\n\x10refresh_rate_min\x18\x0c \x01(\x05\x12\x18\n\x10refresh_rate_max\x18\r \x01(\x05\x12\x16\n\x0eis_vrr_capable\x18\x0e \x01(\x08\x12\x16\n\x0eis_vrr_enabled\x18\x0f \x01(\x08\x12\x16\n\x0eis_hdr_capable\x18\x10 \x01(\x08\x12\x16\n\x0eis_hdr_enabled\x18\x11 \x01(\x08\x12\x1f\n\x17supported_refresh_rates\x18\x12 \x03(\x05\"\xd3\x01\n\x1d\x43MsgSystemDisplayManagerState\x12$\n\x08\x64isplays\x18\x01 \x03(\x0b\x32\x12.CMsgSystemDisplay\x12#\n\x1bis_mode_switching_supported\x18\x02 \x01(\x08\x12g\n\x12\x63ompatibility_mode\x18\x03 \x01(\x0e\x32 .ESystemDisplayCompatibilityMode:)k_ESystemDisplayCompatibilityMode_Invalid\"F\n\x1f\x43MsgSystemDisplayManagerSetMode\x12\x12\n\ndisplay_id\x18\x01 \x01(\x05\x12\x0f\n\x07mode_id\x18\x02 \x01(\x05\"\xa0\x0b\n\x19\x43MsgSystemManagerSettings\x12*\n\"idle_backlight_dim_battery_seconds\x18\x01 \x01(\x02\x12%\n\x1didle_backlight_dim_ac_seconds\x18\x02 \x01(\x02\x12$\n\x1cidle_suspend_battery_seconds\x18\x03 \x01(\x02\x12\x1f\n\x17idle_suspend_ac_seconds\x18\x04 \x01(\x02\x12\x1e\n\x16idle_suspend_supressed\x18\x05 \x01(\x08\x12(\n is_adaptive_brightness_available\x18\x06 \x01(\x08\x12+\n#display_adaptive_brightness_enabled\x18\x07 \x01(\x08\x12!\n\x19\x64isplay_nightmode_enabled\x18\n \x01(\x08\x12&\n\x1e\x64isplay_nightmode_tintstrength\x18\x0b \x01(\x02\x12 \n\x18\x64isplay_nightmode_maxhue\x18\x0c \x01(\x02\x12 \n\x18\x64isplay_nightmode_maxsat\x18\r \x01(\x02\x12\x1f\n\x17\x64isplay_nightmode_uiexp\x18\x0e \x01(\x02\x12\x1f\n\x17\x64isplay_nightmode_blend\x18\x0f \x01(\x02\x12\x1f\n\x17\x64isplay_nightmode_reset\x18\x10 \x01(\x08\x12*\n\"display_nightmode_schedule_enabled\x18\x11 \x01(\x08\x12,\n$display_nightmode_schedule_starttime\x18\x12 \x01(\x02\x12*\n\"display_nightmode_schedule_endtime\x18\x13 \x01(\x02\x12#\n\x1b\x64isplay_diagnostics_enabled\x18\x14 \x01(\x08\x12\x17\n\x0f\x61ls_lux_primary\x18\x15 \x01(\x02\x12\x16\n\x0e\x61ls_lux_median\x18\x16 \x01(\x02\x12\x1d\n\x15\x64isplay_backlight_raw\x18\x17 \x01(\x02\x12&\n\x1e\x64isplay_brightness_adaptivemin\x18\x18 \x01(\x02\x12&\n\x1e\x64isplay_brightness_adaptivemax\x18\x19 \x01(\x02\x12!\n\x19is_wifi_powersave_enabled\x18\x1a \x01(\x08\x12 \n\x18is_fan_control_available\x18\x1b \x01(\x08\x12P\n\x10\x66\x61n_control_mode\x18\x1c \x01(\x0e\x32\x16.ESystemFanControlMode:\x1ek_SystemFanControlMode_Invalid\x12\'\n\x1fis_display_brightness_available\x18\x1d \x01(\x08\x12,\n$is_display_colormanagement_available\x18\x1f \x01(\x08\x12\x1a\n\x12\x64isplay_colorgamut\x18  \x01(\x02\x12\x19\n\x11\x61ls_lux_alternate\x18! \x01(\x02\x12&\n\x1eis_display_colortemp_available\x18\" \x01(\x08\x12\x19\n\x11\x64isplay_colortemp\x18# \x01(\x02\x12!\n\x19\x64isplay_colortemp_default\x18$ \x01(\x02\x12!\n\x19\x64isplay_colortemp_enabled\x18% \x01(\x08\x12W\n\x1b\x64isplay_colorgamut_labelset\x18& \x01(\x0e\x32\x14.EColorGamutLabelSet:\x1ck_ColorGamutLabelSet_Default\x12.\n&display_brightness_overdrive_hdr_split\x18\' \x01(\x02\"b\n\x18\x43MsgSelectOSBranchParams\x12/\n\x06\x62ranch\x18\x01 \x01(\x0e\x32\n.EOSBranch:\x13k_EOSBranch_Unknown\x12\x15\n\rcustom_branch\x18\x02 \x01(\t\"p\n\x18\x43MsgSystemUpdateProgress\x12\x16\n\x0estage_progress\x18\x01 \x01(\x02\x12\x18\n\x10stage_size_bytes\x18\x02 \x01(\x03\x12\"\n\x1artime_estimated_completion\x18\x03 \x01(\x07\"\xd7\x01\n\x1b\x43MsgSystemUpdateCheckResult\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32\r.EUpdaterType:\x16k_EUpdaterType_Invalid\x12\x12\n\x07\x65result\x18\x02 \x01(\r:\x01\x32\x12\x15\n\rrtime_checked\x18\x03 \x01(\x07\x12\x11\n\tavailable\x18\x04 \x01(\x08\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x14\n\x0c\x61uto_message\x18\x06 \x01(\t\x12\x1e\n\x16system_restart_pending\x18\x07 \x01(\x08\"A\n\x1b\x43MsgSystemUpdateApplyParams\x12\"\n\x0b\x61pply_types\x18\x01 \x03(\x0e\x32\r.EUpdaterType\"\xb6\x01\n\x1b\x43MsgSystemUpdateApplyResult\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32\r.EUpdaterType:\x16k_EUpdaterType_Invalid\x12\x12\n\x07\x65result\x18\x02 \x01(\r:\x01\x32\x12&\n\x17requires_client_restart\x18\x03 \x01(\x08:\x05\x66\x61lse\x12&\n\x17requires_system_restart\x18\x04 \x01(\x08:\x05\x66\x61lse\"\x91\x02\n\x15\x43MsgSystemUpdateState\x12\x36\n\x05state\x18\x01 \x01(\x0e\x32\x0e.EUpdaterState:\x17k_EUpdaterState_Invalid\x12+\n\x08progress\x18\x02 \x01(\x0b\x32\x19.CMsgSystemUpdateProgress\x12:\n\x14update_check_results\x18\x03 \x03(\x0b\x32\x1c.CMsgSystemUpdateCheckResult\x12:\n\x14update_apply_results\x18\x04 \x03(\x0b\x32\x1c.CMsgSystemUpdateApplyResult\x12\x1b\n\x13supports_os_updates\x18\x05 \x01(\x08\"&\n\x15\x43MsgAchievementChange\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"\\\n\x0c\x43MsgCellList\x12!\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x12.CMsgCellList.Cell\x1a)\n\x04\x43\x65ll\x12\x0f\n\x07\x63\x65ll_id\x18\x01 \x01(\r\x12\x10\n\x08loc_name\x18\x02 \x01(\t\"\x8e\x03\n\x10\x43MsgShortcutInfo\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0b\n\x03\x65xe\x18\x02 \x01(\t\x12\x11\n\tstart_dir\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\x0c\n\x04path\x18\x05 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x06 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x07 \x01(\t\x12\x16\n\x0eoverride_appid\x18\x08 \x01(\r\x12\x15\n\rflatpak_appid\x18\t \x01(\t\x12\x0c\n\x04tags\x18\n \x03(\t\x12\x11\n\tis_remote\x18\x0b \x01(\x08\x12\x11\n\tis_hidden\x18\x0c \x01(\x08\x12\x14\n\x0cis_temporary\x18\r \x01(\x08\x12\x11\n\tis_openvr\x18\x0e \x01(\x08\x12\x1c\n\x14\x61llow_desktop_config\x18\x0f \x01(\x08\x12\x15\n\rallow_overlay\x18\x10 \x01(\x08\x12\x1b\n\x13rt_last_played_time\x18\x11 \x01(\r\x12\x1a\n\x12is_devkit_shortcut\x18\x12 \x01(\x08\x12\x15\n\rdevkit_gameid\x18\x13 \x01(\t\"$\n\x12\x43MsgShortcutAppIds\x12\x0e\n\x06\x61ppids\x18\x01 \x03(\r\"\xaa\x01\n\x0f\x43MsgMonitorInfo\x12\x1d\n\x15selected_display_name\x18\x01 \x02(\t\x12.\n\x08monitors\x18\x02 \x03(\x0b\x32\x1c.CMsgMonitorInfo.MonitorInfo\x1aH\n\x0bMonitorInfo\x12\x1b\n\x13monitor_device_name\x18\x01 \x02(\t\x12\x1c\n\x14monitor_display_name\x18\x02 \x02(\t\"2\n\x1d\x43MsgGenerateSystemReportReply\x12\x11\n\treport_id\x18\x01 \x01(\t\"8\n\x16\x43MsgWebUITransportInfo\x12\x0c\n\x04port\x18\x01 \x01(\r\x12\x10\n\x08\x61uth_key\x18\x02 \x01(\t\"2\n\x19\x43MsgWebUITransportFailure\x12\x15\n\rconnect_count\x18\x01 \x01(\r\"^\n\x1d\x43MsgClientShaderHitCacheEntry\x12\x0f\n\x07key_sha\x18\x01 \x01(\x0c\x12\x10\n\x08\x63ode_sha\x18\x02 \x01(\x0c\x12\x1a\n\x12time_last_reported\x18\x03 \x01(\x04\"K\n\x18\x43MsgClientShaderHitCache\x12/\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1e.CMsgClientShaderHitCacheEntry*\x96\x02\n\x1c\x45\x43loudPendingRemoteOperation\x12&\n\"k_ECloudPendingRemoteOperationNone\x10\x00\x12\x32\n.k_ECloudPendingRemoteOperationAppSessionActive\x10\x01\x12\x32\n.k_ECloudPendingRemoteOperationUploadInProgress\x10\x02\x12/\n+k_ECloudPendingRemoteOperationUploadPending\x10\x03\x12\x35\n1k_ECloudPendingRemoteOperationAppSessionSuspended\x10\x04*\xca\x0c\n\x18\x45SteamDeckKeyboardLayout\x12%\n!k_ESteamDeckKeyboardLayout_QWERTY\x10\x00\x12(\n$k_ESteamDeckKeyboardLayout_Bulgarian\x10\x01\x12\x31\n-k_ESteamDeckKeyboardLayout_Chinese_Simplified\x10\x02\x12\x32\n.k_ESteamDeckKeyboardLayout_Chinese_Traditional\x10\x03\x12$\n k_ESteamDeckKeyboardLayout_Czech\x10\x04\x12%\n!k_ESteamDeckKeyboardLayout_Danish\x10\x05\x12&\n\"k_ESteamDeckKeyboardLayout_Finnish\x10\x06\x12%\n!k_ESteamDeckKeyboardLayout_French\x10\x07\x12%\n!k_ESteamDeckKeyboardLayout_German\x10\x08\x12$\n k_ESteamDeckKeyboardLayout_Greek\x10\t\x12(\n$k_ESteamDeckKeyboardLayout_Hungarian\x10\n\x12&\n\"k_ESteamDeckKeyboardLayout_Italian\x10\x0b\x12\'\n#k_ESteamDeckKeyboardLayout_Japanese\x10\x0c\x12%\n!k_ESteamDeckKeyboardLayout_Korean\x10\r\x12(\n$k_ESteamDeckKeyboardLayout_Norwegian\x10\x0e\x12%\n!k_ESteamDeckKeyboardLayout_Polish\x10\x0f\x12)\n%k_ESteamDeckKeyboardLayout_Portuguese\x10\x10\x12\'\n#k_ESteamDeckKeyboardLayout_Romanian\x10\x11\x12&\n\"k_ESteamDeckKeyboardLayout_Russian\x10\x12\x12&\n\"k_ESteamDeckKeyboardLayout_Spanish\x10\x13\x12&\n\"k_ESteamDeckKeyboardLayout_Swedish\x10\x14\x12#\n\x1fk_ESteamDeckKeyboardLayout_Thai\x10\x15\x12(\n$k_ESteamDeckKeyboardLayout_Turkish_F\x10\x16\x12(\n$k_ESteamDeckKeyboardLayout_Turkish_Q\x10\x17\x12(\n$k_ESteamDeckKeyboardLayout_Ukrainian\x10\x18\x12)\n%k_ESteamDeckKeyboardLayout_Vietnamese\x10\x19\x12\x33\n/k_ESteamDeckKeyboardLayout_QWERTY_International\x10\x1a\x12%\n!k_ESteamDeckKeyboardLayout_Dvorak\x10\x1b\x12&\n\"k_ESteamDeckKeyboardLayout_Colemak\x10\x1c\x12=\n9k_ESteamDeckKeyboardLayout_Bulgarian_Phonetic_Traditional\x10\x1d\x12\x31\n-k_ESteamDeckKeyboardLayout_Bulgarian_Phonetic\x10\x1e\x12;\n7k_ESteamDeckKeyboardLayout_Chinese_Traditional_Bopomofo\x10\x1f\x12:\n6k_ESteamDeckKeyboardLayout_Chinese_Traditional_Cangjie\x10 \x12,\n(k_ESteamDeckKeyboardLayout_Japanese_Kana\x10!\x12\x38\n4k_ESteamDeckKeyboardLayout_Chinese_Traditional_Quick\x10\"\x12)\n%k_ESteamDeckKeyboardLayout_Indonesian\x10#B\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_client_objects_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_ECLOUDPENDINGREMOTEOPERATION']._serialized_start=15289
  _globals['_ECLOUDPENDINGREMOTEOPERATION']._serialized_end=15567
  _globals['_ESTEAMDECKKEYBOARDLAYOUT']._serialized_start=15570
  _globals['_ESTEAMDECKKEYBOARDLAYOUT']._serialized_end=17180
  _globals['_STEAMMESSAGESCLIENTICLIENTFORCEDENUMDEPENDENCIES']._serialized_start=52
  _globals['_STEAMMESSAGESCLIENTICLIENTFORCEDENUMDEPENDENCIES']._serialized_end=383
  _globals['_CMSGNETWORKDEVICEIP4ADDRESS']._serialized_start=385
  _globals['_CMSGNETWORKDEVICEIP4ADDRESS']._serialized_end=446
  _globals['_CMSGNETWORKDEVICEIP4CONFIG']._serialized_start=449
  _globals['_CMSGNETWORKDEVICEIP4CONFIG']._serialized_end=640
  _globals['_CMSGNETWORKDEVICEIP6ADDRESS']._serialized_start=642
  _globals['_CMSGNETWORKDEVICEIP6ADDRESS']._serialized_end=683
  _globals['_CMSGNETWORKDEVICEIP6CONFIG']._serialized_start=686
  _globals['_CMSGNETWORKDEVICEIP6CONFIG']._serialized_end=877
  _globals['_CMSGNETWORKDEVICESDATA']._serialized_start=880
  _globals['_CMSGNETWORKDEVICESDATA']._serialized_end=1671
  _globals['_CMSGNETWORKDEVICESDATA_DEVICE']._serialized_start=1015
  _globals['_CMSGNETWORKDEVICESDATA_DEVICE']._serialized_end=1671
  _globals['_CMSGNETWORKDEVICESDATA_DEVICE_WIRED']._serialized_start=1313
  _globals['_CMSGNETWORKDEVICESDATA_DEVICE_WIRED']._serialized_end=1396
  _globals['_CMSGNETWORKDEVICESDATA_DEVICE_WIRELESS']._serialized_start=1399
  _globals['_CMSGNETWORKDEVICESDATA_DEVICE_WIRELESS']._serialized_end=1671
  _globals['_CMSGNETWORKDEVICESDATA_DEVICE_WIRELESS_AP']._serialized_start=1498
  _globals['_CMSGNETWORKDEVICESDATA_DEVICE_WIRELESS_AP']._serialized_end=1671
  _globals['_CMSGNETWORKDEVICECONNECT']._serialized_start=1674
  _globals['_CMSGNETWORKDEVICECONNECT']._serialized_end=2111
  _globals['_CMSGNETWORKDEVICECONNECT_KNOWNAP']._serialized_start=1980
  _globals['_CMSGNETWORKDEVICECONNECT_KNOWNAP']._serialized_end=2004
  _globals['_CMSGNETWORKDEVICECONNECT_CUSTOMAP']._serialized_start=2006
  _globals['_CMSGNETWORKDEVICECONNECT_CUSTOMAP']._serialized_end=2049
  _globals['_CMSGNETWORKDEVICECONNECT_CREDENTIALS']._serialized_start=2051
  _globals['_CMSGNETWORKDEVICECONNECT_CREDENTIALS']._serialized_end=2100
  _globals['_CMSGSTORAGEDEVICESDATA']._serialized_start=2114
  _globals['_CMSGSTORAGEDEVICESDATA']._serialized_end=2913
  _globals['_CMSGSTORAGEDEVICESDATA_DRIVE']._serialized_start=2330
  _globals['_CMSGSTORAGEDEVICESDATA_DRIVE']._serialized_end=2520
  _globals['_CMSGSTORAGEDEVICESDATA_BLOCKDEVICE']._serialized_start=2523
  _globals['_CMSGSTORAGEDEVICESDATA_BLOCKDEVICE']._serialized_end=2913
  _globals['_CCLOUD_PENDINGREMOTEOPERATION']._serialized_start=2916
  _globals['_CCLOUD_PENDINGREMOTEOPERATION']._serialized_end=3139
  _globals['_CMSGCLOUDPENDINGREMOTEOPERATIONS']._serialized_start=3141
  _globals['_CMSGCLOUDPENDINGREMOTEOPERATIONS']._serialized_end=3227
  _globals['_CMSGBLUETOOTHDEVICESDATA']._serialized_start=3230
  _globals['_CMSGBLUETOOTHDEVICESDATA']._serialized_end=3837
  _globals['_CMSGBLUETOOTHDEVICESDATA_ADAPTER']._serialized_start=3414
  _globals['_CMSGBLUETOOTHDEVICESDATA_ADAPTER']._serialized_end=3509
  _globals['_CMSGBLUETOOTHDEVICESDATA_DEVICE']._serialized_start=3512
  _globals['_CMSGBLUETOOTHDEVICESDATA_DEVICE']._serialized_end=3796
  _globals['_CMSGBLUETOOTHDEVICESDATA_MANAGER']._serialized_start=3798
  _globals['_CMSGBLUETOOTHDEVICESDATA_MANAGER']._serialized_end=3837
  _globals['_CMSGSYSTEMPERFDIAGNOSTICENTRY']._serialized_start=3839
  _globals['_CMSGSYSTEMPERFDIAGNOSTICENTRY']._serialized_end=3899
  _globals['_CMSGSYSTEMPERFNETWORKINTERFACE']._serialized_start=3902
  _globals['_CMSGSYSTEMPERFNETWORKINTERFACE']._serialized_end=4067
  _globals['_CMSGSYSTEMPERFDIAGNOSTICINFO']._serialized_start=4070
  _globals['_CMSGSYSTEMPERFDIAGNOSTICINFO']._serialized_end=4226
  _globals['_CMSGSYSTEMPERFLIMITS']._serialized_start=4229
  _globals['_CMSGSYSTEMPERFLIMITS']._serialized_end=5370
  _globals['_CMSGSYSTEMPERFSETTINGSGLOBAL']._serialized_start=5373
  _globals['_CMSGSYSTEMPERFSETTINGSGLOBAL']._serialized_end=6345
  _globals['_CMSGSYSTEMPERFSETTINGSPERAPP']._serialized_start=6348
  _globals['_CMSGSYSTEMPERFSETTINGSPERAPP']._serialized_end=7286
  _globals['_CMSGSYSTEMPERFSETTINGS']._serialized_start=7288
  _globals['_CMSGSYSTEMPERFSETTINGS']._serialized_end=7407
  _globals['_CMSGSYSTEMPERFSETTINGSV1']._serialized_start=7410
  _globals['_CMSGSYSTEMPERFSETTINGSV1']._serialized_end=8446
  _globals['_CMSGSYSTEMPERFSTATE']._serialized_start=8449
  _globals['_CMSGSYSTEMPERFSTATE']._serialized_end=8609
  _globals['_CMSGSYSTEMPERFUPDATESETTINGS']._serialized_start=8612
  _globals['_CMSGSYSTEMPERFUPDATESETTINGS']._serialized_end=8776
  _globals['_CMSGSYSTEMPERFLEGACYSETTINGENTRY']._serialized_start=8778
  _globals['_CMSGSYSTEMPERFLEGACYSETTINGENTRY']._serialized_end=8886
  _globals['_CMSGSYSTEMPERFLEGACYSETTINGS']._serialized_start=8889
  _globals['_CMSGSYSTEMPERFLEGACYSETTINGS']._serialized_end=9027
  _globals['_CMSGSYSTEMDOCKUPDATESTATE']._serialized_start=9030
  _globals['_CMSGSYSTEMDOCKUPDATESTATE']._serialized_end=9280
  _globals['_CMSGSYSTEMDOCKSTATE']._serialized_start=9282
  _globals['_CMSGSYSTEMDOCKSTATE']._serialized_end=9353
  _globals['_CMSGSYSTEMDOCKUPDATEFIRMWARE']._serialized_start=9355
  _globals['_CMSGSYSTEMDOCKUPDATEFIRMWARE']._serialized_end=9405
  _globals['_CMSGSYSTEMAUDIOVOLUME']._serialized_start=9408
  _globals['_CMSGSYSTEMAUDIOVOLUME']._serialized_end=9605
  _globals['_CMSGSYSTEMAUDIOVOLUME_CHANNELENTRY']._serialized_start=9505
  _globals['_CMSGSYSTEMAUDIOVOLUME_CHANNELENTRY']._serialized_end=9605
  _globals['_CMSGSYSTEMAUDIOMANAGEROBJECT']._serialized_start=9607
  _globals['_CMSGSYSTEMAUDIOMANAGEROBJECT']._serialized_end=9676
  _globals['_CMSGSYSTEMAUDIOMANAGERDEVICE']._serialized_start=9679
  _globals['_CMSGSYSTEMAUDIOMANAGERDEVICE']._serialized_end=9816
  _globals['_CMSGSYSTEMAUDIOMANAGERNODE']._serialized_start=9819
  _globals['_CMSGSYSTEMAUDIOMANAGERNODE']._serialized_end=10076
  _globals['_CMSGSYSTEMAUDIOMANAGERPORT']._serialized_start=10079
  _globals['_CMSGSYSTEMAUDIOMANAGERPORT']._serialized_end=10433
  _globals['_CMSGSYSTEMAUDIOMANAGERLINK']._serialized_start=10436
  _globals['_CMSGSYSTEMAUDIOMANAGERLINK']._serialized_end=10603
  _globals['_CMSGSYSTEMAUDIOMANAGERSTATEHW']._serialized_start=10606
  _globals['_CMSGSYSTEMAUDIOMANAGERSTATEHW']._serialized_end=10817
  _globals['_CMSGSYSTEMAUDIOMANAGERSTATE']._serialized_start=10819
  _globals['_CMSGSYSTEMAUDIOMANAGERSTATE']._serialized_end=10931
  _globals['_CMSGSYSTEMAUDIOMANAGERUPDATESOMETHING']._serialized_start=10933
  _globals['_CMSGSYSTEMAUDIOMANAGERUPDATESOMETHING']._serialized_end=10989
  _globals['_CMSGSYSTEMDISPLAYMODE']._serialized_start=10991
  _globals['_CMSGSYSTEMDISPLAYMODE']._serialized_end=11077
  _globals['_CMSGSYSTEMDISPLAY']._serialized_start=11080
  _globals['_CMSGSYSTEMDISPLAY']._serialized_end=11516
  _globals['_CMSGSYSTEMDISPLAYMANAGERSTATE']._serialized_start=11519
  _globals['_CMSGSYSTEMDISPLAYMANAGERSTATE']._serialized_end=11730
  _globals['_CMSGSYSTEMDISPLAYMANAGERSETMODE']._serialized_start=11732
  _globals['_CMSGSYSTEMDISPLAYMANAGERSETMODE']._serialized_end=11802
  _globals['_CMSGSYSTEMMANAGERSETTINGS']._serialized_start=11805
  _globals['_CMSGSYSTEMMANAGERSETTINGS']._serialized_end=13245
  _globals['_CMSGSELECTOSBRANCHPARAMS']._serialized_start=13247
  _globals['_CMSGSELECTOSBRANCHPARAMS']._serialized_end=13345
  _globals['_CMSGSYSTEMUPDATEPROGRESS']._serialized_start=13347
  _globals['_CMSGSYSTEMUPDATEPROGRESS']._serialized_end=13459
  _globals['_CMSGSYSTEMUPDATECHECKRESULT']._serialized_start=13462
  _globals['_CMSGSYSTEMUPDATECHECKRESULT']._serialized_end=13677
  _globals['_CMSGSYSTEMUPDATEAPPLYPARAMS']._serialized_start=13679
  _globals['_CMSGSYSTEMUPDATEAPPLYPARAMS']._serialized_end=13744
  _globals['_CMSGSYSTEMUPDATEAPPLYRESULT']._serialized_start=13747
  _globals['_CMSGSYSTEMUPDATEAPPLYRESULT']._serialized_end=13929
  _globals['_CMSGSYSTEMUPDATESTATE']._serialized_start=13932
  _globals['_CMSGSYSTEMUPDATESTATE']._serialized_end=14205
  _globals['_CMSGACHIEVEMENTCHANGE']._serialized_start=14207
  _globals['_CMSGACHIEVEMENTCHANGE']._serialized_end=14245
  _globals['_CMSGCELLLIST']._serialized_start=14247
  _globals['_CMSGCELLLIST']._serialized_end=14339
  _globals['_CMSGCELLLIST_CELL']._serialized_start=14298
  _globals['_CMSGCELLLIST_CELL']._serialized_end=14339
  _globals['_CMSGSHORTCUTINFO']._serialized_start=14342
  _globals['_CMSGSHORTCUTINFO']._serialized_end=14740
  _globals['_CMSGSHORTCUTAPPIDS']._serialized_start=14742
  _globals['_CMSGSHORTCUTAPPIDS']._serialized_end=14778
  _globals['_CMSGMONITORINFO']._serialized_start=14781
  _globals['_CMSGMONITORINFO']._serialized_end=14951
  _globals['_CMSGMONITORINFO_MONITORINFO']._serialized_start=14879
  _globals['_CMSGMONITORINFO_MONITORINFO']._serialized_end=14951
  _globals['_CMSGGENERATESYSTEMREPORTREPLY']._serialized_start=14953
  _globals['_CMSGGENERATESYSTEMREPORTREPLY']._serialized_end=15003
  _globals['_CMSGWEBUITRANSPORTINFO']._serialized_start=15005
  _globals['_CMSGWEBUITRANSPORTINFO']._serialized_end=15061
  _globals['_CMSGWEBUITRANSPORTFAILURE']._serialized_start=15063
  _globals['_CMSGWEBUITRANSPORTFAILURE']._serialized_end=15113
  _globals['_CMSGCLIENTSHADERHITCACHEENTRY']._serialized_start=15115
  _globals['_CMSGCLIENTSHADERHITCACHEENTRY']._serialized_end=15209
  _globals['_CMSGCLIENTSHADERHITCACHE']._serialized_start=15211
  _globals['_CMSGCLIENTSHADERHITCACHE']._serialized_end=15286
# @@protoc_insertion_point(module_scope)