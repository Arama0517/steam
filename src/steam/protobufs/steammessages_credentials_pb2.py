# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_credentials.proto
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
    'steammessages_credentials.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsteammessages_credentials.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"q\n*CCredentials_TestAvailablePassword_Request\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x1b\n\x13sha_digest_password\x18\x02 \x01(\x0c\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x03 \x01(\t\"?\n+CCredentials_TestAvailablePassword_Response\x12\x10\n\x08is_valid\x18\x03 \x01(\x08\"\xa2\x01\n)CCredentials_GetSteamGuardDetails_Request\x12\x11\n\twebcookie\x18\x02 \x01(\t\x12 \n\x18timestamp_minimum_wanted\x18\x03 \x01(\x07\x12\x1c\n\x14\x64\x65precated_ipaddress\x18\x04 \x01(\x05\x12\"\n\nip_address\x18\x05 \x01(\x0b\x32\x0e.CMsgIPAddress\"\xff\x05\n*CCredentials_GetSteamGuardDetails_Response\x12\x1d\n\x15is_steamguard_enabled\x18\x01 \x01(\x08\x12$\n\x1ctimestamp_steamguard_enabled\x18\x02 \x01(\x07\x12*\n\"deprecated_machine_name_userchosen\x18\x04 \x01(\t\x12\x37\n/deprecated_timestamp_machine_steamguard_enabled\x18\x05 \x01(\x07\x12\x43\n;deprecated_authentication_exists_from_geoloc_before_mintime\x18\x06 \x01(\x08\x12\x1d\n\x15\x64\x65precated_machine_id\x18\x07 \x01(\x04\x12M\n\x0csession_data\x18\x08 \x03(\x0b\x32\x37.CCredentials_GetSteamGuardDetails_Response.SessionData\x12\x1c\n\x14is_twofactor_enabled\x18\t \x01(\x08\x12#\n\x1btimestamp_twofactor_enabled\x18\n \x01(\x07\x12\x19\n\x11is_phone_verified\x18\x0b \x01(\x08\x1a\x95\x02\n\x0bSessionData\x12\x12\n\nmachine_id\x18\x01 \x01(\x04\x12\x1f\n\x17machine_name_userchosen\x18\x02 \x01(\t\x12,\n$timestamp_machine_steamguard_enabled\x18\x03 \x01(\x07\x12\x38\n0authentication_exists_from_geoloc_before_mintime\x18\x04 \x01(\x08\x12\x39\n1authentication_exists_from_same_ip_before_mintime\x18\x06 \x01(\x08\x12\x13\n\x0bpublic_ipv4\x18\x07 \x01(\r\x12\x19\n\x11public_ip_address\x18\x08 \x01(\t\";\n)CCredentials_ValidateEmailAddress_Request\x12\x0e\n\x06stoken\x18\x01 \x01(\t\"C\n*CCredentials_ValidateEmailAddress_Response\x12\x15\n\rwas_validated\x18\x01 \x01(\x08\"_\n-CCredentials_SteamGuardPhishingReport_Request\x12\x14\n\x0cparam_string\x18\x01 \x01(\t\x12\x18\n\x10ipaddress_actual\x18\x02 \x01(\t\"\xb3\x02\n.CCredentials_SteamGuardPhishingReport_Response\x12\x1e\n\x16ipaddress_loginattempt\x18\x01 \x01(\t\x12 \n\x18\x63ountryname_loginattempt\x18\x02 \x01(\t\x12\x1e\n\x16statename_loginattempt\x18\x03 \x01(\t\x12\x1d\n\x15\x63ityname_loginattempt\x18\x04 \x01(\t\x12\x18\n\x10ipaddress_actual\x18\x05 \x01(\t\x12\x1a\n\x12\x63ountryname_actual\x18\x06 \x01(\t\x12\x18\n\x10statename_actual\x18\x07 \x01(\t\x12\x17\n\x0f\x63ityname_actual\x18\x08 \x01(\t\x12\x17\n\x0fsteamguard_code\x18\t \x01(\t\"J\n-CCredentials_LastCredentialChangeTime_Request\x12\x19\n\x11user_changes_only\x18\x01 \x01(\x08\"\xa4\x01\n.CCredentials_LastCredentialChangeTime_Response\x12&\n\x1etimestamp_last_password_change\x18\x01 \x01(\x07\x12#\n\x1btimestamp_last_email_change\x18\x02 \x01(\x07\x12%\n\x1dtimestamp_last_password_reset\x18\x03 \x01(\x07\"+\n)CCredentials_GetAccountAuthSecret_Request\"O\n*CCredentials_GetAccountAuthSecret_Response\x12\x11\n\tsecret_id\x18\x01 \x01(\x05\x12\x0e\n\x06secret\x18\x02 \x01(\x0c\x32\xd5\x05\n\x0b\x43redentials\x12r\n\x15TestAvailablePassword\x12+.CCredentials_TestAvailablePassword_Request\x1a,.CCredentials_TestAvailablePassword_Response\x12o\n\x14GetSteamGuardDetails\x12*.CCredentials_GetSteamGuardDetails_Request\x1a+.CCredentials_GetSteamGuardDetails_Response\x12o\n\x14ValidateEmailAddress\x12*.CCredentials_ValidateEmailAddress_Request\x1a+.CCredentials_ValidateEmailAddress_Response\x12{\n\x18SteamGuardPhishingReport\x12..CCredentials_SteamGuardPhishingReport_Request\x1a/.CCredentials_SteamGuardPhishingReport_Response\x12\x81\x01\n\x1eGetCredentialChangeTimeDetails\x12..CCredentials_LastCredentialChangeTime_Request\x1a/.CCredentials_LastCredentialChangeTime_Response\x12o\n\x14GetAccountAuthSecret\x12*.CCredentials_GetAccountAuthSecret_Request\x1a+.CCredentials_GetAccountAuthSecret_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_credentials_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CCREDENTIALS_TESTAVAILABLEPASSWORD_REQUEST']._serialized_start=95
  _globals['_CCREDENTIALS_TESTAVAILABLEPASSWORD_REQUEST']._serialized_end=208
  _globals['_CCREDENTIALS_TESTAVAILABLEPASSWORD_RESPONSE']._serialized_start=210
  _globals['_CCREDENTIALS_TESTAVAILABLEPASSWORD_RESPONSE']._serialized_end=273
  _globals['_CCREDENTIALS_GETSTEAMGUARDDETAILS_REQUEST']._serialized_start=276
  _globals['_CCREDENTIALS_GETSTEAMGUARDDETAILS_REQUEST']._serialized_end=438
  _globals['_CCREDENTIALS_GETSTEAMGUARDDETAILS_RESPONSE']._serialized_start=441
  _globals['_CCREDENTIALS_GETSTEAMGUARDDETAILS_RESPONSE']._serialized_end=1208
  _globals['_CCREDENTIALS_GETSTEAMGUARDDETAILS_RESPONSE_SESSIONDATA']._serialized_start=931
  _globals['_CCREDENTIALS_GETSTEAMGUARDDETAILS_RESPONSE_SESSIONDATA']._serialized_end=1208
  _globals['_CCREDENTIALS_VALIDATEEMAILADDRESS_REQUEST']._serialized_start=1210
  _globals['_CCREDENTIALS_VALIDATEEMAILADDRESS_REQUEST']._serialized_end=1269
  _globals['_CCREDENTIALS_VALIDATEEMAILADDRESS_RESPONSE']._serialized_start=1271
  _globals['_CCREDENTIALS_VALIDATEEMAILADDRESS_RESPONSE']._serialized_end=1338
  _globals['_CCREDENTIALS_STEAMGUARDPHISHINGREPORT_REQUEST']._serialized_start=1340
  _globals['_CCREDENTIALS_STEAMGUARDPHISHINGREPORT_REQUEST']._serialized_end=1435
  _globals['_CCREDENTIALS_STEAMGUARDPHISHINGREPORT_RESPONSE']._serialized_start=1438
  _globals['_CCREDENTIALS_STEAMGUARDPHISHINGREPORT_RESPONSE']._serialized_end=1745
  _globals['_CCREDENTIALS_LASTCREDENTIALCHANGETIME_REQUEST']._serialized_start=1747
  _globals['_CCREDENTIALS_LASTCREDENTIALCHANGETIME_REQUEST']._serialized_end=1821
  _globals['_CCREDENTIALS_LASTCREDENTIALCHANGETIME_RESPONSE']._serialized_start=1824
  _globals['_CCREDENTIALS_LASTCREDENTIALCHANGETIME_RESPONSE']._serialized_end=1988
  _globals['_CCREDENTIALS_GETACCOUNTAUTHSECRET_REQUEST']._serialized_start=1990
  _globals['_CCREDENTIALS_GETACCOUNTAUTHSECRET_REQUEST']._serialized_end=2033
  _globals['_CCREDENTIALS_GETACCOUNTAUTHSECRET_RESPONSE']._serialized_start=2035
  _globals['_CCREDENTIALS_GETACCOUNTAUTHSECRET_RESPONSE']._serialized_end=2114
  _globals['_CREDENTIALS']._serialized_start=2117
  _globals['_CREDENTIALS']._serialized_end=2842
_builder.BuildServices(DESCRIPTOR, 'steammessages_credentials_pb2', _globals)
# @@protoc_insertion_point(module_scope)
