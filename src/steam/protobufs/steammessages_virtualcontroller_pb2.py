# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_virtualcontroller.proto
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
    'steammessages_virtualcontroller.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%steammessages_virtualcontroller.proto\"\xc1\x01\n\x19\x43VirtualControllerElement\x12\x43\n\x04type\x18\x01 \x01(\x0e\x32\x17.EControllerElementType:\x1ck_EControllerElementTypeNone\x12\x0f\n\x07visible\x18\x02 \x01(\x08\x12\x12\n\nx_position\x18\x03 \x01(\x02\x12\x12\n\ny_position\x18\x04 \x01(\x02\x12\x12\n\x07x_scale\x18\x05 \x01(\x02:\x01\x31\x12\x12\n\x07y_scale\x18\x06 \x01(\x02:\x01\x31\"Q\n\x17\x43VirtualControllerColor\x12\x0c\n\x01r\x18\x01 \x01(\x02:\x01\x31\x12\x0c\n\x01g\x18\x02 \x01(\x02:\x01\x31\x12\x0c\n\x01\x62\x18\x03 \x01(\x02:\x01\x31\x12\x0c\n\x01\x61\x18\x04 \x01(\x02:\x01\x31\"\x9f\x01\n\x18\x43VirtualControllerLayout\x12\x16\n\x0elayout_version\x18\x01 \x01(\x05\x12\x14\n\x0c\x61\x63tionset_id\x18\x02 \x01(\x05\x12,\n\x08\x65lements\x18\x04 \x03(\x0b\x32\x1a.CVirtualControllerElement\x12\'\n\x05\x63olor\x18\x05 \x01(\x0b\x32\x18.CVirtualControllerColor\"\xf2\x02\n\x19\x43VirtualControllerLayouts\x12*\n\x07layouts\x18\x01 \x03(\x0b\x32\x19.CVirtualControllerLayout\x12\x37\n\ninput_mode\x18\x02 \x01(\x0e\x32\x0b.EInputMode:\x16k_EInputModeController\x12\x34\n\nmouse_mode\x18\x03 \x01(\x0e\x32\x0b.EMouseMode:\x13k_EMouseModeUnknown\x12\x1f\n\x14trackpad_sensitivity\x18\x04 \x01(\x02:\x01\x31\x12!\n\x12pinch_zoom_enabled\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x17\n\x0cpinch_zoom_x\x18\x06 \x01(\x02:\x01\x30\x12\x17\n\x0cpinch_zoom_y\x18\x07 \x01(\x02:\x01\x30\x12\x1b\n\x10pinch_zoom_scale\x18\x08 \x01(\x02:\x01\x31\x12\x0e\n\x06shaken\x18\t \x01(\x08\x12\x17\n\x0fmouse_offscreen\x18\n \x01(\x08\"\x80\x05\n\x18\x43VirtualControllerConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x37\n\nactionsets\x18\x02 \x03(\x0b\x32#.CVirtualControllerConfig.ActionSet\x12\x43\n\x12\x64\x65\x66\x61ult_mouse_mode\x18\x03 \x01(\x0e\x32\x0b.EMouseMode:\x1ak_EMouseModeAbsoluteCursor\x1a\xe8\x02\n\x07\x43ontrol\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12\x14\n\x0cinput_source\x18\x03 \x01(\x05\x12\x12\n\ninput_mode\x18\x04 \x01(\x05\x12\x15\n\rinput_element\x18\x05 \x01(\x05\x12\x16\n\x0eoutput_gamepad\x18\x06 \x01(\x05\x12\x17\n\x0foutput_keyboard\x18\x07 \x01(\x05\x12\x14\n\x0coutput_mouse\x18\x08 \x01(\x05\x12\x17\n\x0ficon_foreground\x18\t \x01(\t\x12\x17\n\x0ficon_background\x18\n \x01(\t\x12\x14\n\x0cinput_toggle\x18\x0b \x01(\x08\x12(\n input_activate_stick_or_trackpad\x18\x0c \x01(\x05\x12\x17\n\x0f\x61\x63tivation_type\x18\r \x01(\x05\x12\x15\n\rlong_press_ms\x18\x0e \x01(\x05\x12\x17\n\x0f\x64ouble_press_ms\x18\x0f \x01(\x05\x1am\n\tActionSet\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tparent_id\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x33\n\x08\x63ontrols\x18\x04 \x03(\x0b\x32!.CVirtualControllerConfig.Control\"\xcb\x01\n\x1f\x43VirtualControllerLayoutPackage\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x63reator\x18\x02 \x01(\x04\x12\x18\n\x10initial_revision\x18\x03 \x01(\r\x12\x16\n\x0esaved_revision\x18\x04 \x01(\r\x12)\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x19.CVirtualControllerConfig\x12+\n\x07layouts\x18\x06 \x01(\x0b\x32\x1a.CVirtualControllerLayouts\"\xb6\x01\n\x1e\x43VirtualControllerGlobalConfig\x12\x18\n\x10\x66\x65\x65\x64\x62\x61\x63k_enabled\x18\x01 \x01(\x08\x12\x1f\n\x11gyroscope_enabled\x18\x02 \x01(\x08:\x04true\x12\x1f\n\x11\x61uto_fade_enabled\x18\x03 \x01(\x08:\x04true\x12\x1c\n\x0erumble_enabled\x18\x04 \x01(\x08:\x04true\x12\x1a\n\x12shake_fade_enabled\x18\x05 \x01(\x08*|\n\nEInputMode\x12\x17\n\x13k_EInputModeUnknown\x10\x00\x12\x15\n\x11k_EInputModeMouse\x10\x01\x12\x1a\n\x16k_EInputModeController\x10\x02\x12\"\n\x1ek_EInputModeMouseAndController\x10\x03*\x96\x01\n\nEMouseMode\x12\x17\n\x13k_EMouseModeUnknown\x10\x00\x12\x1e\n\x1ak_EMouseModeRelativeCursor\x10\x01\x12\x1e\n\x1ak_EMouseModeAbsoluteCursor\x10\x02\x12\x15\n\x11k_EMouseModeTouch\x10\x03\x12\x18\n\x14k_EMouseModeRelative\x10\x04*\xa6\x0c\n\x16\x45\x43ontrollerElementType\x12)\n\x1ck_EControllerElementTypeNone\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12!\n\x1dk_EControllerElementTypeThumb\x10\x00\x12\'\n#k_EControllerElementTypeButtonSteam\x10\x01\x12(\n$k_EControllerElementTypeJoystickLeft\x10\x02\x12.\n*k_EControllerElementTypeButtonJoystickLeft\x10\x03\x12)\n%k_EControllerElementTypeJoystickRight\x10\x04\x12/\n+k_EControllerElementTypeButtonJoystickRight\x10\x05\x12 \n\x1ck_EControllerElementTypeDPad\x10\x06\x12#\n\x1fk_EControllerElementTypeButtonA\x10\x07\x12#\n\x1fk_EControllerElementTypeButtonB\x10\x08\x12#\n\x1fk_EControllerElementTypeButtonX\x10\t\x12#\n\x1fk_EControllerElementTypeButtonY\x10\n\x12(\n$k_EControllerElementTypeButtonSelect\x10\x0b\x12\'\n#k_EControllerElementTypeButtonStart\x10\x0c\x12-\n)k_EControllerElementTypeButtonTriggerLeft\x10\r\x12.\n*k_EControllerElementTypeButtonTriggerRight\x10\x0e\x12,\n(k_EControllerElementTypeButtonBumperLeft\x10\x0f\x12-\n)k_EControllerElementTypeButtonBumperRight\x10\x10\x12(\n$k_EControllerElementTypeButtonMacro0\x10\x11\x12(\n$k_EControllerElementTypeButtonMacro1\x10\x12\x12(\n$k_EControllerElementTypeButtonMacro2\x10\x13\x12(\n$k_EControllerElementTypeButtonMacro3\x10\x14\x12(\n$k_EControllerElementTypeButtonMacro4\x10\x15\x12(\n$k_EControllerElementTypeButtonMacro5\x10\x16\x12(\n$k_EControllerElementTypeButtonMacro6\x10\x17\x12(\n$k_EControllerElementTypeButtonMacro7\x10\x18\x12*\n&k_EControllerElementTypeTrackpadCenter\x10\x19\x12(\n$k_EControllerElementTypeTrackpadLeft\x10\x1a\x12)\n%k_EControllerElementTypeTrackpadRight\x10\x1b\x12$\n k_EControllerElementTypeKeyboard\x10\x1c\x12+\n\'k_EControllerElementTypeMagnifyingGlass\x10\x1d\x12.\n*k_EControllerElementTypeButtonMacro1Finger\x10\x1e\x12.\n*k_EControllerElementTypeButtonMacro2Finger\x10\x1f\x12\'\n#k_EControllerElementTypeRecordInput\x10 \x12)\n%k_EControllerElementTypePlaybackInput\x10!\x12!\n\x1dk_EControllerElementTypePaste\x10\"\x12\x1f\n\x1bk_EControllerElementTypeMax\x10#')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_virtualcontroller_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EINPUTMODE']._serialized_start=1889
  _globals['_EINPUTMODE']._serialized_end=2013
  _globals['_EMOUSEMODE']._serialized_start=2016
  _globals['_EMOUSEMODE']._serialized_end=2166
  _globals['_ECONTROLLERELEMENTTYPE']._serialized_start=2169
  _globals['_ECONTROLLERELEMENTTYPE']._serialized_end=3743
  _globals['_CVIRTUALCONTROLLERELEMENT']._serialized_start=42
  _globals['_CVIRTUALCONTROLLERELEMENT']._serialized_end=235
  _globals['_CVIRTUALCONTROLLERCOLOR']._serialized_start=237
  _globals['_CVIRTUALCONTROLLERCOLOR']._serialized_end=318
  _globals['_CVIRTUALCONTROLLERLAYOUT']._serialized_start=321
  _globals['_CVIRTUALCONTROLLERLAYOUT']._serialized_end=480
  _globals['_CVIRTUALCONTROLLERLAYOUTS']._serialized_start=483
  _globals['_CVIRTUALCONTROLLERLAYOUTS']._serialized_end=853
  _globals['_CVIRTUALCONTROLLERCONFIG']._serialized_start=856
  _globals['_CVIRTUALCONTROLLERCONFIG']._serialized_end=1496
  _globals['_CVIRTUALCONTROLLERCONFIG_CONTROL']._serialized_start=1025
  _globals['_CVIRTUALCONTROLLERCONFIG_CONTROL']._serialized_end=1385
  _globals['_CVIRTUALCONTROLLERCONFIG_ACTIONSET']._serialized_start=1387
  _globals['_CVIRTUALCONTROLLERCONFIG_ACTIONSET']._serialized_end=1496
  _globals['_CVIRTUALCONTROLLERLAYOUTPACKAGE']._serialized_start=1499
  _globals['_CVIRTUALCONTROLLERLAYOUTPACKAGE']._serialized_end=1702
  _globals['_CVIRTUALCONTROLLERGLOBALCONFIG']._serialized_start=1705
  _globals['_CVIRTUALCONTROLLERGLOBALCONFIG']._serialized_end=1887
# @@protoc_insertion_point(module_scope)
