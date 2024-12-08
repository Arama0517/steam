# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_remoteclient_service_messages.proto
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
    'steammessages_remoteclient_service_messages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1steammessages_remoteclient_service_messages.proto\"%\n#CRemoteClient_CreateSession_Request\"M\n$CRemoteClient_CreateSession_Response\x12\x12\n\nsession_id\x18\x01 \x01(\x06\x12\x11\n\teuniverse\x18\x02 \x01(\x05\">\n(CRemoteClient_DeleteSession_Notification\x12\x12\n\nsession_id\x18\x01 \x01(\x06\"8\n\"CRemoteClient_StartPairing_Request\x12\x12\n\nsession_id\x18\x01 \x01(\x06\"2\n#CRemoteClient_StartPairing_Response\x12\x0b\n\x03pin\x18\x01 \x01(\r\"^\n$CRemoteClient_SetPairingInfo_Request\x12\x12\n\nsession_id\x18\x01 \x01(\x06\x12\x11\n\tdevice_id\x18\x02 \x01(\x06\x12\x0f\n\x07request\x18\x03 \x01(\x0c\"\'\n%CRemoteClient_SetPairingInfo_Response\"3\n$CRemoteClient_GetPairingInfo_Request\x12\x0b\n\x03pin\x18\x01 \x01(\r\"_\n%CRemoteClient_GetPairingInfo_Response\x12\x12\n\nsession_id\x18\x01 \x01(\x06\x12\x11\n\tdevice_id\x18\x02 \x01(\x06\x12\x0f\n\x07request\x18\x03 \x01(\x0c\"9\n#CRemoteClient_CancelPairing_Request\x12\x12\n\nsession_id\x18\x01 \x01(\x06\"&\n$CRemoteClient_CancelPairing_Response\"i\n/CRemoteClient_RegisterStatusUpdate_Notification\x12\x12\n\nsession_id\x18\x01 \x01(\x06\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\x12\x11\n\tdevice_id\x18\x03 \x01(\x06\"X\n1CRemoteClient_UnregisterStatusUpdate_Notification\x12\x12\n\nsession_id\x18\x01 \x01(\x06\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\"h\n\x1b\x43RemoteClient_DeviceDetails\x12\x1c\n\x14\x64\x65vice_friendly_name\x18\x01 \x01(\t\x12\x0f\n\x07os_type\x18\x02 \x01(\x05\x12\x1a\n\x12gaming_device_type\x18\x03 \x01(\r\"\x84\x01\n!CRemoteClient_Online_Notification\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10remote_client_id\x18\x02 \x01(\x06\x12\x34\n\x0e\x64\x65vice_details\x18\x03 \x01(\x0b\x32\x1c.CRemoteClient_DeviceDetails\"(\n&CRemoteClient_GetRecentClients_Request\"}\n\x19\x43RemoteClient_ClientLogin\x12\x18\n\x10remote_client_id\x18\x01 \x01(\x06\x12\x10\n\x08token_id\x18\x02 \x01(\x06\x12\x34\n\x0e\x64\x65vice_details\x18\x03 \x01(\x0b\x32\x1c.CRemoteClient_DeviceDetails\"\xc1\x01\n\x1b\x43RemoteClient_ClientDetails\x12\x18\n\x10remote_client_id\x18\x01 \x01(\x06\x12\x34\n\x0e\x64\x65vice_details\x18\x02 \x01(\x0b\x32\x1c.CRemoteClient_DeviceDetails\x12\x11\n\tlast_seen\x18\x04 \x01(\x04\x12\x0c\n\x04\x63ity\x18\x05 \x01(\t\x12\r\n\x05state\x18\x06 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x07 \x01(\t\x12\x11\n\tis_online\x18\x08 \x01(\x08\"X\n\'CRemoteClient_GetRecentClients_Response\x12-\n\x07\x63lients\x18\x01 \x03(\x0b\x32\x1c.CRemoteClient_ClientDetails\"\x83\x01\n\x12\x43RemoteClient_Task\x12>\n\x04type\x18\x01 \x01(\x0e\x32\x14.ECLientTaskListType:\x1ak_EClientTask_DownloadClip\x12\x0f\n\x07task_id\x18\x02 \x01(\x06\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0f\n\x07\x66ile_id\x18\x04 \x01(\x03\"b\n#CRemoteClient_AddClientTask_Request\x12\x18\n\x10remote_client_id\x18\x01 \x01(\x06\x12!\n\x04task\x18\x02 \x01(\x0b\x32\x13.CRemoteClient_Task\"&\n$CRemoteClient_AddClientTask_Response\"f\n#CRemoteClient_TaskList_Notification\x12\x18\n\x10remote_client_id\x18\x01 \x01(\x06\x12%\n\x08tasklist\x18\x02 \x03(\x0b\x32\x13.CRemoteClient_Task\"g\n&CRemoteClient_MarkTaskComplete_Request\x12\x18\n\x10remote_client_id\x18\x01 \x01(\x06\x12\x0f\n\x07task_id\x18\x02 \x01(\x06\x12\x12\n\ncontent_id\x18\x03 \x01(\t\")\n\'CRemoteClient_MarkTaskComplete_Response\"_\n\'CRemoteClient_RemotePacket_Notification\x12\x12\n\nsession_id\x18\x01 \x01(\x06\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\"M\n&CRemoteClient_ReplyPacket_Notification\x12\x12\n\nsession_id\x18\x01 \x01(\x06\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"6\n CRemoteClient_GetReplies_Request\x12\x12\n\nsession_id\x18\x01 \x01(\x06\"4\n!CRemoteClient_GetReplies_Response\x12\x0f\n\x07payload\x18\x01 \x03(\x0c\"P\n)CRemoteClient_AllocateRelayServer_Request\x12\x0e\n\x06\x63\x65llid\x18\x01 \x01(\r\x12\x13\n\x0b\x63redentials\x18\x02 \x01(\t\"B\n*CRemoteClient_AllocateRelayServer_Response\x12\x14\n\x0crelay_server\x18\x01 \x01(\t\"2\n!CRemoteClient_AllocateSDR_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"$\n\"CRemoteClient_AllocateSDR_Response\"_\n)CRemoteClient_SteamBroadcast_Notification\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x10\n\x08\x63lientid\x18\x02 \x01(\x06\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"\x93\x01\n\'CRemoteClient_SteamToSteam_Notification\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x14\n\x0csrc_clientid\x18\x02 \x01(\x06\x12\x14\n\x0c\x64st_clientid\x18\x03 \x01(\x06\x12\x10\n\x08secretid\x18\x04 \x01(\r\x12\x19\n\x11\x65ncrypted_payload\x18\x05 \x01(\x0c\"\xb8\x01\n\"CRemotePlay_SessionStarted_Request\x12\x17\n\x0fhost_account_id\x18\x01 \x01(\r\x12\x19\n\x11\x63lient_account_id\x18\x02 \x01(\r\x12\r\n\x05\x61ppid\x18\x03 \x01(\r\x12\x1a\n\x12\x64\x65vice_form_factor\x18\x04 \x01(\x05\x12\x1c\n\x14remote_play_together\x18\x05 \x01(\x08\x12\x15\n\rguest_session\x18\x06 \x01(\x08\"8\n#CRemotePlay_SessionStarted_Response\x12\x11\n\trecord_id\x18\x01 \x01(\x06\"u\n\'CRemotePlay_SessionStopped_Notification\x12\x11\n\trecord_id\x18\x01 \x01(\x06\x12\x11\n\tused_x264\x18\x02 \x01(\x08\x12\x11\n\tused_h264\x18\x03 \x01(\x08\x12\x11\n\tused_hevc\x18\x04 \x01(\x08\"\xb7\x06\n CRemotePlayTogether_Notification\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12G\n\rgroup_updated\x18\x02 \x01(\x0b\x32..CRemotePlayTogether_Notification.GroupUpdatedH\x00\x1a\x8c\x01\n\x06Player\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x0f\n\x07guestid\x18\x02 \x01(\r\x12\x13\n\x0b\x61vatar_hash\x18\x03 \x01(\x0c\x12\x18\n\x10keyboard_enabled\x18\x04 \x01(\x08\x12\x15\n\rmouse_enabled\x18\x05 \x01(\x08\x12\x1a\n\x12\x63ontroller_enabled\x18\x06 \x01(\x08\x1a:\n\x17\x43ontrollerSlot_obsolete\x12\x0e\n\x06slotid\x18\x01 \x01(\r\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\x1as\n\x0e\x43ontrollerSlot\x12\x0e\n\x06slotid\x18\x01 \x01(\r\x12\x38\n\x06player\x18\x02 \x01(\x0b\x32(.CRemotePlayTogether_Notification.Player\x12\x17\n\x0f\x63ontroller_type\x18\x03 \x01(\x05\x1a\xed\x02\n\x0cGroupUpdated\x12\x14\n\x0chost_steamid\x18\x01 \x01(\x06\x12\x15\n\rhost_clientid\x18\x02 \x01(\x06\x12\x18\n\x10players_obsolete\x18\x03 \x03(\x06\x12\x13\n\x0bhost_gameid\x18\x04 \x01(\x06\x12\\\n\x19\x63ontroller_slots_obsolete\x18\x05 \x03(\x0b\x32\x39.CRemotePlayTogether_Notification.ControllerSlot_obsolete\x12\x17\n\x0fhas_new_players\x18\x06 \x01(\x08\x12>\n\x0cplayer_slots\x18\x07 \x03(\x0b\x32(.CRemotePlayTogether_Notification.Player\x12J\n\x10\x63ontroller_slots\x18\x08 \x03(\x0b\x32\x30.CRemotePlayTogether_Notification.ControllerSlotB\t\n\x07Message\"d\n8CRemoteClient_CreateRemotePlayTogetherInvitation_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x19\n\x11launch_parameters\x18\x02 \x01(\t\"T\n9CRemoteClient_CreateRemotePlayTogetherInvitation_Response\x12\x17\n\x0finvitation_code\x18\x01 \x01(\t\"S\n8CRemoteClient_DeleteRemotePlayTogetherInvitation_Request\x12\x17\n\x0finvitation_code\x18\x01 \x01(\t\";\n9CRemoteClient_DeleteRemotePlayTogetherInvitation_Response\"S\n8CRemoteClient_LookupRemotePlayTogetherInvitation_Request\x12\x17\n\x0finvitation_code\x18\x01 \x01(\t\"S\n9CRemoteClient_LookupRemotePlayTogetherInvitation_Response\x12\x16\n\x0einvitation_url\x18\x01 \x01(\t\"\xba\x04\n\x1d\x43\x43MRemoteClient_ClientMessage\x12\x46\n\x16\x63reate_session_request\x18\x01 \x01(\x0b\x32$.CRemoteClient_CreateSession_RequestH\x00\x12\x44\n\x15start_pairing_request\x18\x02 \x01(\x0b\x32#.CRemoteClient_StartPairing_RequestH\x00\x12I\n\x18set_pairing_info_request\x18\x03 \x01(\x0b\x32%.CRemoteClient_SetPairingInfo_RequestH\x00\x12\x46\n\x16\x63\x61ncel_pairing_request\x18\x04 \x01(\x0b\x32$.CRemoteClient_CancelPairing_RequestH\x00\x12R\n\x16register_status_update\x18\x05 \x01(\x0b\x32\x30.CRemoteClient_RegisterStatusUpdate_NotificationH\x00\x12V\n\x18unregister_status_update\x18\x06 \x01(\x0b\x32\x32.CRemoteClient_UnregisterStatusUpdate_NotificationH\x00\x12\x41\n\rremote_packet\x18\x07 \x01(\x0b\x32(.CRemoteClient_RemotePacket_NotificationH\x00\x42\t\n\x07Message\"\x9f\x03\n\x1d\x43\x43MRemoteClient_ServerMessage\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12H\n\x17\x63reate_session_response\x18\x02 \x01(\x0b\x32%.CRemoteClient_CreateSession_ResponseH\x00\x12\x46\n\x16start_pairing_response\x18\x03 \x01(\x0b\x32$.CRemoteClient_StartPairing_ResponseH\x00\x12K\n\x19set_pairing_info_response\x18\x04 \x01(\x0b\x32&.CRemoteClient_SetPairingInfo_ResponseH\x00\x12H\n\x17\x63\x61ncel_pairing_response\x18\x05 \x01(\x0b\x32%.CRemoteClient_CancelPairing_ResponseH\x00\x12:\n\x0creply_packet\x18\x06 \x01(\x0b\x32\".CRemoteClient_GetReplies_ResponseH\x00\x42\t\n\x07Message*5\n\x13\x45\x43LientTaskListType\x12\x1e\n\x1ak_EClientTask_DownloadClip\x10\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_remoteclient_service_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ECLIENTTASKLISTTYPE']._serialized_start=5608
  _globals['_ECLIENTTASKLISTTYPE']._serialized_end=5661
  _globals['_CREMOTECLIENT_CREATESESSION_REQUEST']._serialized_start=53
  _globals['_CREMOTECLIENT_CREATESESSION_REQUEST']._serialized_end=90
  _globals['_CREMOTECLIENT_CREATESESSION_RESPONSE']._serialized_start=92
  _globals['_CREMOTECLIENT_CREATESESSION_RESPONSE']._serialized_end=169
  _globals['_CREMOTECLIENT_DELETESESSION_NOTIFICATION']._serialized_start=171
  _globals['_CREMOTECLIENT_DELETESESSION_NOTIFICATION']._serialized_end=233
  _globals['_CREMOTECLIENT_STARTPAIRING_REQUEST']._serialized_start=235
  _globals['_CREMOTECLIENT_STARTPAIRING_REQUEST']._serialized_end=291
  _globals['_CREMOTECLIENT_STARTPAIRING_RESPONSE']._serialized_start=293
  _globals['_CREMOTECLIENT_STARTPAIRING_RESPONSE']._serialized_end=343
  _globals['_CREMOTECLIENT_SETPAIRINGINFO_REQUEST']._serialized_start=345
  _globals['_CREMOTECLIENT_SETPAIRINGINFO_REQUEST']._serialized_end=439
  _globals['_CREMOTECLIENT_SETPAIRINGINFO_RESPONSE']._serialized_start=441
  _globals['_CREMOTECLIENT_SETPAIRINGINFO_RESPONSE']._serialized_end=480
  _globals['_CREMOTECLIENT_GETPAIRINGINFO_REQUEST']._serialized_start=482
  _globals['_CREMOTECLIENT_GETPAIRINGINFO_REQUEST']._serialized_end=533
  _globals['_CREMOTECLIENT_GETPAIRINGINFO_RESPONSE']._serialized_start=535
  _globals['_CREMOTECLIENT_GETPAIRINGINFO_RESPONSE']._serialized_end=630
  _globals['_CREMOTECLIENT_CANCELPAIRING_REQUEST']._serialized_start=632
  _globals['_CREMOTECLIENT_CANCELPAIRING_REQUEST']._serialized_end=689
  _globals['_CREMOTECLIENT_CANCELPAIRING_RESPONSE']._serialized_start=691
  _globals['_CREMOTECLIENT_CANCELPAIRING_RESPONSE']._serialized_end=729
  _globals['_CREMOTECLIENT_REGISTERSTATUSUPDATE_NOTIFICATION']._serialized_start=731
  _globals['_CREMOTECLIENT_REGISTERSTATUSUPDATE_NOTIFICATION']._serialized_end=836
  _globals['_CREMOTECLIENT_UNREGISTERSTATUSUPDATE_NOTIFICATION']._serialized_start=838
  _globals['_CREMOTECLIENT_UNREGISTERSTATUSUPDATE_NOTIFICATION']._serialized_end=926
  _globals['_CREMOTECLIENT_DEVICEDETAILS']._serialized_start=928
  _globals['_CREMOTECLIENT_DEVICEDETAILS']._serialized_end=1032
  _globals['_CREMOTECLIENT_ONLINE_NOTIFICATION']._serialized_start=1035
  _globals['_CREMOTECLIENT_ONLINE_NOTIFICATION']._serialized_end=1167
  _globals['_CREMOTECLIENT_GETRECENTCLIENTS_REQUEST']._serialized_start=1169
  _globals['_CREMOTECLIENT_GETRECENTCLIENTS_REQUEST']._serialized_end=1209
  _globals['_CREMOTECLIENT_CLIENTLOGIN']._serialized_start=1211
  _globals['_CREMOTECLIENT_CLIENTLOGIN']._serialized_end=1336
  _globals['_CREMOTECLIENT_CLIENTDETAILS']._serialized_start=1339
  _globals['_CREMOTECLIENT_CLIENTDETAILS']._serialized_end=1532
  _globals['_CREMOTECLIENT_GETRECENTCLIENTS_RESPONSE']._serialized_start=1534
  _globals['_CREMOTECLIENT_GETRECENTCLIENTS_RESPONSE']._serialized_end=1622
  _globals['_CREMOTECLIENT_TASK']._serialized_start=1625
  _globals['_CREMOTECLIENT_TASK']._serialized_end=1756
  _globals['_CREMOTECLIENT_ADDCLIENTTASK_REQUEST']._serialized_start=1758
  _globals['_CREMOTECLIENT_ADDCLIENTTASK_REQUEST']._serialized_end=1856
  _globals['_CREMOTECLIENT_ADDCLIENTTASK_RESPONSE']._serialized_start=1858
  _globals['_CREMOTECLIENT_ADDCLIENTTASK_RESPONSE']._serialized_end=1896
  _globals['_CREMOTECLIENT_TASKLIST_NOTIFICATION']._serialized_start=1898
  _globals['_CREMOTECLIENT_TASKLIST_NOTIFICATION']._serialized_end=2000
  _globals['_CREMOTECLIENT_MARKTASKCOMPLETE_REQUEST']._serialized_start=2002
  _globals['_CREMOTECLIENT_MARKTASKCOMPLETE_REQUEST']._serialized_end=2105
  _globals['_CREMOTECLIENT_MARKTASKCOMPLETE_RESPONSE']._serialized_start=2107
  _globals['_CREMOTECLIENT_MARKTASKCOMPLETE_RESPONSE']._serialized_end=2148
  _globals['_CREMOTECLIENT_REMOTEPACKET_NOTIFICATION']._serialized_start=2150
  _globals['_CREMOTECLIENT_REMOTEPACKET_NOTIFICATION']._serialized_end=2245
  _globals['_CREMOTECLIENT_REPLYPACKET_NOTIFICATION']._serialized_start=2247
  _globals['_CREMOTECLIENT_REPLYPACKET_NOTIFICATION']._serialized_end=2324
  _globals['_CREMOTECLIENT_GETREPLIES_REQUEST']._serialized_start=2326
  _globals['_CREMOTECLIENT_GETREPLIES_REQUEST']._serialized_end=2380
  _globals['_CREMOTECLIENT_GETREPLIES_RESPONSE']._serialized_start=2382
  _globals['_CREMOTECLIENT_GETREPLIES_RESPONSE']._serialized_end=2434
  _globals['_CREMOTECLIENT_ALLOCATERELAYSERVER_REQUEST']._serialized_start=2436
  _globals['_CREMOTECLIENT_ALLOCATERELAYSERVER_REQUEST']._serialized_end=2516
  _globals['_CREMOTECLIENT_ALLOCATERELAYSERVER_RESPONSE']._serialized_start=2518
  _globals['_CREMOTECLIENT_ALLOCATERELAYSERVER_RESPONSE']._serialized_end=2584
  _globals['_CREMOTECLIENT_ALLOCATESDR_REQUEST']._serialized_start=2586
  _globals['_CREMOTECLIENT_ALLOCATESDR_REQUEST']._serialized_end=2636
  _globals['_CREMOTECLIENT_ALLOCATESDR_RESPONSE']._serialized_start=2638
  _globals['_CREMOTECLIENT_ALLOCATESDR_RESPONSE']._serialized_end=2674
  _globals['_CREMOTECLIENT_STEAMBROADCAST_NOTIFICATION']._serialized_start=2676
  _globals['_CREMOTECLIENT_STEAMBROADCAST_NOTIFICATION']._serialized_end=2771
  _globals['_CREMOTECLIENT_STEAMTOSTEAM_NOTIFICATION']._serialized_start=2774
  _globals['_CREMOTECLIENT_STEAMTOSTEAM_NOTIFICATION']._serialized_end=2921
  _globals['_CREMOTEPLAY_SESSIONSTARTED_REQUEST']._serialized_start=2924
  _globals['_CREMOTEPLAY_SESSIONSTARTED_REQUEST']._serialized_end=3108
  _globals['_CREMOTEPLAY_SESSIONSTARTED_RESPONSE']._serialized_start=3110
  _globals['_CREMOTEPLAY_SESSIONSTARTED_RESPONSE']._serialized_end=3166
  _globals['_CREMOTEPLAY_SESSIONSTOPPED_NOTIFICATION']._serialized_start=3168
  _globals['_CREMOTEPLAY_SESSIONSTOPPED_NOTIFICATION']._serialized_end=3285
  _globals['_CREMOTEPLAYTOGETHER_NOTIFICATION']._serialized_start=3288
  _globals['_CREMOTEPLAYTOGETHER_NOTIFICATION']._serialized_end=4111
  _globals['_CREMOTEPLAYTOGETHER_NOTIFICATION_PLAYER']._serialized_start=3415
  _globals['_CREMOTEPLAYTOGETHER_NOTIFICATION_PLAYER']._serialized_end=3555
  _globals['_CREMOTEPLAYTOGETHER_NOTIFICATION_CONTROLLERSLOT_OBSOLETE']._serialized_start=3557
  _globals['_CREMOTEPLAYTOGETHER_NOTIFICATION_CONTROLLERSLOT_OBSOLETE']._serialized_end=3615
  _globals['_CREMOTEPLAYTOGETHER_NOTIFICATION_CONTROLLERSLOT']._serialized_start=3617
  _globals['_CREMOTEPLAYTOGETHER_NOTIFICATION_CONTROLLERSLOT']._serialized_end=3732
  _globals['_CREMOTEPLAYTOGETHER_NOTIFICATION_GROUPUPDATED']._serialized_start=3735
  _globals['_CREMOTEPLAYTOGETHER_NOTIFICATION_GROUPUPDATED']._serialized_end=4100
  _globals['_CREMOTECLIENT_CREATEREMOTEPLAYTOGETHERINVITATION_REQUEST']._serialized_start=4113
  _globals['_CREMOTECLIENT_CREATEREMOTEPLAYTOGETHERINVITATION_REQUEST']._serialized_end=4213
  _globals['_CREMOTECLIENT_CREATEREMOTEPLAYTOGETHERINVITATION_RESPONSE']._serialized_start=4215
  _globals['_CREMOTECLIENT_CREATEREMOTEPLAYTOGETHERINVITATION_RESPONSE']._serialized_end=4299
  _globals['_CREMOTECLIENT_DELETEREMOTEPLAYTOGETHERINVITATION_REQUEST']._serialized_start=4301
  _globals['_CREMOTECLIENT_DELETEREMOTEPLAYTOGETHERINVITATION_REQUEST']._serialized_end=4384
  _globals['_CREMOTECLIENT_DELETEREMOTEPLAYTOGETHERINVITATION_RESPONSE']._serialized_start=4386
  _globals['_CREMOTECLIENT_DELETEREMOTEPLAYTOGETHERINVITATION_RESPONSE']._serialized_end=4445
  _globals['_CREMOTECLIENT_LOOKUPREMOTEPLAYTOGETHERINVITATION_REQUEST']._serialized_start=4447
  _globals['_CREMOTECLIENT_LOOKUPREMOTEPLAYTOGETHERINVITATION_REQUEST']._serialized_end=4530
  _globals['_CREMOTECLIENT_LOOKUPREMOTEPLAYTOGETHERINVITATION_RESPONSE']._serialized_start=4532
  _globals['_CREMOTECLIENT_LOOKUPREMOTEPLAYTOGETHERINVITATION_RESPONSE']._serialized_end=4615
  _globals['_CCMREMOTECLIENT_CLIENTMESSAGE']._serialized_start=4618
  _globals['_CCMREMOTECLIENT_CLIENTMESSAGE']._serialized_end=5188
  _globals['_CCMREMOTECLIENT_SERVERMESSAGE']._serialized_start=5191
  _globals['_CCMREMOTECLIENT_SERVERMESSAGE']._serialized_end=5606
# @@protoc_insertion_point(module_scope)
