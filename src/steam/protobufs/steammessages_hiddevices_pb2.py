# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_hiddevices.proto
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
    'steammessages_hiddevices.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esteammessages_hiddevices.proto\"\xba\x04\n\x0e\x43HIDDeviceInfo\x12=\n\x08location\x18\x01 \x01(\x0e\x32\x13.EHIDDeviceLocation:\x16k_EDeviceLocationLocal\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x11\n\tvendor_id\x18\x03 \x01(\r\x12\x12\n\nproduct_id\x18\x04 \x01(\r\x12\x15\n\rserial_number\x18\x05 \x01(\t\x12\x16\n\x0erelease_number\x18\x06 \x01(\r\x12\x1b\n\x13manufacturer_string\x18\x07 \x01(\t\x12\x16\n\x0eproduct_string\x18\x08 \x01(\t\x12\x12\n\nusage_page\x18\t \x01(\r\x12\r\n\x05usage\x18\n \x01(\r\x12\x1c\n\x10interface_number\x18\x0b \x01(\x05:\x02-1\x12\x12\n\x06ostype\x18\x0c \x01(\x05:\x02-1\x12\x1a\n\x12is_generic_gamepad\x18\r \x01(\x08\x12\x1b\n\x13is_generic_joystick\x18\x0e \x01(\x08\x12\x11\n\tcaps_bits\x18\x0f \x01(\r\x12\x12\n\nsession_id\x18\x10 \x01(\r\x12#\n\x18\x65\x43ontrollerType_OBSOLETE\x18\x11 \x01(\r:\x01\x30\x12(\n\x19is_xinput_device_OBSOLETE\x18\x12 \x01(\x08:\x05\x66\x61lse\x12*\n\"session_remote_play_together_appid\x18\x13 \x01(\r\x12 \n\x11is_steamvr_device\x18\x14 \x01(\x08:\x05\x66\x61lse\"w\n\x15\x43HIDDeviceInputReport\x12\x13\n\x0b\x66ull_report\x18\x01 \x01(\x0c\x12\x14\n\x0c\x64\x65lta_report\x18\x02 \x01(\x0c\x12\x19\n\x11\x64\x65lta_report_size\x18\x03 \x01(\r\x12\x18\n\x10\x64\x65lta_report_crc\x18\x04 \x01(\r\"\xe2\x0c\n\x13\x43HIDMessageToRemote\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12\x36\n\x0b\x64\x65vice_open\x18\x02 \x01(\x0b\x32\x1f.CHIDMessageToRemote.DeviceOpenH\x00\x12\x38\n\x0c\x64\x65vice_close\x18\x03 \x01(\x0b\x32 .CHIDMessageToRemote.DeviceCloseH\x00\x12\x38\n\x0c\x64\x65vice_write\x18\x04 \x01(\x0b\x32 .CHIDMessageToRemote.DeviceWriteH\x00\x12\x36\n\x0b\x64\x65vice_read\x18\x05 \x01(\x0b\x32\x1f.CHIDMessageToRemote.DeviceReadH\x00\x12R\n\x1a\x64\x65vice_send_feature_report\x18\x06 \x01(\x0b\x32,.CHIDMessageToRemote.DeviceSendFeatureReportH\x00\x12P\n\x19\x64\x65vice_get_feature_report\x18\x07 \x01(\x0b\x32+.CHIDMessageToRemote.DeviceGetFeatureReportH\x00\x12N\n\x18\x64\x65vice_get_vendor_string\x18\x08 \x01(\x0b\x32*.CHIDMessageToRemote.DeviceGetVendorStringH\x00\x12P\n\x19\x64\x65vice_get_product_string\x18\t \x01(\x0b\x32+.CHIDMessageToRemote.DeviceGetProductStringH\x00\x12[\n\x1f\x64\x65vice_get_serial_number_string\x18\n \x01(\x0b\x32\x30.CHIDMessageToRemote.DeviceGetSerialNumberStringH\x00\x12R\n\x1a\x64\x65vice_start_input_reports\x18\x0b \x01(\x0b\x32,.CHIDMessageToRemote.DeviceStartInputReportsH\x00\x12R\n\x1a\x64\x65vice_request_full_report\x18\x0c \x01(\x0b\x32,.CHIDMessageToRemote.DeviceRequestFullReportH\x00\x12\x42\n\x11\x64\x65vice_disconnect\x18\r \x01(\x0b\x32%.CHIDMessageToRemote.DeviceDisconnectH\x00\x1a+\n\nDeviceOpen\x12\x1d\n\x04info\x18\x01 \x01(\x0b\x32\x0f.CHIDDeviceInfo\x1a\x1d\n\x0b\x44\x65viceClose\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x1a+\n\x0b\x44\x65viceWrite\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x1a@\n\nDeviceRead\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x12\x0e\n\x06length\x18\x02 \x01(\r\x12\x12\n\ntimeout_ms\x18\x03 \x01(\x05\x1a\x37\n\x17\x44\x65viceSendFeatureReport\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x1aO\n\x16\x44\x65viceGetFeatureReport\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x12\x15\n\rreport_number\x18\x02 \x01(\x0c\x12\x0e\n\x06length\x18\x03 \x01(\r\x1a\'\n\x15\x44\x65viceGetVendorString\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x1a(\n\x16\x44\x65viceGetProductString\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x1a-\n\x1b\x44\x65viceGetSerialNumberString\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x1a\x39\n\x17\x44\x65viceStartInputReports\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x12\x0e\n\x06length\x18\x02 \x01(\r\x1a)\n\x17\x44\x65viceRequestFullReport\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x1a\x89\x01\n\x10\x44\x65viceDisconnect\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x12W\n\x10\x64isconnectMethod\x18\x02 \x01(\x0e\x32\x1b.EHIDDeviceDisconnectMethod: k_EDeviceDisconnectMethodUnknown\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x42\t\n\x07\x63ommand\"\xcb\x05\n\x15\x43HIDMessageFromRemote\x12\x45\n\x12update_device_list\x18\x01 \x01(\x0b\x32\'.CHIDMessageFromRemote.UpdateDeviceListH\x00\x12:\n\x08response\x18\x02 \x01(\x0b\x32&.CHIDMessageFromRemote.RequestResponseH\x00\x12<\n\x07reports\x18\x03 \x01(\x0b\x32).CHIDMessageFromRemote.DeviceInputReportsH\x00\x12:\n\x0c\x63lose_device\x18\x04 \x01(\x0b\x32\".CHIDMessageFromRemote.CloseDeviceH\x00\x12\x43\n\x11\x63lose_all_devices\x18\x05 \x01(\x0b\x32&.CHIDMessageFromRemote.CloseAllDevicesH\x00\x1a\x34\n\x10UpdateDeviceList\x12 \n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x0f.CHIDDeviceInfo\x1a\x43\n\x0fRequestResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12\x0e\n\x06result\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x1a\xb7\x01\n\x12\x44\x65viceInputReports\x12S\n\x0e\x64\x65vice_reports\x18\x01 \x03(\x0b\x32;.CHIDMessageFromRemote.DeviceInputReports.DeviceInputReport\x1aL\n\x11\x44\x65viceInputReport\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x12\'\n\x07reports\x18\x02 \x03(\x0b\x32\x16.CHIDDeviceInputReport\x1a\x1d\n\x0b\x43loseDevice\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\r\x1a\x11\n\x0f\x43loseAllDevicesB\t\n\x07\x63ommand*g\n\x12\x45HIDDeviceLocation\x12\x1a\n\x16k_EDeviceLocationLocal\x10\x00\x12\x1b\n\x17k_EDeviceLocationRemote\x10\x02\x12\x18\n\x14k_EDeviceLocationAny\x10\x03*\xc1\x01\n\x1a\x45HIDDeviceDisconnectMethod\x12$\n k_EDeviceDisconnectMethodUnknown\x10\x00\x12&\n\"k_EDeviceDisconnectMethodBluetooth\x10\x01\x12*\n&k_EDeviceDisconnectMethodFeatureReport\x10\x02\x12)\n%k_EDeviceDisconnectMethodOutputReport\x10\x03\x42\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_hiddevices_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_EHIDDEVICELOCATION']._serialized_start=3083
  _globals['_EHIDDEVICELOCATION']._serialized_end=3186
  _globals['_EHIDDEVICEDISCONNECTMETHOD']._serialized_start=3189
  _globals['_EHIDDEVICEDISCONNECTMETHOD']._serialized_end=3382
  _globals['_CHIDDEVICEINFO']._serialized_start=35
  _globals['_CHIDDEVICEINFO']._serialized_end=605
  _globals['_CHIDDEVICEINPUTREPORT']._serialized_start=607
  _globals['_CHIDDEVICEINPUTREPORT']._serialized_end=726
  _globals['_CHIDMESSAGETOREMOTE']._serialized_start=729
  _globals['_CHIDMESSAGETOREMOTE']._serialized_end=2363
  _globals['_CHIDMESSAGETOREMOTE_DEVICEOPEN']._serialized_start=1657
  _globals['_CHIDMESSAGETOREMOTE_DEVICEOPEN']._serialized_end=1700
  _globals['_CHIDMESSAGETOREMOTE_DEVICECLOSE']._serialized_start=1702
  _globals['_CHIDMESSAGETOREMOTE_DEVICECLOSE']._serialized_end=1731
  _globals['_CHIDMESSAGETOREMOTE_DEVICEWRITE']._serialized_start=1733
  _globals['_CHIDMESSAGETOREMOTE_DEVICEWRITE']._serialized_end=1776
  _globals['_CHIDMESSAGETOREMOTE_DEVICEREAD']._serialized_start=1778
  _globals['_CHIDMESSAGETOREMOTE_DEVICEREAD']._serialized_end=1842
  _globals['_CHIDMESSAGETOREMOTE_DEVICESENDFEATUREREPORT']._serialized_start=1844
  _globals['_CHIDMESSAGETOREMOTE_DEVICESENDFEATUREREPORT']._serialized_end=1899
  _globals['_CHIDMESSAGETOREMOTE_DEVICEGETFEATUREREPORT']._serialized_start=1901
  _globals['_CHIDMESSAGETOREMOTE_DEVICEGETFEATUREREPORT']._serialized_end=1980
  _globals['_CHIDMESSAGETOREMOTE_DEVICEGETVENDORSTRING']._serialized_start=1982
  _globals['_CHIDMESSAGETOREMOTE_DEVICEGETVENDORSTRING']._serialized_end=2021
  _globals['_CHIDMESSAGETOREMOTE_DEVICEGETPRODUCTSTRING']._serialized_start=2023
  _globals['_CHIDMESSAGETOREMOTE_DEVICEGETPRODUCTSTRING']._serialized_end=2063
  _globals['_CHIDMESSAGETOREMOTE_DEVICEGETSERIALNUMBERSTRING']._serialized_start=2065
  _globals['_CHIDMESSAGETOREMOTE_DEVICEGETSERIALNUMBERSTRING']._serialized_end=2110
  _globals['_CHIDMESSAGETOREMOTE_DEVICESTARTINPUTREPORTS']._serialized_start=2112
  _globals['_CHIDMESSAGETOREMOTE_DEVICESTARTINPUTREPORTS']._serialized_end=2169
  _globals['_CHIDMESSAGETOREMOTE_DEVICEREQUESTFULLREPORT']._serialized_start=2171
  _globals['_CHIDMESSAGETOREMOTE_DEVICEREQUESTFULLREPORT']._serialized_end=2212
  _globals['_CHIDMESSAGETOREMOTE_DEVICEDISCONNECT']._serialized_start=2215
  _globals['_CHIDMESSAGETOREMOTE_DEVICEDISCONNECT']._serialized_end=2352
  _globals['_CHIDMESSAGEFROMREMOTE']._serialized_start=2366
  _globals['_CHIDMESSAGEFROMREMOTE']._serialized_end=3081
  _globals['_CHIDMESSAGEFROMREMOTE_UPDATEDEVICELIST']._serialized_start=2713
  _globals['_CHIDMESSAGEFROMREMOTE_UPDATEDEVICELIST']._serialized_end=2765
  _globals['_CHIDMESSAGEFROMREMOTE_REQUESTRESPONSE']._serialized_start=2767
  _globals['_CHIDMESSAGEFROMREMOTE_REQUESTRESPONSE']._serialized_end=2834
  _globals['_CHIDMESSAGEFROMREMOTE_DEVICEINPUTREPORTS']._serialized_start=2837
  _globals['_CHIDMESSAGEFROMREMOTE_DEVICEINPUTREPORTS']._serialized_end=3020
  _globals['_CHIDMESSAGEFROMREMOTE_DEVICEINPUTREPORTS_DEVICEINPUTREPORT']._serialized_start=2944
  _globals['_CHIDMESSAGEFROMREMOTE_DEVICEINPUTREPORTS_DEVICEINPUTREPORT']._serialized_end=3020
  _globals['_CHIDMESSAGEFROMREMOTE_CLOSEDEVICE']._serialized_start=3022
  _globals['_CHIDMESSAGEFROMREMOTE_CLOSEDEVICE']._serialized_end=3051
  _globals['_CHIDMESSAGEFROMREMOTE_CLOSEALLDEVICES']._serialized_start=3053
  _globals['_CHIDMESSAGEFROMREMOTE_CLOSEALLDEVICES']._serialized_end=3070
# @@protoc_insertion_point(module_scope)
