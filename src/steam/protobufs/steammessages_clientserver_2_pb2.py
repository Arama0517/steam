# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_clientserver_2.proto
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
    'steammessages_clientserver_2.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"steammessages_clientserver_2.proto\x1a\x18steammessages_base.proto\"w\n\x1c\x43MsgClientUpdateUserGameInfo\x12\x14\n\x0csteamid_idgs\x18\x01 \x01(\x06\x12\x0e\n\x06gameid\x18\x02 \x01(\x06\x12\x0f\n\x07game_ip\x18\x03 \x01(\r\x12\x11\n\tgame_port\x18\x04 \x01(\r\x12\r\n\x05token\x18\x05 \x01(\x0c\"S\n\x1c\x43MsgClientRichPresenceUpload\x12\x18\n\x10rich_presence_kv\x18\x01 \x01(\x0c\x12\x19\n\x11steamid_broadcast\x18\x02 \x03(\x06\"8\n\x1d\x43MsgClientRichPresenceRequest\x12\x17\n\x0fsteamid_request\x18\x01 \x03(\x06\"\x9d\x01\n\x1a\x43MsgClientRichPresenceInfo\x12?\n\rrich_presence\x18\x01 \x03(\x0b\x32(.CMsgClientRichPresenceInfo.RichPresence\x1a>\n\x0cRichPresence\x12\x14\n\x0csteamid_user\x18\x01 \x01(\x06\x12\x18\n\x10rich_presence_kv\x18\x02 \x01(\x0c\".\n\x1c\x43MsgClientCheckFileSignature\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\"\xf7\x01\n$CMsgClientCheckFileSignatureResponse\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x0b\n\x03pid\x18\x02 \x01(\r\x12\x0f\n\x07\x65result\x18\x03 \x01(\r\x12\x10\n\x08\x66ilename\x18\x04 \x01(\t\x12\x18\n\x10\x65signatureresult\x18\x05 \x01(\r\x12\x10\n\x08sha_file\x18\x06 \x01(\x0c\x12\x17\n\x0fsignatureheader\x18\x07 \x01(\x0c\x12\x10\n\x08\x66ilesize\x18\x08 \x01(\r\x12\x14\n\x0cgetlasterror\x18\t \x01(\r\x12\"\n\x1a\x65valvesignaturecheckdetail\x18\n \x01(\r\"P\n\x19\x43MsgClientReadMachineAuth\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x11\n\tcubtoread\x18\x03 \x01(\r\"\xce\x01\n!CMsgClientReadMachineAuthResponse\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0f\n\x07\x65result\x18\x02 \x01(\r\x12\x10\n\x08\x66ilesize\x18\x03 \x01(\r\x12\x10\n\x08sha_file\x18\x04 \x01(\x0c\x12\x14\n\x0cgetlasterror\x18\x05 \x01(\r\x12\x0e\n\x06offset\x18\x06 \x01(\r\x12\x0f\n\x07\x63ubread\x18\x07 \x01(\r\x12\x12\n\nbytes_read\x18\x08 \x01(\x0c\x12\x17\n\x0f\x66ilename_sentry\x18\t \x01(\t\"\xbd\x01\n\x1b\x43MsgClientUpdateMachineAuth\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x12\n\ncubtowrite\x18\x03 \x01(\r\x12\r\n\x05\x62ytes\x18\x04 \x01(\x0c\x12\x10\n\x08otp_type\x18\x05 \x01(\r\x12\x16\n\x0eotp_identifier\x18\x06 \x01(\t\x12\x18\n\x10otp_sharedsecret\x18\x07 \x01(\x0c\x12\x15\n\rotp_timedrift\x18\x08 \x01(\r\"\xe1\x01\n#CMsgClientUpdateMachineAuthResponse\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0f\n\x07\x65result\x18\x02 \x01(\r\x12\x10\n\x08\x66ilesize\x18\x03 \x01(\r\x12\x10\n\x08sha_file\x18\x04 \x01(\x0c\x12\x14\n\x0cgetlasterror\x18\x05 \x01(\r\x12\x0e\n\x06offset\x18\x06 \x01(\r\x12\x10\n\x08\x63ubwrote\x18\x07 \x01(\r\x12\x10\n\x08otp_type\x18\x08 \x01(\x05\x12\x11\n\totp_value\x18\t \x01(\r\x12\x16\n\x0eotp_identifier\x18\n \x01(\t\"$\n\x15\x43MsgClientRegisterKey\x12\x0b\n\x03key\x18\x01 \x01(\t\"p\n\x1a\x43MsgClientPurchaseResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x1f\n\x17purchase_result_details\x18\x02 \x01(\x05\x12\x1d\n\x15purchase_receipt_info\x18\x03 \x01(\x0c\"\xc5\x01\n\x1c\x43MsgClientActivateOEMLicense\x12\x19\n\x11\x62ios_manufacturer\x18\x01 \x01(\t\x12\x19\n\x11\x62ios_serialnumber\x18\x02 \x01(\t\x12\x14\n\x0clicense_file\x18\x03 \x01(\x0c\x12\x1e\n\x16mainboard_manufacturer\x18\x04 \x01(\t\x12\x19\n\x11mainboard_product\x18\x05 \x01(\t\x12\x1e\n\x16mainboard_serialnumber\x18\x06 \x01(\t\"9\n\x1c\x43MsgClientRegisterOEMMachine\x12\x19\n\x11oem_register_file\x18\x01 \x01(\x0c\"7\n$CMsgClientRegisterOEMMachineResponse\x12\x0f\n\x07\x65result\x18\x01 \x01(\r\"K\n\x1f\x43MsgClientPurchaseWithMachineID\x12\x12\n\npackage_id\x18\x01 \x01(\r\x12\x14\n\x0cmachine_info\x18\x02 \x01(\x0c\"g\n CMsgTrading_InitiateTradeRequest\x12\x18\n\x10trade_request_id\x18\x01 \x01(\r\x12\x15\n\rother_steamid\x18\x02 \x01(\x04\x12\x12\n\nother_name\x18\x03 \x01(\t\"\xd2\x02\n!CMsgTrading_InitiateTradeResponse\x12\x10\n\x08response\x18\x01 \x01(\r\x12\x18\n\x10trade_request_id\x18\x02 \x01(\r\x12\x15\n\rother_steamid\x18\x03 \x01(\x04\x12 \n\x18steamguard_required_days\x18\x04 \x01(\r\x12 \n\x18new_device_cooldown_days\x18\x05 \x01(\r\x12-\n%default_password_reset_probation_days\x18\x06 \x01(\r\x12%\n\x1dpassword_reset_probation_days\x18\x07 \x01(\r\x12+\n#default_email_change_probation_days\x18\x08 \x01(\r\x12#\n\x1b\x65mail_change_probation_days\x18\t \x01(\r\"7\n\x1e\x43MsgTrading_CancelTradeRequest\x12\x15\n\rother_steamid\x18\x01 \x01(\x04\"1\n\x18\x43MsgTrading_StartSession\x12\x15\n\rother_steamid\x18\x01 \x01(\x04\"C\n\x1f\x43MsgClientGetDepotDecryptionKey\x12\x10\n\x08\x64\x65pot_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\"m\n\'CMsgClientGetDepotDecryptionKeyResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x10\n\x08\x64\x65pot_id\x18\x02 \x01(\r\x12\x1c\n\x14\x64\x65pot_encryption_key\x18\x03 \x01(\x0c\"X\n\x1e\x43MsgClientCheckAppBetaPassword\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x14\n\x0c\x62\x65tapassword\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\x05\"\xda\x01\n&CMsgClientCheckAppBetaPasswordResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12K\n\rbetapasswords\x18\x04 \x03(\x0b\x32\x34.CMsgClientCheckAppBetaPasswordResponse.BetaPassword\x1aO\n\x0c\x42\x65taPassword\x12\x10\n\x08\x62\x65taname\x18\x01 \x01(\t\x12\x14\n\x0c\x62\x65tapassword\x18\x02 \x01(\t\x12\x17\n\x0f\x62\x65tadescription\x18\x03 \x01(\t\"\x99\x01\n\x1b\x43MsgClientUGSGetGlobalStats\x12\x0e\n\x06gameid\x18\x01 \x01(\x04\x12\x1e\n\x16history_days_requested\x18\x02 \x01(\r\x12\x1b\n\x13time_last_requested\x18\x03 \x01(\x07\x12\x18\n\x10\x66irst_day_cached\x18\x04 \x01(\r\x12\x13\n\x0b\x64\x61ys_cached\x18\x05 \x01(\r\"\x95\x02\n#CMsgClientUGSGetGlobalStatsResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x11\n\ttimestamp\x18\x02 \x01(\x07\x12\x13\n\x0b\x64\x61y_current\x18\x03 \x01(\x05\x12\x36\n\x04\x64\x61ys\x18\x04 \x03(\x0b\x32(.CMsgClientUGSGetGlobalStatsResponse.Day\x1az\n\x03\x44\x61y\x12\x0e\n\x06\x64\x61y_id\x18\x01 \x01(\r\x12<\n\x05stats\x18\x02 \x03(\x0b\x32-.CMsgClientUGSGetGlobalStatsResponse.Day.Stat\x1a%\n\x04Stat\x12\x0f\n\x07stat_id\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x03\"2\n\x19\x43MsgClientRedeemGuestPass\x12\x15\n\rguest_pass_id\x18\x01 \x01(\x06\"c\n!CMsgClientRedeemGuestPassResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\r:\x01\x32\x12\x12\n\npackage_id\x18\x02 \x01(\r\x12\x16\n\x0emust_own_appid\x18\x03 \x01(\r\"8\n\x1f\x43MsgClientGetClanActivityCounts\x12\x15\n\rsteamid_clans\x18\x01 \x03(\x04\"=\n\'CMsgClientGetClanActivityCountsResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\r:\x01\x32\"y\n\x19\x43MsgClientOGSReportString\x12\x13\n\x0b\x61\x63\x63umulated\x18\x01 \x01(\x08\x12\x11\n\tsessionid\x18\x02 \x01(\x04\x12\x10\n\x08severity\x18\x03 \x01(\x05\x12\x11\n\tformatter\x18\x04 \x01(\t\x12\x0f\n\x07varargs\x18\x05 \x01(\x0c\"P\n\x16\x43MsgClientOGSReportBug\x12\x11\n\tsessionid\x18\x01 \x01(\x04\x12\x0f\n\x07\x62ugtext\x18\x02 \x01(\t\x12\x12\n\nscreenshot\x18\x03 \x01(\x0c\"\x14\n\x12\x43MsgClientSentLogs\"l\n\x0c\x43MsgGCClient\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07msgtype\x18\x02 \x01(\r\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x0f\n\x07steamid\x18\x04 \x01(\x06\x12\x0e\n\x06gcname\x18\x05 \x01(\t\x12\n\n\x02ip\x18\x06 \x01(\r\".\n\x1c\x43MsgClientRequestFreeLicense\x12\x0e\n\x06\x61ppids\x18\x02 \x03(\r\"n\n$CMsgClientRequestFreeLicenseResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\r:\x01\x32\x12\x1a\n\x12granted_packageids\x18\x02 \x03(\r\x12\x16\n\x0egranted_appids\x18\x03 \x03(\r\"\xd3\x01\n#CMsgDRMDownloadRequestWithCrashData\x12\x16\n\x0e\x64ownload_flags\x18\x01 \x01(\r\x12\x1c\n\x14\x64ownload_types_known\x18\x02 \x01(\r\x12\x10\n\x08guid_drm\x18\x03 \x01(\x0c\x12\x12\n\nguid_split\x18\x04 \x01(\x0c\x12\x12\n\nguid_merge\x18\x05 \x01(\x0c\x12\x13\n\x0bmodule_name\x18\x06 \x01(\t\x12\x13\n\x0bmodule_path\x18\x07 \x01(\t\x12\x12\n\ncrash_data\x18\x08 \x01(\x0c\"\xdb\x01\n\x17\x43MsgDRMDownloadResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\r:\x01\x32\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12\x1a\n\x12\x62lob_download_type\x18\x03 \x01(\r\x12\x12\n\nmerge_guid\x18\x04 \x01(\x0c\x12\x1c\n\x14\x64ownload_file_dfs_ip\x18\x05 \x01(\r\x12\x1e\n\x16\x64ownload_file_dfs_port\x18\x06 \x01(\r\x12\x19\n\x11\x64ownload_file_url\x18\x07 \x01(\t\x12\x13\n\x0bmodule_path\x18\x08 \x01(\t\"\xd7\x01\n\x12\x43MsgDRMFinalResult\x12\x12\n\x07\x65Result\x18\x01 \x01(\r:\x01\x32\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12\x1a\n\x12\x62lob_download_type\x18\x03 \x01(\r\x12\x14\n\x0c\x65rror_detail\x18\x04 \x01(\r\x12\x12\n\nmerge_guid\x18\x05 \x01(\x0c\x12\x1c\n\x14\x64ownload_file_dfs_ip\x18\x06 \x01(\r\x12\x1e\n\x16\x64ownload_file_dfs_port\x18\x07 \x01(\r\x12\x19\n\x11\x64ownload_file_url\x18\x08 \x01(\t\"3\n\x1e\x43MsgClientDPCheckSpecialSurvey\x12\x11\n\tsurvey_id\x18\x01 \x01(\r\"\x96\x01\n&CMsgClientDPCheckSpecialSurveyResponse\x12\x12\n\x07\x65Result\x18\x01 \x01(\r:\x01\x32\x12\r\n\x05state\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\ncustom_url\x18\x04 \x01(\t\x12\x18\n\x10include_software\x18\x05 \x01(\x08\x12\r\n\x05token\x18\x06 \x01(\x0c\"H\n%CMsgClientDPSendSpecialSurveyResponse\x12\x11\n\tsurvey_id\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"O\n*CMsgClientDPSendSpecialSurveyResponseReply\x12\x12\n\x07\x65Result\x18\x01 \x01(\r:\x01\x32\x12\r\n\x05token\x18\x02 \x01(\x0c\"W\n\'CMsgClientRequestForgottenPasswordEmail\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\t\x12\x16\n\x0epassword_tried\x18\x02 \x01(\t\"_\n/CMsgClientRequestForgottenPasswordEmailResponse\x12\x0f\n\x07\x65Result\x18\x01 \x01(\r\x12\x1b\n\x13use_secret_question\x18\x02 \x01(\x08\"\xf6\x01\n\x1b\x43MsgClientItemAnnouncements\x12\x17\n\x0f\x63ount_new_items\x18\x01 \x01(\r\x12=\n\x0cunseen_items\x18\x02 \x03(\x0b\x32\'.CMsgClientItemAnnouncements.UnseenItem\x1a\x7f\n\nUnseenItem\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x12\n\ncontext_id\x18\x02 \x01(\x04\x12\x10\n\x08\x61sset_id\x18\x03 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x16\n\x0ertime32_gained\x18\x05 \x01(\x07\x12\x14\n\x0csource_appid\x18\x06 \x01(\r\"$\n\"CMsgClientRequestItemAnnouncements\"\x9e\x01\n\x1b\x43MsgClientUserNotifications\x12@\n\rnotifications\x18\x01 \x03(\x0b\x32).CMsgClientUserNotifications.Notification\x1a=\n\x0cNotification\x12\x1e\n\x16user_notification_type\x18\x01 \x01(\r\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"\x88\x01\n\x1e\x43MsgClientCommentNotifications\x12\x1a\n\x12\x63ount_new_comments\x18\x01 \x01(\r\x12 \n\x18\x63ount_new_comments_owner\x18\x02 \x01(\r\x12(\n count_new_comments_subscriptions\x18\x03 \x01(\r\"\'\n%CMsgClientRequestCommentNotifications\"g\n$CMsgClientOfflineMessageNotification\x12\x18\n\x10offline_messages\x18\x01 \x01(\r\x12%\n\x1d\x66riends_with_offline_messages\x18\x02 \x03(\r\"&\n$CMsgClientRequestOfflineMessageCount\"8\n%CMsgClientChatGetFriendMessageHistory\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"\xf9\x01\n-CMsgClientChatGetFriendMessageHistoryResponse\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x0f\n\x07success\x18\x02 \x01(\r\x12N\n\x08messages\x18\x03 \x03(\x0b\x32<.CMsgClientChatGetFriendMessageHistoryResponse.FriendMessage\x1aV\n\rFriendMessage\x12\x11\n\taccountid\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0e\n\x06unread\x18\x04 \x01(\x08\"9\n7CMsgClientChatGetFriendMessageHistoryForOfflineMessages\"7\n!CMsgClientFSGetFriendsSteamLevels\x12\x12\n\naccountids\x18\x01 \x03(\r\"\x9b\x01\n)CMsgClientFSGetFriendsSteamLevelsResponse\x12\x42\n\x07\x66riends\x18\x01 \x03(\x0b\x32\x31.CMsgClientFSGetFriendsSteamLevelsResponse.Friend\x1a*\n\x06\x46riend\x12\x11\n\taccountid\x18\x01 \x01(\r\x12\r\n\x05level\x18\x02 \x01(\r\"\xca\x01\n\x17\x43MsgClientEmailAddrInfo\x12\x15\n\remail_address\x18\x01 \x01(\t\x12\x1a\n\x12\x65mail_is_validated\x18\x02 \x01(\x08\x12 \n\x18\x65mail_validation_changed\x18\x03 \x01(\x08\x12\'\n\x1f\x63redential_change_requires_code\x18\x04 \x01(\x08\x12\x31\n)password_or_secretqa_change_requires_code\x18\x05 \x01(\x08\"\x8b\x01\n\x16\x43MsgCREItemVoteSummary\x12\x43\n\x12published_file_ids\x18\x01 \x03(\x0b\x32\'.CMsgCREItemVoteSummary.PublishedFileId\x1a,\n\x0fPublishedFileId\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\"\xfa\x01\n\x1e\x43MsgCREItemVoteSummaryResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12L\n\x13item_vote_summaries\x18\x02 \x03(\x0b\x32/.CMsgCREItemVoteSummaryResponse.ItemVoteSummary\x1av\n\x0fItemVoteSummary\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\x12\x11\n\tvotes_for\x18\x02 \x01(\x05\x12\x15\n\rvotes_against\x18\x03 \x01(\x05\x12\x0f\n\x07reports\x18\x04 \x01(\x05\x12\r\n\x05score\x18\x05 \x01(\x02\"P\n\"CMsgCREUpdateUserPublishedItemVote\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\x12\x0f\n\x07vote_up\x18\x02 \x01(\x08\"@\n*CMsgCREUpdateUserPublishedItemVoteResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\"\xab\x01\n&CMsgCREGetUserPublishedItemVoteDetails\x12S\n\x12published_file_ids\x18\x01 \x03(\x0b\x32\x37.CMsgCREGetUserPublishedItemVoteDetails.PublishedFileId\x1a,\n\x0fPublishedFileId\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\"\xea\x01\n.CMsgCREGetUserPublishedItemVoteDetailsResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x62\n\x16user_item_vote_details\x18\x02 \x03(\x0b\x32\x42.CMsgCREGetUserPublishedItemVoteDetailsResponse.UserItemVoteDetail\x1a@\n\x12UserItemVoteDetail\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\x12\x0f\n\x04vote\x18\x02 \x01(\x05:\x01\x30\"*\n\x16\x43MsgFSGetFollowerCount\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\"F\n\x1e\x43MsgFSGetFollowerCountResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x10\n\x05\x63ount\x18\x02 \x01(\x05:\x01\x30\"(\n\x14\x43MsgFSGetIsFollowing\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\"O\n\x1c\x43MsgFSGetIsFollowingResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x1b\n\x0cis_following\x18\x02 \x01(\x08:\x05\x66\x61lse\"3\n\x1c\x43MsgFSEnumerateFollowingList\x12\x13\n\x0bstart_index\x18\x01 \x01(\r\"d\n$CMsgFSEnumerateFollowingListResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x15\n\rtotal_results\x18\x02 \x01(\x05\x12\x11\n\tsteam_ids\x18\x03 \x03(\x06\"0\n\x1f\x43MsgDPGetNumberOfCurrentPlayers\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"S\n\'CMsgDPGetNumberOfCurrentPlayersResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x14\n\x0cplayer_count\x18\x02 \x01(\x05\"a\n#CMsgClientFriendUserStatusPublished\x12\x16\n\x0e\x66riend_steamid\x18\x01 \x01(\x06\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x13\n\x0bstatus_text\x18\x03 \x01(\t\"h\n\x1d\x43MsgClientServiceMethodLegacy\x12\x13\n\x0bmethod_name\x18\x01 \x01(\t\x12\x19\n\x11serialized_method\x18\x02 \x01(\x0c\x12\x17\n\x0fis_notification\x18\x03 \x01(\x08\"`\n%CMsgClientServiceMethodLegacyResponse\x12\x13\n\x0bmethod_name\x18\x01 \x01(\t\x12\"\n\x1aserialized_method_response\x18\x02 \x01(\x0c\"5\n\x10\x43MsgClientUIMode\x12\x0e\n\x06uimode\x18\x01 \x01(\r\x12\x11\n\tchat_mode\x18\x02 \x01(\r\"<\n&CMsgClientVanityURLChangedNotification\x12\x12\n\nvanity_url\x18\x01 \x01(\t\"y\n%CMsgClientAuthorizeLocalDeviceRequest\x12\x1a\n\x12\x64\x65vice_description\x18\x01 \x01(\t\x12\x18\n\x10owner_account_id\x18\x02 \x01(\r\x12\x1a\n\x12local_device_token\x18\x03 \x01(\x04\"k\n\x1e\x43MsgClientAuthorizeLocalDevice\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x18\n\x10owner_account_id\x18\x02 \x01(\r\x12\x1b\n\x13\x61uthed_device_token\x18\x03 \x01(\x04\"v\n*CMsgClientAuthorizeLocalDeviceNotification\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x18\n\x10owner_account_id\x18\x02 \x01(\r\x12\x1a\n\x12local_device_token\x18\x03 \x01(\x04\"n\n\"CMsgClientDeauthorizeDeviceRequest\x12\"\n\x1a\x64\x65\x61uthorization_account_id\x18\x01 \x01(\r\x12$\n\x1c\x64\x65\x61uthorization_device_token\x18\x02 \x01(\x04\"U\n\x1b\x43MsgClientDeauthorizeDevice\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\"\n\x1a\x64\x65\x61uthorization_account_id\x18\x02 \x01(\r\"\xd1\x01\n&CMsgClientUseLocalDeviceAuthorizations\x12 \n\x18\x61uthorization_account_id\x18\x01 \x03(\r\x12J\n\rdevice_tokens\x18\x02 \x03(\x0b\x32\x33.CMsgClientUseLocalDeviceAuthorizations.DeviceToken\x1a\x39\n\x0b\x44\x65viceToken\x12\x18\n\x10owner_account_id\x18\x01 \x01(\r\x12\x10\n\x08token_id\x18\x02 \x01(\x04\" \n\x1e\x43MsgClientGetAuthorizedDevices\"\xad\x02\n&CMsgClientGetAuthorizedDevicesResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12S\n\x11\x61uthorized_device\x18\x02 \x03(\x0b\x32\x38.CMsgClientGetAuthorizedDevicesResponse.AuthorizedDevice\x1a\x99\x01\n\x10\x41uthorizedDevice\x12\x19\n\x11\x61uth_device_token\x18\x01 \x01(\x04\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x18\n\x10last_access_time\x18\x03 \x01(\r\x12\x13\n\x0b\x62orrower_id\x18\x04 \x01(\r\x12\x12\n\nis_pending\x18\x05 \x01(\x08\x12\x12\n\napp_played\x18\x06 \x01(\r\"\xc2\x01\n!CMsgClientSharedLibraryLockStatus\x12H\n\x0elocked_library\x18\x01 \x03(\x0b\x32\x30.CMsgClientSharedLibraryLockStatus.LockedLibrary\x12\x1d\n\x15own_library_locked_by\x18\x02 \x01(\r\x1a\x34\n\rLockedLibrary\x12\x10\n\x08owner_id\x18\x01 \x01(\r\x12\x11\n\tlocked_by\x18\x02 \x01(\r\"\xa7\x01\n\"CMsgClientSharedLibraryStopPlaying\x12\x14\n\x0cseconds_left\x18\x01 \x01(\x05\x12>\n\tstop_apps\x18\x02 \x03(\x0b\x32+.CMsgClientSharedLibraryStopPlaying.StopApp\x1a+\n\x07StopApp\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x10\n\x08owner_id\x18\x02 \x01(\r\"\x81\x02\n\x15\x43MsgClientServiceCall\x12\x15\n\rsysid_routing\x18\x01 \x01(\x0c\x12\x13\n\x0b\x63\x61ll_handle\x18\x02 \x01(\r\x12\x12\n\nmodule_crc\x18\x03 \x01(\r\x12\x13\n\x0bmodule_hash\x18\x04 \x01(\x0c\x12\x13\n\x0b\x66unction_id\x18\x05 \x01(\r\x12\x16\n\x0e\x63ub_output_max\x18\x06 \x01(\r\x12\r\n\x05\x66lags\x18\x07 \x01(\r\x12\x15\n\rcallparameter\x18\x08 \x01(\x0c\x12\x11\n\tping_only\x18\t \x01(\x08\x12\x1d\n\x15max_outstanding_calls\x18\n \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x0b \x01(\r\"Z\n\x17\x43MsgClientServiceModule\x12\x12\n\nmodule_crc\x18\x01 \x01(\r\x12\x13\n\x0bmodule_hash\x18\x02 \x01(\x0c\x12\x16\n\x0emodule_content\x18\x03 \x01(\x0c\"\xb8\x04\n\x1d\x43MsgClientServiceCallResponse\x12\x15\n\rsysid_routing\x18\x01 \x01(\x0c\x12\x13\n\x0b\x63\x61ll_handle\x18\x02 \x01(\r\x12\x12\n\nmodule_crc\x18\x03 \x01(\r\x12\x13\n\x0bmodule_hash\x18\x04 \x01(\x0c\x12\x13\n\x0b\x65\x63\x61llresult\x18\x05 \x01(\r\x12\x16\n\x0eresult_content\x18\x06 \x01(\x0c\x12\x17\n\x0fos_version_info\x18\x07 \x01(\x0c\x12\x13\n\x0bsystem_info\x18\x08 \x01(\x0c\x12\x14\n\x0cload_address\x18\t \x01(\x06\x12\x18\n\x10\x65xception_record\x18\n \x01(\x0c\x12 \n\x18portable_os_version_info\x18\x0b \x01(\x0c\x12\x1c\n\x14portable_system_info\x18\x0c \x01(\x0c\x12\x15\n\rwas_converted\x18\r \x01(\x08\x12\x17\n\x0finternal_result\x18\x0e \x01(\r\x12\x15\n\rcurrent_count\x18\x0f \x01(\r\x12\x18\n\x10last_call_handle\x18\x10 \x01(\r\x12\x1c\n\x14last_call_module_crc\x18\x11 \x01(\r\x12\x1f\n\x17last_call_sysid_routing\x18\x12 \x01(\x0c\x12\x18\n\x10last_ecallresult\x18\x13 \x01(\r\x12\x1c\n\x14last_callissue_delta\x18\x14 \x01(\r\x12\x1f\n\x17last_callcomplete_delta\x18\x15 \x01(\r\"C\n\x10\x43MsgAMUnlockH264\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x10\n\x08platform\x18\x02 \x01(\x05\x12\x0e\n\x06reason\x18\x03 \x01(\x05\"F\n\x18\x43MsgAMUnlockH264Response\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x16\n\x0e\x65ncryption_key\x18\x02 \x01(\x0c\"M\n\x1d\x43MsgClientPlayingSessionState\x12\x17\n\x0fplaying_blocked\x18\x02 \x01(\x08\x12\x13\n\x0bplaying_app\x18\x03 \x01(\r\"6\n\x1c\x43MsgClientKickPlayingSession\x12\x16\n\x0eonly_stop_game\x18\x01 \x01(\x08\"v\n\x1f\x43MsgClientVoiceCallPreAuthorize\x12\x16\n\x0e\x63\x61ller_steamid\x18\x01 \x01(\x06\x12\x18\n\x10receiver_steamid\x18\x02 \x01(\x06\x12\x11\n\tcaller_id\x18\x03 \x01(\x05\x12\x0e\n\x06hangup\x18\x04 \x01(\x08\"\x82\x01\n\'CMsgClientVoiceCallPreAuthorizeResponse\x12\x16\n\x0e\x63\x61ller_steamid\x18\x01 \x01(\x06\x12\x18\n\x10receiver_steamid\x18\x02 \x01(\x06\x12\x12\n\x07\x65result\x18\x03 \x01(\x05:\x01\x32\x12\x11\n\tcaller_id\x18\x04 \x01(\x05\"B\n\x1c\x43MsgBadgeCraftedNotification\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x13\n\x0b\x62\x61\x64ge_level\x18\x02 \x01(\r\"w\n CMsgClientStartPeerContentServer\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10\x63lient_remote_id\x18\x02 \x01(\x06\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\r\x12\x18\n\x10\x63urrent_build_id\x18\x04 \x01(\r\"\x7f\n(CMsgClientStartPeerContentServerResponse\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x13\n\x0bserver_port\x18\x02 \x01(\r\x12\x18\n\x10installed_depots\x18\x03 \x03(\r\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\x04\"f\n\x1c\x43MsgClientGetPeerContentInfo\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10\x63lient_remote_id\x18\x02 \x01(\x06\x12\x1b\n\x13owned_games_visible\x18\x03 \x01(\x08\"D\n$CMsgClientGetPeerContentInfoResponse\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x0c\n\x04\x61pps\x18\x02 \x03(\r\"-\n\x1b\x43MsgClientPendingGameLaunch\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\"Y\n#CMsgClientPendingGameLaunchResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12\x0e\n\x06\x65nvkey\x18\x03 \x01(\tB\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_clientserver_2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_CMSGCLIENTUPDATEUSERGAMEINFO']._serialized_start=64
  _globals['_CMSGCLIENTUPDATEUSERGAMEINFO']._serialized_end=183
  _globals['_CMSGCLIENTRICHPRESENCEUPLOAD']._serialized_start=185
  _globals['_CMSGCLIENTRICHPRESENCEUPLOAD']._serialized_end=268
  _globals['_CMSGCLIENTRICHPRESENCEREQUEST']._serialized_start=270
  _globals['_CMSGCLIENTRICHPRESENCEREQUEST']._serialized_end=326
  _globals['_CMSGCLIENTRICHPRESENCEINFO']._serialized_start=329
  _globals['_CMSGCLIENTRICHPRESENCEINFO']._serialized_end=486
  _globals['_CMSGCLIENTRICHPRESENCEINFO_RICHPRESENCE']._serialized_start=424
  _globals['_CMSGCLIENTRICHPRESENCEINFO_RICHPRESENCE']._serialized_end=486
  _globals['_CMSGCLIENTCHECKFILESIGNATURE']._serialized_start=488
  _globals['_CMSGCLIENTCHECKFILESIGNATURE']._serialized_end=534
  _globals['_CMSGCLIENTCHECKFILESIGNATURERESPONSE']._serialized_start=537
  _globals['_CMSGCLIENTCHECKFILESIGNATURERESPONSE']._serialized_end=784
  _globals['_CMSGCLIENTREADMACHINEAUTH']._serialized_start=786
  _globals['_CMSGCLIENTREADMACHINEAUTH']._serialized_end=866
  _globals['_CMSGCLIENTREADMACHINEAUTHRESPONSE']._serialized_start=869
  _globals['_CMSGCLIENTREADMACHINEAUTHRESPONSE']._serialized_end=1075
  _globals['_CMSGCLIENTUPDATEMACHINEAUTH']._serialized_start=1078
  _globals['_CMSGCLIENTUPDATEMACHINEAUTH']._serialized_end=1267
  _globals['_CMSGCLIENTUPDATEMACHINEAUTHRESPONSE']._serialized_start=1270
  _globals['_CMSGCLIENTUPDATEMACHINEAUTHRESPONSE']._serialized_end=1495
  _globals['_CMSGCLIENTREGISTERKEY']._serialized_start=1497
  _globals['_CMSGCLIENTREGISTERKEY']._serialized_end=1533
  _globals['_CMSGCLIENTPURCHASERESPONSE']._serialized_start=1535
  _globals['_CMSGCLIENTPURCHASERESPONSE']._serialized_end=1647
  _globals['_CMSGCLIENTACTIVATEOEMLICENSE']._serialized_start=1650
  _globals['_CMSGCLIENTACTIVATEOEMLICENSE']._serialized_end=1847
  _globals['_CMSGCLIENTREGISTEROEMMACHINE']._serialized_start=1849
  _globals['_CMSGCLIENTREGISTEROEMMACHINE']._serialized_end=1906
  _globals['_CMSGCLIENTREGISTEROEMMACHINERESPONSE']._serialized_start=1908
  _globals['_CMSGCLIENTREGISTEROEMMACHINERESPONSE']._serialized_end=1963
  _globals['_CMSGCLIENTPURCHASEWITHMACHINEID']._serialized_start=1965
  _globals['_CMSGCLIENTPURCHASEWITHMACHINEID']._serialized_end=2040
  _globals['_CMSGTRADING_INITIATETRADEREQUEST']._serialized_start=2042
  _globals['_CMSGTRADING_INITIATETRADEREQUEST']._serialized_end=2145
  _globals['_CMSGTRADING_INITIATETRADERESPONSE']._serialized_start=2148
  _globals['_CMSGTRADING_INITIATETRADERESPONSE']._serialized_end=2486
  _globals['_CMSGTRADING_CANCELTRADEREQUEST']._serialized_start=2488
  _globals['_CMSGTRADING_CANCELTRADEREQUEST']._serialized_end=2543
  _globals['_CMSGTRADING_STARTSESSION']._serialized_start=2545
  _globals['_CMSGTRADING_STARTSESSION']._serialized_end=2594
  _globals['_CMSGCLIENTGETDEPOTDECRYPTIONKEY']._serialized_start=2596
  _globals['_CMSGCLIENTGETDEPOTDECRYPTIONKEY']._serialized_end=2663
  _globals['_CMSGCLIENTGETDEPOTDECRYPTIONKEYRESPONSE']._serialized_start=2665
  _globals['_CMSGCLIENTGETDEPOTDECRYPTIONKEYRESPONSE']._serialized_end=2774
  _globals['_CMSGCLIENTCHECKAPPBETAPASSWORD']._serialized_start=2776
  _globals['_CMSGCLIENTCHECKAPPBETAPASSWORD']._serialized_end=2864
  _globals['_CMSGCLIENTCHECKAPPBETAPASSWORDRESPONSE']._serialized_start=2867
  _globals['_CMSGCLIENTCHECKAPPBETAPASSWORDRESPONSE']._serialized_end=3085
  _globals['_CMSGCLIENTCHECKAPPBETAPASSWORDRESPONSE_BETAPASSWORD']._serialized_start=3006
  _globals['_CMSGCLIENTCHECKAPPBETAPASSWORDRESPONSE_BETAPASSWORD']._serialized_end=3085
  _globals['_CMSGCLIENTUGSGETGLOBALSTATS']._serialized_start=3088
  _globals['_CMSGCLIENTUGSGETGLOBALSTATS']._serialized_end=3241
  _globals['_CMSGCLIENTUGSGETGLOBALSTATSRESPONSE']._serialized_start=3244
  _globals['_CMSGCLIENTUGSGETGLOBALSTATSRESPONSE']._serialized_end=3521
  _globals['_CMSGCLIENTUGSGETGLOBALSTATSRESPONSE_DAY']._serialized_start=3399
  _globals['_CMSGCLIENTUGSGETGLOBALSTATSRESPONSE_DAY']._serialized_end=3521
  _globals['_CMSGCLIENTUGSGETGLOBALSTATSRESPONSE_DAY_STAT']._serialized_start=3484
  _globals['_CMSGCLIENTUGSGETGLOBALSTATSRESPONSE_DAY_STAT']._serialized_end=3521
  _globals['_CMSGCLIENTREDEEMGUESTPASS']._serialized_start=3523
  _globals['_CMSGCLIENTREDEEMGUESTPASS']._serialized_end=3573
  _globals['_CMSGCLIENTREDEEMGUESTPASSRESPONSE']._serialized_start=3575
  _globals['_CMSGCLIENTREDEEMGUESTPASSRESPONSE']._serialized_end=3674
  _globals['_CMSGCLIENTGETCLANACTIVITYCOUNTS']._serialized_start=3676
  _globals['_CMSGCLIENTGETCLANACTIVITYCOUNTS']._serialized_end=3732
  _globals['_CMSGCLIENTGETCLANACTIVITYCOUNTSRESPONSE']._serialized_start=3734
  _globals['_CMSGCLIENTGETCLANACTIVITYCOUNTSRESPONSE']._serialized_end=3795
  _globals['_CMSGCLIENTOGSREPORTSTRING']._serialized_start=3797
  _globals['_CMSGCLIENTOGSREPORTSTRING']._serialized_end=3918
  _globals['_CMSGCLIENTOGSREPORTBUG']._serialized_start=3920
  _globals['_CMSGCLIENTOGSREPORTBUG']._serialized_end=4000
  _globals['_CMSGCLIENTSENTLOGS']._serialized_start=4002
  _globals['_CMSGCLIENTSENTLOGS']._serialized_end=4022
  _globals['_CMSGGCCLIENT']._serialized_start=4024
  _globals['_CMSGGCCLIENT']._serialized_end=4132
  _globals['_CMSGCLIENTREQUESTFREELICENSE']._serialized_start=4134
  _globals['_CMSGCLIENTREQUESTFREELICENSE']._serialized_end=4180
  _globals['_CMSGCLIENTREQUESTFREELICENSERESPONSE']._serialized_start=4182
  _globals['_CMSGCLIENTREQUESTFREELICENSERESPONSE']._serialized_end=4292
  _globals['_CMSGDRMDOWNLOADREQUESTWITHCRASHDATA']._serialized_start=4295
  _globals['_CMSGDRMDOWNLOADREQUESTWITHCRASHDATA']._serialized_end=4506
  _globals['_CMSGDRMDOWNLOADRESPONSE']._serialized_start=4509
  _globals['_CMSGDRMDOWNLOADRESPONSE']._serialized_end=4728
  _globals['_CMSGDRMFINALRESULT']._serialized_start=4731
  _globals['_CMSGDRMFINALRESULT']._serialized_end=4946
  _globals['_CMSGCLIENTDPCHECKSPECIALSURVEY']._serialized_start=4948
  _globals['_CMSGCLIENTDPCHECKSPECIALSURVEY']._serialized_end=4999
  _globals['_CMSGCLIENTDPCHECKSPECIALSURVEYRESPONSE']._serialized_start=5002
  _globals['_CMSGCLIENTDPCHECKSPECIALSURVEYRESPONSE']._serialized_end=5152
  _globals['_CMSGCLIENTDPSENDSPECIALSURVEYRESPONSE']._serialized_start=5154
  _globals['_CMSGCLIENTDPSENDSPECIALSURVEYRESPONSE']._serialized_end=5226
  _globals['_CMSGCLIENTDPSENDSPECIALSURVEYRESPONSEREPLY']._serialized_start=5228
  _globals['_CMSGCLIENTDPSENDSPECIALSURVEYRESPONSEREPLY']._serialized_end=5307
  _globals['_CMSGCLIENTREQUESTFORGOTTENPASSWORDEMAIL']._serialized_start=5309
  _globals['_CMSGCLIENTREQUESTFORGOTTENPASSWORDEMAIL']._serialized_end=5396
  _globals['_CMSGCLIENTREQUESTFORGOTTENPASSWORDEMAILRESPONSE']._serialized_start=5398
  _globals['_CMSGCLIENTREQUESTFORGOTTENPASSWORDEMAILRESPONSE']._serialized_end=5493
  _globals['_CMSGCLIENTITEMANNOUNCEMENTS']._serialized_start=5496
  _globals['_CMSGCLIENTITEMANNOUNCEMENTS']._serialized_end=5742
  _globals['_CMSGCLIENTITEMANNOUNCEMENTS_UNSEENITEM']._serialized_start=5615
  _globals['_CMSGCLIENTITEMANNOUNCEMENTS_UNSEENITEM']._serialized_end=5742
  _globals['_CMSGCLIENTREQUESTITEMANNOUNCEMENTS']._serialized_start=5744
  _globals['_CMSGCLIENTREQUESTITEMANNOUNCEMENTS']._serialized_end=5780
  _globals['_CMSGCLIENTUSERNOTIFICATIONS']._serialized_start=5783
  _globals['_CMSGCLIENTUSERNOTIFICATIONS']._serialized_end=5941
  _globals['_CMSGCLIENTUSERNOTIFICATIONS_NOTIFICATION']._serialized_start=5880
  _globals['_CMSGCLIENTUSERNOTIFICATIONS_NOTIFICATION']._serialized_end=5941
  _globals['_CMSGCLIENTCOMMENTNOTIFICATIONS']._serialized_start=5944
  _globals['_CMSGCLIENTCOMMENTNOTIFICATIONS']._serialized_end=6080
  _globals['_CMSGCLIENTREQUESTCOMMENTNOTIFICATIONS']._serialized_start=6082
  _globals['_CMSGCLIENTREQUESTCOMMENTNOTIFICATIONS']._serialized_end=6121
  _globals['_CMSGCLIENTOFFLINEMESSAGENOTIFICATION']._serialized_start=6123
  _globals['_CMSGCLIENTOFFLINEMESSAGENOTIFICATION']._serialized_end=6226
  _globals['_CMSGCLIENTREQUESTOFFLINEMESSAGECOUNT']._serialized_start=6228
  _globals['_CMSGCLIENTREQUESTOFFLINEMESSAGECOUNT']._serialized_end=6266
  _globals['_CMSGCLIENTCHATGETFRIENDMESSAGEHISTORY']._serialized_start=6268
  _globals['_CMSGCLIENTCHATGETFRIENDMESSAGEHISTORY']._serialized_end=6324
  _globals['_CMSGCLIENTCHATGETFRIENDMESSAGEHISTORYRESPONSE']._serialized_start=6327
  _globals['_CMSGCLIENTCHATGETFRIENDMESSAGEHISTORYRESPONSE']._serialized_end=6576
  _globals['_CMSGCLIENTCHATGETFRIENDMESSAGEHISTORYRESPONSE_FRIENDMESSAGE']._serialized_start=6490
  _globals['_CMSGCLIENTCHATGETFRIENDMESSAGEHISTORYRESPONSE_FRIENDMESSAGE']._serialized_end=6576
  _globals['_CMSGCLIENTCHATGETFRIENDMESSAGEHISTORYFOROFFLINEMESSAGES']._serialized_start=6578
  _globals['_CMSGCLIENTCHATGETFRIENDMESSAGEHISTORYFOROFFLINEMESSAGES']._serialized_end=6635
  _globals['_CMSGCLIENTFSGETFRIENDSSTEAMLEVELS']._serialized_start=6637
  _globals['_CMSGCLIENTFSGETFRIENDSSTEAMLEVELS']._serialized_end=6692
  _globals['_CMSGCLIENTFSGETFRIENDSSTEAMLEVELSRESPONSE']._serialized_start=6695
  _globals['_CMSGCLIENTFSGETFRIENDSSTEAMLEVELSRESPONSE']._serialized_end=6850
  _globals['_CMSGCLIENTFSGETFRIENDSSTEAMLEVELSRESPONSE_FRIEND']._serialized_start=6808
  _globals['_CMSGCLIENTFSGETFRIENDSSTEAMLEVELSRESPONSE_FRIEND']._serialized_end=6850
  _globals['_CMSGCLIENTEMAILADDRINFO']._serialized_start=6853
  _globals['_CMSGCLIENTEMAILADDRINFO']._serialized_end=7055
  _globals['_CMSGCREITEMVOTESUMMARY']._serialized_start=7058
  _globals['_CMSGCREITEMVOTESUMMARY']._serialized_end=7197
  _globals['_CMSGCREITEMVOTESUMMARY_PUBLISHEDFILEID']._serialized_start=7153
  _globals['_CMSGCREITEMVOTESUMMARY_PUBLISHEDFILEID']._serialized_end=7197
  _globals['_CMSGCREITEMVOTESUMMARYRESPONSE']._serialized_start=7200
  _globals['_CMSGCREITEMVOTESUMMARYRESPONSE']._serialized_end=7450
  _globals['_CMSGCREITEMVOTESUMMARYRESPONSE_ITEMVOTESUMMARY']._serialized_start=7332
  _globals['_CMSGCREITEMVOTESUMMARYRESPONSE_ITEMVOTESUMMARY']._serialized_end=7450
  _globals['_CMSGCREUPDATEUSERPUBLISHEDITEMVOTE']._serialized_start=7452
  _globals['_CMSGCREUPDATEUSERPUBLISHEDITEMVOTE']._serialized_end=7532
  _globals['_CMSGCREUPDATEUSERPUBLISHEDITEMVOTERESPONSE']._serialized_start=7534
  _globals['_CMSGCREUPDATEUSERPUBLISHEDITEMVOTERESPONSE']._serialized_end=7598
  _globals['_CMSGCREGETUSERPUBLISHEDITEMVOTEDETAILS']._serialized_start=7601
  _globals['_CMSGCREGETUSERPUBLISHEDITEMVOTEDETAILS']._serialized_end=7772
  _globals['_CMSGCREGETUSERPUBLISHEDITEMVOTEDETAILS_PUBLISHEDFILEID']._serialized_start=7153
  _globals['_CMSGCREGETUSERPUBLISHEDITEMVOTEDETAILS_PUBLISHEDFILEID']._serialized_end=7197
  _globals['_CMSGCREGETUSERPUBLISHEDITEMVOTEDETAILSRESPONSE']._serialized_start=7775
  _globals['_CMSGCREGETUSERPUBLISHEDITEMVOTEDETAILSRESPONSE']._serialized_end=8009
  _globals['_CMSGCREGETUSERPUBLISHEDITEMVOTEDETAILSRESPONSE_USERITEMVOTEDETAIL']._serialized_start=7945
  _globals['_CMSGCREGETUSERPUBLISHEDITEMVOTEDETAILSRESPONSE_USERITEMVOTEDETAIL']._serialized_end=8009
  _globals['_CMSGFSGETFOLLOWERCOUNT']._serialized_start=8011
  _globals['_CMSGFSGETFOLLOWERCOUNT']._serialized_end=8053
  _globals['_CMSGFSGETFOLLOWERCOUNTRESPONSE']._serialized_start=8055
  _globals['_CMSGFSGETFOLLOWERCOUNTRESPONSE']._serialized_end=8125
  _globals['_CMSGFSGETISFOLLOWING']._serialized_start=8127
  _globals['_CMSGFSGETISFOLLOWING']._serialized_end=8167
  _globals['_CMSGFSGETISFOLLOWINGRESPONSE']._serialized_start=8169
  _globals['_CMSGFSGETISFOLLOWINGRESPONSE']._serialized_end=8248
  _globals['_CMSGFSENUMERATEFOLLOWINGLIST']._serialized_start=8250
  _globals['_CMSGFSENUMERATEFOLLOWINGLIST']._serialized_end=8301
  _globals['_CMSGFSENUMERATEFOLLOWINGLISTRESPONSE']._serialized_start=8303
  _globals['_CMSGFSENUMERATEFOLLOWINGLISTRESPONSE']._serialized_end=8403
  _globals['_CMSGDPGETNUMBEROFCURRENTPLAYERS']._serialized_start=8405
  _globals['_CMSGDPGETNUMBEROFCURRENTPLAYERS']._serialized_end=8453
  _globals['_CMSGDPGETNUMBEROFCURRENTPLAYERSRESPONSE']._serialized_start=8455
  _globals['_CMSGDPGETNUMBEROFCURRENTPLAYERSRESPONSE']._serialized_end=8538
  _globals['_CMSGCLIENTFRIENDUSERSTATUSPUBLISHED']._serialized_start=8540
  _globals['_CMSGCLIENTFRIENDUSERSTATUSPUBLISHED']._serialized_end=8637
  _globals['_CMSGCLIENTSERVICEMETHODLEGACY']._serialized_start=8639
  _globals['_CMSGCLIENTSERVICEMETHODLEGACY']._serialized_end=8743
  _globals['_CMSGCLIENTSERVICEMETHODLEGACYRESPONSE']._serialized_start=8745
  _globals['_CMSGCLIENTSERVICEMETHODLEGACYRESPONSE']._serialized_end=8841
  _globals['_CMSGCLIENTUIMODE']._serialized_start=8843
  _globals['_CMSGCLIENTUIMODE']._serialized_end=8896
  _globals['_CMSGCLIENTVANITYURLCHANGEDNOTIFICATION']._serialized_start=8898
  _globals['_CMSGCLIENTVANITYURLCHANGEDNOTIFICATION']._serialized_end=8958
  _globals['_CMSGCLIENTAUTHORIZELOCALDEVICEREQUEST']._serialized_start=8960
  _globals['_CMSGCLIENTAUTHORIZELOCALDEVICEREQUEST']._serialized_end=9081
  _globals['_CMSGCLIENTAUTHORIZELOCALDEVICE']._serialized_start=9083
  _globals['_CMSGCLIENTAUTHORIZELOCALDEVICE']._serialized_end=9190
  _globals['_CMSGCLIENTAUTHORIZELOCALDEVICENOTIFICATION']._serialized_start=9192
  _globals['_CMSGCLIENTAUTHORIZELOCALDEVICENOTIFICATION']._serialized_end=9310
  _globals['_CMSGCLIENTDEAUTHORIZEDEVICEREQUEST']._serialized_start=9312
  _globals['_CMSGCLIENTDEAUTHORIZEDEVICEREQUEST']._serialized_end=9422
  _globals['_CMSGCLIENTDEAUTHORIZEDEVICE']._serialized_start=9424
  _globals['_CMSGCLIENTDEAUTHORIZEDEVICE']._serialized_end=9509
  _globals['_CMSGCLIENTUSELOCALDEVICEAUTHORIZATIONS']._serialized_start=9512
  _globals['_CMSGCLIENTUSELOCALDEVICEAUTHORIZATIONS']._serialized_end=9721
  _globals['_CMSGCLIENTUSELOCALDEVICEAUTHORIZATIONS_DEVICETOKEN']._serialized_start=9664
  _globals['_CMSGCLIENTUSELOCALDEVICEAUTHORIZATIONS_DEVICETOKEN']._serialized_end=9721
  _globals['_CMSGCLIENTGETAUTHORIZEDDEVICES']._serialized_start=9723
  _globals['_CMSGCLIENTGETAUTHORIZEDDEVICES']._serialized_end=9755
  _globals['_CMSGCLIENTGETAUTHORIZEDDEVICESRESPONSE']._serialized_start=9758
  _globals['_CMSGCLIENTGETAUTHORIZEDDEVICESRESPONSE']._serialized_end=10059
  _globals['_CMSGCLIENTGETAUTHORIZEDDEVICESRESPONSE_AUTHORIZEDDEVICE']._serialized_start=9906
  _globals['_CMSGCLIENTGETAUTHORIZEDDEVICESRESPONSE_AUTHORIZEDDEVICE']._serialized_end=10059
  _globals['_CMSGCLIENTSHAREDLIBRARYLOCKSTATUS']._serialized_start=10062
  _globals['_CMSGCLIENTSHAREDLIBRARYLOCKSTATUS']._serialized_end=10256
  _globals['_CMSGCLIENTSHAREDLIBRARYLOCKSTATUS_LOCKEDLIBRARY']._serialized_start=10204
  _globals['_CMSGCLIENTSHAREDLIBRARYLOCKSTATUS_LOCKEDLIBRARY']._serialized_end=10256
  _globals['_CMSGCLIENTSHAREDLIBRARYSTOPPLAYING']._serialized_start=10259
  _globals['_CMSGCLIENTSHAREDLIBRARYSTOPPLAYING']._serialized_end=10426
  _globals['_CMSGCLIENTSHAREDLIBRARYSTOPPLAYING_STOPAPP']._serialized_start=10383
  _globals['_CMSGCLIENTSHAREDLIBRARYSTOPPLAYING_STOPAPP']._serialized_end=10426
  _globals['_CMSGCLIENTSERVICECALL']._serialized_start=10429
  _globals['_CMSGCLIENTSERVICECALL']._serialized_end=10686
  _globals['_CMSGCLIENTSERVICEMODULE']._serialized_start=10688
  _globals['_CMSGCLIENTSERVICEMODULE']._serialized_end=10778
  _globals['_CMSGCLIENTSERVICECALLRESPONSE']._serialized_start=10781
  _globals['_CMSGCLIENTSERVICECALLRESPONSE']._serialized_end=11349
  _globals['_CMSGAMUNLOCKH264']._serialized_start=11351
  _globals['_CMSGAMUNLOCKH264']._serialized_end=11418
  _globals['_CMSGAMUNLOCKH264RESPONSE']._serialized_start=11420
  _globals['_CMSGAMUNLOCKH264RESPONSE']._serialized_end=11490
  _globals['_CMSGCLIENTPLAYINGSESSIONSTATE']._serialized_start=11492
  _globals['_CMSGCLIENTPLAYINGSESSIONSTATE']._serialized_end=11569
  _globals['_CMSGCLIENTKICKPLAYINGSESSION']._serialized_start=11571
  _globals['_CMSGCLIENTKICKPLAYINGSESSION']._serialized_end=11625
  _globals['_CMSGCLIENTVOICECALLPREAUTHORIZE']._serialized_start=11627
  _globals['_CMSGCLIENTVOICECALLPREAUTHORIZE']._serialized_end=11745
  _globals['_CMSGCLIENTVOICECALLPREAUTHORIZERESPONSE']._serialized_start=11748
  _globals['_CMSGCLIENTVOICECALLPREAUTHORIZERESPONSE']._serialized_end=11878
  _globals['_CMSGBADGECRAFTEDNOTIFICATION']._serialized_start=11880
  _globals['_CMSGBADGECRAFTEDNOTIFICATION']._serialized_end=11946
  _globals['_CMSGCLIENTSTARTPEERCONTENTSERVER']._serialized_start=11948
  _globals['_CMSGCLIENTSTARTPEERCONTENTSERVER']._serialized_end=12067
  _globals['_CMSGCLIENTSTARTPEERCONTENTSERVERRESPONSE']._serialized_start=12069
  _globals['_CMSGCLIENTSTARTPEERCONTENTSERVERRESPONSE']._serialized_end=12196
  _globals['_CMSGCLIENTGETPEERCONTENTINFO']._serialized_start=12198
  _globals['_CMSGCLIENTGETPEERCONTENTINFO']._serialized_end=12300
  _globals['_CMSGCLIENTGETPEERCONTENTINFORESPONSE']._serialized_start=12302
  _globals['_CMSGCLIENTGETPEERCONTENTINFORESPONSE']._serialized_end=12370
  _globals['_CMSGCLIENTPENDINGGAMELAUNCH']._serialized_start=12372
  _globals['_CMSGCLIENTPENDINGGAMELAUNCH']._serialized_end=12417
  _globals['_CMSGCLIENTPENDINGGAMELAUNCHRESPONSE']._serialized_start=12419
  _globals['_CMSGCLIENTPENDINGGAMELAUNCHRESPONSE']._serialized_end=12508
# @@protoc_insertion_point(module_scope)
