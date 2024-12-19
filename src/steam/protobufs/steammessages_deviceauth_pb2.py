# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_deviceauth.proto
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
    'steammessages_deviceauth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esteammessages_deviceauth.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"X\n+CDeviceAuth_GetOwnAuthorizedDevices_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10include_canceled\x18\x02 \x01(\x08\"\xb8\x02\n,CDeviceAuth_GetOwnAuthorizedDevices_Response\x12\x45\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x34.CDeviceAuth_GetOwnAuthorizedDevices_Response.Device\x1a\xc0\x01\n\x06\x44\x65vice\x12\x19\n\x11\x61uth_device_token\x18\x01 \x01(\x06\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x12\n\nis_pending\x18\x03 \x01(\x08\x12\x13\n\x0bis_canceled\x18\x04 \x01(\x08\x12\x16\n\x0elast_time_used\x18\x05 \x01(\r\x12\x18\n\x10last_borrower_id\x18\x06 \x01(\x06\x12\x17\n\x0flast_app_played\x18\x07 \x01(\r\x12\x12\n\nis_limited\x18\x08 \x01(\x08\"\x85\x01\n.CDeviceAuth_AcceptAuthorizationRequest_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x19\n\x11\x61uth_device_token\x18\x02 \x01(\x06\x12\x11\n\tauth_code\x18\x03 \x01(\x06\x12\x14\n\x0c\x66rom_steamid\x18\x04 \x01(\x06\"1\n/CDeviceAuth_AcceptAuthorizationRequest_Response\"W\n)CDeviceAuth_AuthorizeRemoteDevice_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x19\n\x11\x61uth_device_token\x18\x02 \x01(\x06\",\n*CDeviceAuth_AuthorizeRemoteDevice_Response\"Y\n+CDeviceAuth_DeauthorizeRemoteDevice_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x19\n\x11\x61uth_device_token\x18\x02 \x01(\x06\".\n,CDeviceAuth_DeauthorizeRemoteDevice_Response\"?\n,CDeviceAuth_GetUsedAuthorizedDevices_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"\xfa\x01\n-CDeviceAuth_GetUsedAuthorizedDevices_Response\x12\x46\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x35.CDeviceAuth_GetUsedAuthorizedDevices_Response.Device\x1a\x80\x01\n\x06\x44\x65vice\x12\x19\n\x11\x61uth_device_token\x18\x01 \x01(\x06\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x15\n\rowner_steamid\x18\x03 \x01(\x06\x12\x16\n\x0elast_time_used\x18\x04 \x01(\r\x12\x17\n\x0flast_app_played\x18\x05 \x01(\r\"p\n*CDeviceAuth_GetAuthorizedBorrowers_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10include_canceled\x18\x02 \x01(\x08\x12\x17\n\x0finclude_pending\x18\x03 \x01(\x08\"\xd3\x01\n+CDeviceAuth_GetAuthorizedBorrowers_Response\x12H\n\tborrowers\x18\x01 \x03(\x0b\x32\x35.CDeviceAuth_GetAuthorizedBorrowers_Response.Borrower\x1aZ\n\x08\x42orrower\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x12\n\nis_pending\x18\x02 \x01(\x08\x12\x13\n\x0bis_canceled\x18\x03 \x01(\x08\x12\x14\n\x0ctime_created\x18\x04 \x01(\r\"W\n*CDeviceAuth_AddAuthorizedBorrowers_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10steamid_borrower\x18\x02 \x03(\x06\"F\n+CDeviceAuth_AddAuthorizedBorrowers_Response\x12\x17\n\x0fseconds_to_wait\x18\x01 \x01(\x05\"Z\n-CDeviceAuth_RemoveAuthorizedBorrowers_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10steamid_borrower\x18\x02 \x03(\x06\"0\n.CDeviceAuth_RemoveAuthorizedBorrowers_Response\"q\n+CDeviceAuth_GetAuthorizedAsBorrower_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10include_canceled\x18\x02 \x01(\x08\x12\x17\n\x0finclude_pending\x18\x03 \x01(\x08\"\x8b\x02\n,CDeviceAuth_GetAuthorizedAsBorrower_Response\x12\x45\n\x07lenders\x18\x01 \x03(\x0b\x32\x34.CDeviceAuth_GetAuthorizedAsBorrower_Response.Lender\x1a\x93\x01\n\x06Lender\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x14\n\x0ctime_created\x18\x02 \x01(\r\x12\x12\n\nis_pending\x18\x03 \x01(\x08\x12\x13\n\x0bis_canceled\x18\x04 \x01(\x08\x12\x0f\n\x07is_used\x18\x05 \x01(\x08\x12\x14\n\x0ctime_removed\x18\x06 \x01(\r\x12\x12\n\ntime_first\x18\x07 \x01(\r\"@\n-CDeviceAuth_GetExcludedGamesInLibrary_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"\xe6\x01\n.CDeviceAuth_GetExcludedGamesInLibrary_Response\x12T\n\x0e\x65xcluded_games\x18\x01 \x03(\x0b\x32<.CDeviceAuth_GetExcludedGamesInLibrary_Response.ExcludedGame\x1a^\n\x0c\x45xcludedGame\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\tgame_name\x18\x02 \x01(\t\x12\x12\n\nvac_banned\x18\x03 \x01(\x08\x12\x18\n\x10package_excluded\x18\x04 \x01(\x08\"L\n*CDeviceAuth_GetBorrowerPlayHistory_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\"\xb8\x02\n+CDeviceAuth_GetBorrowerPlayHistory_Response\x12R\n\x0elender_history\x18\x01 \x03(\x0b\x32:.CDeviceAuth_GetBorrowerPlayHistory_Response.LenderHistory\x1a\x43\n\x0bGameHistory\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\ttime_last\x18\x02 \x01(\r\x12\x12\n\ntime_total\x18\x03 \x01(\r\x1ap\n\rLenderHistory\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12N\n\x0cgame_history\x18\x02 \x03(\x0b\x32\x38.CDeviceAuth_GetBorrowerPlayHistory_Response.GameHistory2\xbd\n\n\nDeviceAuth\x12v\n\x17GetOwnAuthorizedDevices\x12,.CDeviceAuth_GetOwnAuthorizedDevices_Request\x1a-.CDeviceAuth_GetOwnAuthorizedDevices_Response\x12\x7f\n\x1a\x41\x63\x63\x65ptAuthorizationRequest\x12/.CDeviceAuth_AcceptAuthorizationRequest_Request\x1a\x30.CDeviceAuth_AcceptAuthorizationRequest_Response\x12p\n\x15\x41uthorizeRemoteDevice\x12*.CDeviceAuth_AuthorizeRemoteDevice_Request\x1a+.CDeviceAuth_AuthorizeRemoteDevice_Response\x12v\n\x17\x44\x65\x61uthorizeRemoteDevice\x12,.CDeviceAuth_DeauthorizeRemoteDevice_Request\x1a-.CDeviceAuth_DeauthorizeRemoteDevice_Response\x12y\n\x18GetUsedAuthorizedDevices\x12-.CDeviceAuth_GetUsedAuthorizedDevices_Request\x1a..CDeviceAuth_GetUsedAuthorizedDevices_Response\x12s\n\x16GetAuthorizedBorrowers\x12+.CDeviceAuth_GetAuthorizedBorrowers_Request\x1a,.CDeviceAuth_GetAuthorizedBorrowers_Response\x12s\n\x16\x41\x64\x64\x41uthorizedBorrowers\x12+.CDeviceAuth_AddAuthorizedBorrowers_Request\x1a,.CDeviceAuth_AddAuthorizedBorrowers_Response\x12|\n\x19RemoveAuthorizedBorrowers\x12..CDeviceAuth_RemoveAuthorizedBorrowers_Request\x1a/.CDeviceAuth_RemoveAuthorizedBorrowers_Response\x12v\n\x17GetAuthorizedAsBorrower\x12,.CDeviceAuth_GetAuthorizedAsBorrower_Request\x1a-.CDeviceAuth_GetAuthorizedAsBorrower_Response\x12|\n\x19GetExcludedGamesInLibrary\x12..CDeviceAuth_GetExcludedGamesInLibrary_Request\x1a/.CDeviceAuth_GetExcludedGamesInLibrary_Response\x12s\n\x16GetBorrowerPlayHistory\x12+.CDeviceAuth_GetBorrowerPlayHistory_Request\x1a,.CDeviceAuth_GetBorrowerPlayHistory_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_deviceauth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CDEVICEAUTH_GETOWNAUTHORIZEDDEVICES_REQUEST']._serialized_start=94
  _globals['_CDEVICEAUTH_GETOWNAUTHORIZEDDEVICES_REQUEST']._serialized_end=182
  _globals['_CDEVICEAUTH_GETOWNAUTHORIZEDDEVICES_RESPONSE']._serialized_start=185
  _globals['_CDEVICEAUTH_GETOWNAUTHORIZEDDEVICES_RESPONSE']._serialized_end=497
  _globals['_CDEVICEAUTH_GETOWNAUTHORIZEDDEVICES_RESPONSE_DEVICE']._serialized_start=305
  _globals['_CDEVICEAUTH_GETOWNAUTHORIZEDDEVICES_RESPONSE_DEVICE']._serialized_end=497
  _globals['_CDEVICEAUTH_ACCEPTAUTHORIZATIONREQUEST_REQUEST']._serialized_start=500
  _globals['_CDEVICEAUTH_ACCEPTAUTHORIZATIONREQUEST_REQUEST']._serialized_end=633
  _globals['_CDEVICEAUTH_ACCEPTAUTHORIZATIONREQUEST_RESPONSE']._serialized_start=635
  _globals['_CDEVICEAUTH_ACCEPTAUTHORIZATIONREQUEST_RESPONSE']._serialized_end=684
  _globals['_CDEVICEAUTH_AUTHORIZEREMOTEDEVICE_REQUEST']._serialized_start=686
  _globals['_CDEVICEAUTH_AUTHORIZEREMOTEDEVICE_REQUEST']._serialized_end=773
  _globals['_CDEVICEAUTH_AUTHORIZEREMOTEDEVICE_RESPONSE']._serialized_start=775
  _globals['_CDEVICEAUTH_AUTHORIZEREMOTEDEVICE_RESPONSE']._serialized_end=819
  _globals['_CDEVICEAUTH_DEAUTHORIZEREMOTEDEVICE_REQUEST']._serialized_start=821
  _globals['_CDEVICEAUTH_DEAUTHORIZEREMOTEDEVICE_REQUEST']._serialized_end=910
  _globals['_CDEVICEAUTH_DEAUTHORIZEREMOTEDEVICE_RESPONSE']._serialized_start=912
  _globals['_CDEVICEAUTH_DEAUTHORIZEREMOTEDEVICE_RESPONSE']._serialized_end=958
  _globals['_CDEVICEAUTH_GETUSEDAUTHORIZEDDEVICES_REQUEST']._serialized_start=960
  _globals['_CDEVICEAUTH_GETUSEDAUTHORIZEDDEVICES_REQUEST']._serialized_end=1023
  _globals['_CDEVICEAUTH_GETUSEDAUTHORIZEDDEVICES_RESPONSE']._serialized_start=1026
  _globals['_CDEVICEAUTH_GETUSEDAUTHORIZEDDEVICES_RESPONSE']._serialized_end=1276
  _globals['_CDEVICEAUTH_GETUSEDAUTHORIZEDDEVICES_RESPONSE_DEVICE']._serialized_start=1148
  _globals['_CDEVICEAUTH_GETUSEDAUTHORIZEDDEVICES_RESPONSE_DEVICE']._serialized_end=1276
  _globals['_CDEVICEAUTH_GETAUTHORIZEDBORROWERS_REQUEST']._serialized_start=1278
  _globals['_CDEVICEAUTH_GETAUTHORIZEDBORROWERS_REQUEST']._serialized_end=1390
  _globals['_CDEVICEAUTH_GETAUTHORIZEDBORROWERS_RESPONSE']._serialized_start=1393
  _globals['_CDEVICEAUTH_GETAUTHORIZEDBORROWERS_RESPONSE']._serialized_end=1604
  _globals['_CDEVICEAUTH_GETAUTHORIZEDBORROWERS_RESPONSE_BORROWER']._serialized_start=1514
  _globals['_CDEVICEAUTH_GETAUTHORIZEDBORROWERS_RESPONSE_BORROWER']._serialized_end=1604
  _globals['_CDEVICEAUTH_ADDAUTHORIZEDBORROWERS_REQUEST']._serialized_start=1606
  _globals['_CDEVICEAUTH_ADDAUTHORIZEDBORROWERS_REQUEST']._serialized_end=1693
  _globals['_CDEVICEAUTH_ADDAUTHORIZEDBORROWERS_RESPONSE']._serialized_start=1695
  _globals['_CDEVICEAUTH_ADDAUTHORIZEDBORROWERS_RESPONSE']._serialized_end=1765
  _globals['_CDEVICEAUTH_REMOVEAUTHORIZEDBORROWERS_REQUEST']._serialized_start=1767
  _globals['_CDEVICEAUTH_REMOVEAUTHORIZEDBORROWERS_REQUEST']._serialized_end=1857
  _globals['_CDEVICEAUTH_REMOVEAUTHORIZEDBORROWERS_RESPONSE']._serialized_start=1859
  _globals['_CDEVICEAUTH_REMOVEAUTHORIZEDBORROWERS_RESPONSE']._serialized_end=1907
  _globals['_CDEVICEAUTH_GETAUTHORIZEDASBORROWER_REQUEST']._serialized_start=1909
  _globals['_CDEVICEAUTH_GETAUTHORIZEDASBORROWER_REQUEST']._serialized_end=2022
  _globals['_CDEVICEAUTH_GETAUTHORIZEDASBORROWER_RESPONSE']._serialized_start=2025
  _globals['_CDEVICEAUTH_GETAUTHORIZEDASBORROWER_RESPONSE']._serialized_end=2292
  _globals['_CDEVICEAUTH_GETAUTHORIZEDASBORROWER_RESPONSE_LENDER']._serialized_start=2145
  _globals['_CDEVICEAUTH_GETAUTHORIZEDASBORROWER_RESPONSE_LENDER']._serialized_end=2292
  _globals['_CDEVICEAUTH_GETEXCLUDEDGAMESINLIBRARY_REQUEST']._serialized_start=2294
  _globals['_CDEVICEAUTH_GETEXCLUDEDGAMESINLIBRARY_REQUEST']._serialized_end=2358
  _globals['_CDEVICEAUTH_GETEXCLUDEDGAMESINLIBRARY_RESPONSE']._serialized_start=2361
  _globals['_CDEVICEAUTH_GETEXCLUDEDGAMESINLIBRARY_RESPONSE']._serialized_end=2591
  _globals['_CDEVICEAUTH_GETEXCLUDEDGAMESINLIBRARY_RESPONSE_EXCLUDEDGAME']._serialized_start=2497
  _globals['_CDEVICEAUTH_GETEXCLUDEDGAMESINLIBRARY_RESPONSE_EXCLUDEDGAME']._serialized_end=2591
  _globals['_CDEVICEAUTH_GETBORROWERPLAYHISTORY_REQUEST']._serialized_start=2593
  _globals['_CDEVICEAUTH_GETBORROWERPLAYHISTORY_REQUEST']._serialized_end=2669
  _globals['_CDEVICEAUTH_GETBORROWERPLAYHISTORY_RESPONSE']._serialized_start=2672
  _globals['_CDEVICEAUTH_GETBORROWERPLAYHISTORY_RESPONSE']._serialized_end=2984
  _globals['_CDEVICEAUTH_GETBORROWERPLAYHISTORY_RESPONSE_GAMEHISTORY']._serialized_start=2803
  _globals['_CDEVICEAUTH_GETBORROWERPLAYHISTORY_RESPONSE_GAMEHISTORY']._serialized_end=2870
  _globals['_CDEVICEAUTH_GETBORROWERPLAYHISTORY_RESPONSE_LENDERHISTORY']._serialized_start=2872
  _globals['_CDEVICEAUTH_GETBORROWERPLAYHISTORY_RESPONSE_LENDERHISTORY']._serialized_end=2984
  _globals['_DEVICEAUTH']._serialized_start=2987
  _globals['_DEVICEAUTH']._serialized_end=4328
_builder.BuildServices(DESCRIPTOR, 'steammessages_deviceauth_pb2', _globals)
# @@protoc_insertion_point(module_scope)
