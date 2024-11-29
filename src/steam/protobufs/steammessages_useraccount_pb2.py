# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_useraccount.proto
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
    'steammessages_useraccount.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsteammessages_useraccount.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"P\n8CUserAccount_GetAvailableValveDiscountPromotions_Request\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\"\x85\x04\n9CUserAccount_GetAvailableValveDiscountPromotions_Response\x12l\n\npromotions\x18\x01 \x03(\x0b\x32X.CUserAccount_GetAvailableValveDiscountPromotions_Response.ValveDiscountPromotionDetails\x1a\xd9\x02\n\x1dValveDiscountPromotionDetails\x12\x13\n\x0bpromotionid\x18\x01 \x01(\r\x12\x1d\n\x15promotion_description\x18\x02 \x01(\t\x12\x1b\n\x13minimum_cart_amount\x18\x03 \x01(\x03\x12\'\n\x1fminimum_cart_amount_for_display\x18\x04 \x01(\x03\x12\x17\n\x0f\x64iscount_amount\x18\x05 \x01(\x03\x12\x15\n\rcurrency_code\x18\x06 \x01(\x05\x12\x1b\n\x13\x61vailable_use_count\x18\x07 \x01(\x05\x12!\n\x19promotional_discount_type\x18\x08 \x01(\x05\x12\x19\n\x11loyalty_reward_id\x18\t \x01(\x05\x12\x1c\n\x14localized_name_token\x18\n \x01(\t\x12\x15\n\rmax_use_count\x18\x0b \x01(\x05\"\x8a\x01\n+CUserAccount_GetClientWalletDetails_Request\x12\x1e\n\x16include_balance_in_usd\x18\x01 \x01(\x08\x12\x18\n\rwallet_region\x18\x02 \x01(\x05:\x01\x31\x12!\n\x19include_formatted_balance\x18\x03 \x01(\x08\"\xb5\x04\n&CUserAccount_GetWalletDetails_Response\x12\x12\n\nhas_wallet\x18\x01 \x01(\x08\x12\x19\n\x11user_country_code\x18\x02 \x01(\t\x12\x1b\n\x13wallet_country_code\x18\x03 \x01(\t\x12\x14\n\x0cwallet_state\x18\x04 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x05 \x01(\x03\x12\x17\n\x0f\x64\x65layed_balance\x18\x06 \x01(\x03\x12\x15\n\rcurrency_code\x18\x07 \x01(\x05\x12\x1c\n\x14time_most_recent_txn\x18\x08 \x01(\r\x12\x19\n\x11most_recent_txnid\x18\t \x01(\x04\x12\x16\n\x0e\x62\x61lance_in_usd\x18\n \x01(\x03\x12\x1e\n\x16\x64\x65layed_balance_in_usd\x18\x0b \x01(\x03\x12#\n\x1bhas_wallet_in_other_regions\x18\x0c \x01(\x08\x12\x15\n\rother_regions\x18\r \x03(\x05\x12\x19\n\x11\x66ormatted_balance\x18\x0e \x01(\t\x12!\n\x19\x66ormatted_delayed_balance\x18\x0f \x01(\t\x12*\n\"delayed_balance_available_min_time\x18\x10 \x01(\x05\x12*\n\"delayed_balance_available_max_time\x18\x11 \x01(\x05\x12%\n\x1d\x64\x65layed_balance_newest_source\x18\x12 \x01(\x05\"+\n)CUserAccount_GetAccountLinkStatus_Request\"}\n*CUserAccount_GetAccountLinkStatus_Response\x12\x0c\n\x04pwid\x18\x01 \x01(\r\x12\x1d\n\x15identity_verification\x18\x02 \x01(\r\x12\"\n\x1aperformed_age_verification\x18\x03 \x01(\x08\"9\n(CUserAccount_CancelLicenseForApp_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"+\n)CUserAccount_CancelLicenseForApp_Response\"6\n#CUserAccount_GetUserCountry_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"7\n$CUserAccount_GetUserCountry_Response\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\"r\n,CUserAccount_CreateFriendInviteToken_Request\x12\x14\n\x0cinvite_limit\x18\x01 \x01(\r\x12\x17\n\x0finvite_duration\x18\x02 \x01(\r\x12\x13\n\x0binvite_note\x18\x03 \x01(\t\"\x99\x01\n-CUserAccount_CreateFriendInviteToken_Response\x12\x14\n\x0cinvite_token\x18\x01 \x01(\t\x12\x14\n\x0cinvite_limit\x18\x02 \x01(\x04\x12\x17\n\x0finvite_duration\x18\x03 \x01(\x04\x12\x14\n\x0ctime_created\x18\x04 \x01(\x07\x12\r\n\x05valid\x18\x05 \x01(\x08\",\n*CUserAccount_GetFriendInviteTokens_Request\"m\n+CUserAccount_GetFriendInviteTokens_Response\x12>\n\x06tokens\x18\x01 \x03(\x0b\x32..CUserAccount_CreateFriendInviteToken_Response\"S\n*CUserAccount_ViewFriendInviteToken_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x14\n\x0cinvite_token\x18\x02 \x01(\t\"f\n+CUserAccount_ViewFriendInviteToken_Response\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\x12\x17\n\x0finvite_duration\x18\x03 \x01(\x04\"U\n,CUserAccount_RedeemFriendInviteToken_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x14\n\x0cinvite_token\x18\x02 \x01(\t\"/\n-CUserAccount_RedeemFriendInviteToken_Response\"D\n,CUserAccount_RevokeFriendInviteToken_Request\x12\x14\n\x0cinvite_token\x18\x01 \x01(\t\"/\n-CUserAccount_RevokeFriendInviteToken_Response\">\n\'CUserAccount_RegisterCompatTool_Request\x12\x13\n\x0b\x63ompat_tool\x18\x01 \x01(\r\"*\n(CUserAccount_RegisterCompatTool_Response\"\xe1\x01\n,CAccountLinking_GetLinkedAccountInfo_Request\x12H\n\x0c\x61\x63\x63ount_type\x18\x01 \x01(\x0e\x32\x15.EInternalAccountType:\x1bk_EInternalSteamAccountType\x12\x12\n\naccount_id\x18\x02 \x01(\x04\x12\x36\n\x06\x66ilter\x18\x03 \x01(\x0e\x32\x15.EExternalAccountType:\x0fk_EExternalNone\x12\x1b\n\x13return_access_token\x18\x04 \x01(\x08\"\x87\x03\n-CAccountLinking_GetLinkedAccountInfo_Response\x12h\n\x11\x65xternal_accounts\x18\x01 \x03(\x0b\x32M.CAccountLinking_GetLinkedAccountInfo_Response.CExternalAccountTuple_Response\x1a\xeb\x01\n\x1e\x43\x45xternalAccountTuple_Response\x12=\n\rexternal_type\x18\x01 \x01(\x0e\x32\x15.EExternalAccountType:\x0fk_EExternalNone\x12\x13\n\x0b\x65xternal_id\x18\x02 \x01(\t\x12\x1a\n\x12\x65xternal_user_name\x18\x03 \x01(\t\x12\x14\n\x0c\x65xternal_url\x18\x04 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x05 \x01(\t\x12\x1b\n\x13\x61\x63\x63\x65ss_token_secret\x18\x06 \x01(\t\x12\x10\n\x08is_valid\x18\x07 \x01(\x08\"w\n.CEmbeddedClient_AuthorizeCurrentDevice_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x13\n\x0b\x64\x65vice_info\x18\x03 \x01(\t\x12\x10\n\x08\x64\x65viceid\x18\x04 \x01(\r\"`\n\x15\x43\x45mbeddedClient_Token\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x14\n\x0c\x63lient_token\x18\x02 \x01(\x0c\x12\x0e\n\x06\x65xpiry\x18\x03 \x01(\r\x12\x10\n\x08\x64\x65viceid\x18\x04 \x01(\r\"a\n(CEmbeddedClient_AuthorizeDevice_Response\x12\x0e\n\x06result\x18\x01 \x01(\r\x12%\n\x05token\x18\x02 \x01(\x0b\x32\x16.CEmbeddedClient_Token*\x8d\x01\n\x14\x45InternalAccountType\x12\x1f\n\x1bk_EInternalSteamAccountType\x10\x01\x12\x17\n\x13k_EInternalClanType\x10\x02\x12\x16\n\x12k_EInternalAppType\x10\x03\x12#\n\x1fk_EInternalBroadcastChannelType\x10\x04*\x86\x02\n\x14\x45\x45xternalAccountType\x12\x13\n\x0fk_EExternalNone\x10\x00\x12\x1b\n\x17k_EExternalSteamAccount\x10\x01\x12\x1c\n\x18k_EExternalGoogleAccount\x10\x02\x12\x1e\n\x1ak_EExternalFacebookAccount\x10\x03\x12\x1d\n\x19k_EExternalTwitterAccount\x10\x04\x12\x1c\n\x18k_EExternalTwitchAccount\x10\x05\x12$\n k_EExternalYouTubeChannelAccount\x10\x06\x12\x1b\n\x17k_EExternalFacebookPage\x10\x07\x32\x9c\n\n\x0bUserAccount\x12\x9c\x01\n#GetAvailableValveDiscountPromotions\x12\x39.CUserAccount_GetAvailableValveDiscountPromotions_Request\x1a:.CUserAccount_GetAvailableValveDiscountPromotions_Response\x12o\n\x16GetClientWalletDetails\x12,.CUserAccount_GetClientWalletDetails_Request\x1a\'.CUserAccount_GetWalletDetails_Response\x12o\n\x14GetAccountLinkStatus\x12*.CUserAccount_GetAccountLinkStatus_Request\x1a+.CUserAccount_GetAccountLinkStatus_Response\x12l\n\x13\x43\x61ncelLicenseForApp\x12).CUserAccount_CancelLicenseForApp_Request\x1a*.CUserAccount_CancelLicenseForApp_Response\x12]\n\x0eGetUserCountry\x12$.CUserAccount_GetUserCountry_Request\x1a%.CUserAccount_GetUserCountry_Response\x12x\n\x17\x43reateFriendInviteToken\x12-.CUserAccount_CreateFriendInviteToken_Request\x1a..CUserAccount_CreateFriendInviteToken_Response\x12r\n\x15GetFriendInviteTokens\x12+.CUserAccount_GetFriendInviteTokens_Request\x1a,.CUserAccount_GetFriendInviteTokens_Response\x12r\n\x15ViewFriendInviteToken\x12+.CUserAccount_ViewFriendInviteToken_Request\x1a,.CUserAccount_ViewFriendInviteToken_Response\x12x\n\x17RedeemFriendInviteToken\x12-.CUserAccount_RedeemFriendInviteToken_Request\x1a..CUserAccount_RedeemFriendInviteToken_Response\x12x\n\x17RevokeFriendInviteToken\x12-.CUserAccount_RevokeFriendInviteToken_Request\x1a..CUserAccount_RevokeFriendInviteToken_Response\x12i\n\x12RegisterCompatTool\x12(.CUserAccount_RegisterCompatTool_Request\x1a).CUserAccount_RegisterCompatTool_Response2\x87\x01\n\x0e\x41\x63\x63ountLinking\x12u\n\x14GetLinkedAccountInfo\x12-.CAccountLinking_GetLinkedAccountInfo_Request\x1a..CAccountLinking_GetLinkedAccountInfo_Response2\x86\x01\n\x0e\x45mbeddedClient\x12t\n\x16\x41uthorizeCurrentDevice\x12/.CEmbeddedClient_AuthorizeCurrentDevice_Request\x1a).CEmbeddedClient_AuthorizeDevice_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_useraccount_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_EINTERNALACCOUNTTYPE']._serialized_start=3717
  _globals['_EINTERNALACCOUNTTYPE']._serialized_end=3858
  _globals['_EEXTERNALACCOUNTTYPE']._serialized_start=3861
  _globals['_EEXTERNALACCOUNTTYPE']._serialized_end=4123
  _globals['_CUSERACCOUNT_GETAVAILABLEVALVEDISCOUNTPROMOTIONS_REQUEST']._serialized_start=95
  _globals['_CUSERACCOUNT_GETAVAILABLEVALVEDISCOUNTPROMOTIONS_REQUEST']._serialized_end=175
  _globals['_CUSERACCOUNT_GETAVAILABLEVALVEDISCOUNTPROMOTIONS_RESPONSE']._serialized_start=178
  _globals['_CUSERACCOUNT_GETAVAILABLEVALVEDISCOUNTPROMOTIONS_RESPONSE']._serialized_end=695
  _globals['_CUSERACCOUNT_GETAVAILABLEVALVEDISCOUNTPROMOTIONS_RESPONSE_VALVEDISCOUNTPROMOTIONDETAILS']._serialized_start=350
  _globals['_CUSERACCOUNT_GETAVAILABLEVALVEDISCOUNTPROMOTIONS_RESPONSE_VALVEDISCOUNTPROMOTIONDETAILS']._serialized_end=695
  _globals['_CUSERACCOUNT_GETCLIENTWALLETDETAILS_REQUEST']._serialized_start=698
  _globals['_CUSERACCOUNT_GETCLIENTWALLETDETAILS_REQUEST']._serialized_end=836
  _globals['_CUSERACCOUNT_GETWALLETDETAILS_RESPONSE']._serialized_start=839
  _globals['_CUSERACCOUNT_GETWALLETDETAILS_RESPONSE']._serialized_end=1404
  _globals['_CUSERACCOUNT_GETACCOUNTLINKSTATUS_REQUEST']._serialized_start=1406
  _globals['_CUSERACCOUNT_GETACCOUNTLINKSTATUS_REQUEST']._serialized_end=1449
  _globals['_CUSERACCOUNT_GETACCOUNTLINKSTATUS_RESPONSE']._serialized_start=1451
  _globals['_CUSERACCOUNT_GETACCOUNTLINKSTATUS_RESPONSE']._serialized_end=1576
  _globals['_CUSERACCOUNT_CANCELLICENSEFORAPP_REQUEST']._serialized_start=1578
  _globals['_CUSERACCOUNT_CANCELLICENSEFORAPP_REQUEST']._serialized_end=1635
  _globals['_CUSERACCOUNT_CANCELLICENSEFORAPP_RESPONSE']._serialized_start=1637
  _globals['_CUSERACCOUNT_CANCELLICENSEFORAPP_RESPONSE']._serialized_end=1680
  _globals['_CUSERACCOUNT_GETUSERCOUNTRY_REQUEST']._serialized_start=1682
  _globals['_CUSERACCOUNT_GETUSERCOUNTRY_REQUEST']._serialized_end=1736
  _globals['_CUSERACCOUNT_GETUSERCOUNTRY_RESPONSE']._serialized_start=1738
  _globals['_CUSERACCOUNT_GETUSERCOUNTRY_RESPONSE']._serialized_end=1793
  _globals['_CUSERACCOUNT_CREATEFRIENDINVITETOKEN_REQUEST']._serialized_start=1795
  _globals['_CUSERACCOUNT_CREATEFRIENDINVITETOKEN_REQUEST']._serialized_end=1909
  _globals['_CUSERACCOUNT_CREATEFRIENDINVITETOKEN_RESPONSE']._serialized_start=1912
  _globals['_CUSERACCOUNT_CREATEFRIENDINVITETOKEN_RESPONSE']._serialized_end=2065
  _globals['_CUSERACCOUNT_GETFRIENDINVITETOKENS_REQUEST']._serialized_start=2067
  _globals['_CUSERACCOUNT_GETFRIENDINVITETOKENS_REQUEST']._serialized_end=2111
  _globals['_CUSERACCOUNT_GETFRIENDINVITETOKENS_RESPONSE']._serialized_start=2113
  _globals['_CUSERACCOUNT_GETFRIENDINVITETOKENS_RESPONSE']._serialized_end=2222
  _globals['_CUSERACCOUNT_VIEWFRIENDINVITETOKEN_REQUEST']._serialized_start=2224
  _globals['_CUSERACCOUNT_VIEWFRIENDINVITETOKEN_REQUEST']._serialized_end=2307
  _globals['_CUSERACCOUNT_VIEWFRIENDINVITETOKEN_RESPONSE']._serialized_start=2309
  _globals['_CUSERACCOUNT_VIEWFRIENDINVITETOKEN_RESPONSE']._serialized_end=2411
  _globals['_CUSERACCOUNT_REDEEMFRIENDINVITETOKEN_REQUEST']._serialized_start=2413
  _globals['_CUSERACCOUNT_REDEEMFRIENDINVITETOKEN_REQUEST']._serialized_end=2498
  _globals['_CUSERACCOUNT_REDEEMFRIENDINVITETOKEN_RESPONSE']._serialized_start=2500
  _globals['_CUSERACCOUNT_REDEEMFRIENDINVITETOKEN_RESPONSE']._serialized_end=2547
  _globals['_CUSERACCOUNT_REVOKEFRIENDINVITETOKEN_REQUEST']._serialized_start=2549
  _globals['_CUSERACCOUNT_REVOKEFRIENDINVITETOKEN_REQUEST']._serialized_end=2617
  _globals['_CUSERACCOUNT_REVOKEFRIENDINVITETOKEN_RESPONSE']._serialized_start=2619
  _globals['_CUSERACCOUNT_REVOKEFRIENDINVITETOKEN_RESPONSE']._serialized_end=2666
  _globals['_CUSERACCOUNT_REGISTERCOMPATTOOL_REQUEST']._serialized_start=2668
  _globals['_CUSERACCOUNT_REGISTERCOMPATTOOL_REQUEST']._serialized_end=2730
  _globals['_CUSERACCOUNT_REGISTERCOMPATTOOL_RESPONSE']._serialized_start=2732
  _globals['_CUSERACCOUNT_REGISTERCOMPATTOOL_RESPONSE']._serialized_end=2774
  _globals['_CACCOUNTLINKING_GETLINKEDACCOUNTINFO_REQUEST']._serialized_start=2777
  _globals['_CACCOUNTLINKING_GETLINKEDACCOUNTINFO_REQUEST']._serialized_end=3002
  _globals['_CACCOUNTLINKING_GETLINKEDACCOUNTINFO_RESPONSE']._serialized_start=3005
  _globals['_CACCOUNTLINKING_GETLINKEDACCOUNTINFO_RESPONSE']._serialized_end=3396
  _globals['_CACCOUNTLINKING_GETLINKEDACCOUNTINFO_RESPONSE_CEXTERNALACCOUNTTUPLE_RESPONSE']._serialized_start=3161
  _globals['_CACCOUNTLINKING_GETLINKEDACCOUNTINFO_RESPONSE_CEXTERNALACCOUNTTUPLE_RESPONSE']._serialized_end=3396
  _globals['_CEMBEDDEDCLIENT_AUTHORIZECURRENTDEVICE_REQUEST']._serialized_start=3398
  _globals['_CEMBEDDEDCLIENT_AUTHORIZECURRENTDEVICE_REQUEST']._serialized_end=3517
  _globals['_CEMBEDDEDCLIENT_TOKEN']._serialized_start=3519
  _globals['_CEMBEDDEDCLIENT_TOKEN']._serialized_end=3615
  _globals['_CEMBEDDEDCLIENT_AUTHORIZEDEVICE_RESPONSE']._serialized_start=3617
  _globals['_CEMBEDDEDCLIENT_AUTHORIZEDEVICE_RESPONSE']._serialized_end=3714
  _globals['_USERACCOUNT']._serialized_start=4126
  _globals['_USERACCOUNT']._serialized_end=5434
  _globals['_ACCOUNTLINKING']._serialized_start=5437
  _globals['_ACCOUNTLINKING']._serialized_end=5572
  _globals['_EMBEDDEDCLIENT']._serialized_start=5575
  _globals['_EMBEDDEDCLIENT']._serialized_end=5709
_builder.BuildServices(DESCRIPTOR, 'steammessages_useraccount_pb2', _globals)
# @@protoc_insertion_point(module_scope)
