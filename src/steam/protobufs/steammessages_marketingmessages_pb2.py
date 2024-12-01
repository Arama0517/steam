# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_marketingmessages.proto
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
    'steammessages_marketingmessages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2
import steam.protobufs.steammessages_storebrowse_pb2 as steammessages__storebrowse__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%steammessages_marketingmessages.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\x1a\x1fsteammessages_storebrowse.proto\"`\n5CMarketingMessages_GetActiveMarketingMessages_Request\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\x12\x16\n\x0e\x61nonymous_user\x18\x02 \x01(\x08\"\xaf\x06\n\x16\x43MarketingMessageProto\x12\x0b\n\x03gid\x18\x01 \x01(\x06\x12\r\n\x05title\x18\x02 \x01(\t\x12@\n\x04type\x18\x03 \x01(\x0e\x32\x16.EMarketingMessageType:\x1ak_EMarketingMessageInvalid\x12P\n\nvisibility\x18\x04 \x01(\x0e\x32\x1c.EMarketingMessageVisibility:\x1ek_EMarketingMessageVisibleBeta\x12\x10\n\x08priority\x18\x05 \x01(\r\x12]\n\x10\x61ssociation_type\x18\x06 \x01(\x0e\x32!.EMarketingMessageAssociationType: k_EMarketingMessageNoAssociation\x12\x15\n\rassociated_id\x18\x07 \x01(\r\x12\x17\n\x0f\x61ssociated_name\x18\x08 \x01(\t\x12\x12\n\nstart_date\x18\t \x01(\r\x12\x10\n\x08\x65nd_date\x18\n \x01(\r\x12\x15\n\rcountry_allow\x18\x0b \x01(\t\x12\x14\n\x0c\x63ountry_deny\x18\x0c \x01(\t\x12)\n!ownership_restrictions_overridden\x18\r \x01(\x08\x12\x16\n\x0emust_own_appid\x18\x0e \x01(\r\x12\x1a\n\x12must_not_own_appid\x18\x0f \x01(\r\x12\x1a\n\x12must_own_packageid\x18\x10 \x01(\r\x12\x1e\n\x16must_not_own_packageid\x18\x11 \x01(\r\x12 \n\x18must_have_launched_appid\x18\x12 \x01(\r\x12\x1f\n\x17\x61\x64\x64itional_restrictions\x18\x13 \x01(\t\x12\x15\n\rtemplate_type\x18\x14 \x01(\t\x12\x15\n\rtemplate_vars\x18\x15 \x01(\t\x12\r\n\x05\x66lags\x18\x16 \x01(\r\x12\x14\n\x0c\x63reator_name\x18\x17 \x01(\t\x12\x1a\n\x12template_vars_json\x18\x18 \x01(\t\x12$\n\x1c\x61\x64\x64itional_restrictions_json\x18\x19 \x01(\t\"\x82\x01\n6CMarketingMessages_GetActiveMarketingMessages_Response\x12)\n\x08messages\x18\x01 \x03(\x0b\x32\x17.CMarketingMessageProto\x12\x1d\n\x15time_next_message_age\x18\x02 \x01(\r\"\x93\x02\n6CMarketingMessages_GetMarketingMessagesForUser_Request\x12\x1d\n\x15include_seen_messages\x18\x01 \x01(\x08\x12\x14\n\x0c\x63ountry_code\x18\x02 \x01(\t\x12\x11\n\telanguage\x18\x03 \x01(\x05\x12\x18\n\x10operating_system\x18\x04 \x01(\x05\x12\x1e\n\x16\x63lient_package_version\x18\x05 \x01(\x05\x12$\n\x07\x63ontext\x18\x06 \x01(\x0b\x32\x13.StoreBrowseContext\x12\x31\n\x0c\x64\x61ta_request\x18\x07 \x01(\x0b\x32\x1b.StoreBrowseItemDataRequest\"\x93\x02\n\x18\x43\x44isplayMarketingMessage\x12\x0b\n\x03gid\x18\x01 \x01(\x06\x12\r\n\x05title\x18\x02 \x01(\t\x12@\n\x04type\x18\x03 \x01(\x0e\x32\x16.EMarketingMessageType:\x1ak_EMarketingMessageInvalid\x12(\n\x12\x61ssociated_item_id\x18\x04 \x01(\x0b\x32\x0c.StoreItemID\x12#\n\x0f\x61ssociated_item\x18\x05 \x01(\x0b\x32\n.StoreItem\x12\x17\n\x0f\x61ssociated_name\x18\x06 \x01(\t\x12\x15\n\rtemplate_type\x18\n \x01(\t\x12\x1a\n\x12template_vars_json\x18\x0b \x01(\t\"\xfa\x01\n7CMarketingMessages_GetMarketingMessagesForUser_Response\x12\x62\n\x08messages\x18\x01 \x03(\x0b\x32P.CMarketingMessages_GetMarketingMessagesForUser_Response.MarketingMessageForUser\x1a[\n\x17MarketingMessageForUser\x12\x14\n\x0c\x61lready_seen\x18\x01 \x01(\x08\x12*\n\x07message\x18\x02 \x01(\x0b\x32\x19.CDisplayMarketingMessage\"\xa4\x01\n?CMarketingMessages_DoesUserHavePendingMarketingMessages_Request\x12\x14\n\x0c\x63ountry_code\x18\x02 \x01(\t\x12\x11\n\telanguage\x18\x03 \x01(\x05\x12\x18\n\x10operating_system\x18\x04 \x01(\x05\x12\x1e\n\x16\x63lient_package_version\x18\x05 \x01(\x05\"\x7f\n@CMarketingMessages_DoesUserHavePendingMarketingMessages_Response\x12\x1c\n\x14has_pending_messages\x18\x01 \x01(\x08\x12\x1d\n\x15pending_message_count\x18\x02 \x01(\x05\"\x9d\x01\n5CMarketingMessages_GetDisplayMarketingMessage_Request\x12\x0b\n\x03gid\x18\x01 \x01(\x06\x12$\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x13.StoreBrowseContext\x12\x31\n\x0c\x64\x61ta_request\x18\x03 \x01(\x0b\x32\x1b.StoreBrowseItemDataRequest\"d\n6CMarketingMessages_GetDisplayMarketingMessage_Response\x12*\n\x07message\x18\x01 \x01(\x0b\x32\x19.CDisplayMarketingMessage\"\xb4\x01\n/CMarketingMessages_MarkMessageSeen_Notification\x12\x0b\n\x03gid\x18\x01 \x01(\x06\x12\x18\n\rdisplay_index\x18\x02 \x01(\r:\x01\x30\x12Z\n\rtemplate_type\x18\x03 \x01(\x0e\x32\x1e.EMarketingMessageTemplateType:#k_EMarketingMessageTemplate_Unknown\"=\n.CMarketingMessages_GetMarketingMessage_Request\x12\x0b\n\x03gid\x18\x01 \x01(\x06\"[\n/CMarketingMessages_GetMarketingMessage_Response\x12(\n\x07message\x18\x01 \x01(\x0b\x32\x17.CMarketingMessageProto\"p\n1CMarketingMessages_CreateMarketingMessage_Request\x12(\n\x07message\x18\x01 \x01(\x0b\x32\x17.CMarketingMessageProto\x12\x11\n\tfrom_json\x18\x02 \x01(\x08\"A\n2CMarketingMessages_CreateMarketingMessage_Response\x12\x0b\n\x03gid\x18\x01 \x01(\x06\"}\n1CMarketingMessages_UpdateMarketingMessage_Request\x12\x0b\n\x03gid\x18\x01 \x01(\x06\x12(\n\x07message\x18\x02 \x01(\x0b\x32\x17.CMarketingMessageProto\x12\x11\n\tfrom_json\x18\x03 \x01(\x08\"4\n2CMarketingMessages_UpdateMarketingMessage_Response\"@\n1CMarketingMessages_DeleteMarketingMessage_Request\x12\x0b\n\x03gid\x18\x01 \x01(\x06\"4\n2CMarketingMessages_DeleteMarketingMessage_Response\"\xfe\x01\n0CMarketingMessages_FindMarketingMessages_Request\x12S\n\x0blookup_type\x18\x01 \x01(\x0e\x32\x1c.EMarketingMessageLookupType: k_EMarketingMessageLookupInvalid\x12\x0b\n\x03gid\x18\x02 \x01(\x06\x12H\n\x0cmessage_type\x18\x03 \x01(\x0e\x32\x16.EMarketingMessageType:\x1ak_EMarketingMessageInvalid\x12\x0f\n\x07gidlist\x18\x04 \x03(\x06\x12\r\n\x05title\x18\x05 \x01(\t\"^\n1CMarketingMessages_FindMarketingMessages_Response\x12)\n\x08messages\x18\x01 \x03(\x0b\x32\x17.CMarketingMessageProto\"H\n9CMarketingMessages_GetMarketingMessageViewerStats_Request\x12\x0b\n\x03gid\x18\x01 \x01(\x06\"\xbb\x01\n\x1c\x43MarketingMessageHourlyStats\x12\x14\n\x0crt_time_hour\x18\x01 \x01(\r\x12\x12\n\nseen_count\x18\x02 \x01(\r\x12Z\n\rtemplate_type\x18\x03 \x01(\x0e\x32\x1e.EMarketingMessageTemplateType:#k_EMarketingMessageTemplate_Unknown\x12\x15\n\rdisplay_index\x18\x04 \x01(\r\"j\n:CMarketingMessages_GetMarketingMessageViewerStats_Response\x12,\n\x05stats\x18\x01 \x03(\x0b\x32\x1d.CMarketingMessageHourlyStats\"m\n?CMarketingMessages_GetMarketingMessagesViewerRangeStats_Request\x12\x15\n\rrt_start_time\x18\x01 \x01(\r\x12\x13\n\x0brt_end_time\x18\x02 \x01(\r\"p\n@CMarketingMessages_GetMarketingMessagesViewerRangeStats_Response\x12,\n\x05stats\x18\x01 \x03(\x0b\x32\x1d.CMarketingMessageHourlyStats\"P\n;CMarketingMessages_GetPartnerReadyToPublishMessages_Request\x12\x11\n\tpartnerid\x18\x01 \x01(\r\"k\n<CMarketingMessages_GetPartnerReadyToPublishMessages_Response\x12+\n\x08messages\x18\x01 \x03(\x0b\x32\x19.CDisplayMarketingMessage\"R\n0CMarketingMessages_PartnerPublishMessage_Request\x12\x0b\n\x03gid\x18\x01 \x01(\x06\x12\x11\n\tpartnerid\x18\x02 \x01(\r\"3\n1CMarketingMessages_PartnerPublishMessage_Response\"U\n3CMarketingMessages_GetPartnerMessagePreview_Request\x12\x0b\n\x03gid\x18\x01 \x01(\x06\x12\x11\n\tpartnerid\x18\x02 \x01(\r\"`\n4CMarketingMessages_GetPartnerMessagePreview_Response\x12(\n\x07message\x18\x01 \x01(\x0b\x32\x17.CMarketingMessageProto\"M\n8CMarketingMessage_GetMarketingMessagesForPartner_Request\x12\x11\n\tpartnerid\x18\x01 \x01(\r\"f\n9CMarketingMessage_GetMarketingMessagesForPartner_Response\x12)\n\x08messages\x18\x01 \x03(\x0b\x32\x17.CMarketingMessageProto\"G\n5CMarketingMessage_GetMarketingMessagesForApps_Request\x12\x0e\n\x06\x61ppids\x18\x01 \x03(\r\"c\n6CMarketingMessage_GetMarketingMessagesForApps_Response\x12)\n\x08messages\x18\x01 \x03(\x0b\x32\x17.CMarketingMessageProto*\xde\x04\n\x15\x45MarketingMessageType\x12\x1e\n\x1ak_EMarketingMessageInvalid\x10\x00\x12#\n\x1fk_EMarketingMessageNowAvailable\x10\x01\x12\"\n\x1ek_EMarketingMessageWeekendDeal\x10\x02\x12\"\n\x1ek_EMarketingMessagePrePurchase\x10\x03\x12\x1e\n\x1ak_EMarketingMessagePlayNow\x10\x04\x12!\n\x1dk_EMarketingMessagePreloadNow\x10\x05\x12\x1e\n\x1ak_EMarketingMessageGeneral\x10\x06\x12\x1f\n\x1bk_EMarketingMessageDemoQuit\x10\x07\x12\x1e\n\x1ak_EMarketingMessageGifting\x10\x08\x12 \n\x1ck_EMarketingMessageEJsKorner\x10\t\x12\x1d\n\x19k_EMarketingMessageUpdate\x10\n\x12\"\n\x1ek_EMarketingMessageMidweekDeal\x10\x0b\x12 \n\x1ck_EMarketingMessageDailyDeal\x10\x0c\x12\x1d\n\x19k_EMarketingMessageNewDLC\x10\r\x12\"\n\x1ek_EMarketingMessageFreeWeekend\x10\x0e\x12 \n\x1ck_EMarketingMessageSalePages\x10\x0f\x12(\n$k_EMarketingMessagePlaytestAvailable\x10\x10*\x99\x01\n\x1b\x45MarketingMessageVisibility\x12\"\n\x1ek_EMarketingMessageVisibleBeta\x10\x01\x12$\n k_EMarketingMessageVisiblePublic\x10\x02\x12\x30\n,k_EMarketingMessageVisibleApprovedForPublish\x10\x03*\x9f\x02\n EMarketingMessageAssociationType\x12$\n k_EMarketingMessageNoAssociation\x10\x00\x12%\n!k_EMarketingMessageAppAssociation\x10\x01\x12.\n*k_EMarketingMessageSubscriptionAssociation\x10\x02\x12+\n\'k_EMarketingMessagePublisherAssociation\x10\x03\x12\'\n#k_EMarketingMessageGenreAssociation\x10\x04\x12(\n$k_EMarketingMessageBundleAssociation\x10\x05*\xc4\x02\n\x1d\x45MarketingMessageTemplateType\x12\'\n#k_EMarketingMessageTemplate_Unknown\x10\x00\x12%\n!k_EMarketingMessageTemplate_Image\x10\x01\x12(\n$k_EMarketingMessageTemplate_Animated\x10\x02\x12.\n*k_EMarketingMessageTemplate_Featured_Video\x10\x03\x12,\n(k_EMarketingMessageTemplate_DLC_Override\x10\x04\x12&\n\"k_EMarketingMessageTemplate_Replay\x10\x05\x12#\n\x1fk_EMarketingMessageTemplate_MAX\x10\x06*\xe2\x01\n\x1b\x45MarketingMessageLookupType\x12$\n k_EMarketingMessageLookupInvalid\x10\x00\x12\"\n\x1ek_EMarketingMessageLookupByGID\x10\x01\x12#\n\x1fk_EMarketingMessageLookupActive\x10\x02\x12,\n(k_EMarketingMessageLookupByTitleWithType\x10\x03\x12&\n\"k_EMarketingMessageLookupByGIDList\x10\x04\x32\x99\x15\n\x11MarketingMessages\x12\x8d\x01\n\x1aGetActiveMarketingMessages\x12\x36.CMarketingMessages_GetActiveMarketingMessages_Request\x1a\x37.CMarketingMessages_GetActiveMarketingMessages_Response\x12\x90\x01\n\x1bGetMarketingMessagesForUser\x12\x37.CMarketingMessages_GetMarketingMessagesForUser_Request\x1a\x38.CMarketingMessages_GetMarketingMessagesForUser_Response\x12\xab\x01\n$DoesUserHavePendingMarketingMessages\x12@.CMarketingMessages_DoesUserHavePendingMarketingMessages_Request\x1a\x41.CMarketingMessages_DoesUserHavePendingMarketingMessages_Response\x12\x8d\x01\n\x1aGetDisplayMarketingMessage\x12\x36.CMarketingMessages_GetDisplayMarketingMessage_Request\x1a\x37.CMarketingMessages_GetDisplayMarketingMessage_Response\x12\x94\x01\n!GetDisplayMarketingMessageForUser\x12\x36.CMarketingMessages_GetDisplayMarketingMessage_Request\x1a\x37.CMarketingMessages_GetDisplayMarketingMessage_Response\x12\x92\x01\n\x1fGetDisplayMarketingMessageAdmin\x12\x36.CMarketingMessages_GetDisplayMarketingMessage_Request\x1a\x37.CMarketingMessages_GetDisplayMarketingMessage_Response\x12P\n\x0fMarkMessageSeen\x12\x30.CMarketingMessages_MarkMessageSeen_Notification\x1a\x0b.NoResponse\x12x\n\x13GetMarketingMessage\x12/.CMarketingMessages_GetMarketingMessage_Request\x1a\x30.CMarketingMessages_GetMarketingMessage_Response\x12\x81\x01\n\x16\x43reateMarketingMessage\x12\x32.CMarketingMessages_CreateMarketingMessage_Request\x1a\x33.CMarketingMessages_CreateMarketingMessage_Response\x12\x81\x01\n\x16UpdateMarketingMessage\x12\x32.CMarketingMessages_UpdateMarketingMessage_Request\x1a\x33.CMarketingMessages_UpdateMarketingMessage_Response\x12\x81\x01\n\x16\x44\x65leteMarketingMessage\x12\x32.CMarketingMessages_DeleteMarketingMessage_Request\x1a\x33.CMarketingMessages_DeleteMarketingMessage_Response\x12~\n\x15\x46indMarketingMessages\x12\x31.CMarketingMessages_FindMarketingMessages_Request\x1a\x32.CMarketingMessages_FindMarketingMessages_Response\x12\x99\x01\n\x1eGetMarketingMessageViewerStats\x12:.CMarketingMessages_GetMarketingMessageViewerStats_Request\x1a;.CMarketingMessages_GetMarketingMessageViewerStats_Response\x12\xab\x01\n$GetMarketingMessagesViewerRangeStats\x12@.CMarketingMessages_GetMarketingMessagesViewerRangeStats_Request\x1a\x41.CMarketingMessages_GetMarketingMessagesViewerRangeStats_Response\x12\x9f\x01\n GetPartnerReadyToPublishMessages\x12<.CMarketingMessages_GetPartnerReadyToPublishMessages_Request\x1a=.CMarketingMessages_GetPartnerReadyToPublishMessages_Response\x12~\n\x15PublishPartnerMessage\x12\x31.CMarketingMessages_PartnerPublishMessage_Request\x1a\x32.CMarketingMessages_PartnerPublishMessage_Response\x12\x87\x01\n\x18GetPartnerMessagePreview\x12\x34.CMarketingMessages_GetPartnerMessagePreview_Request\x1a\x35.CMarketingMessages_GetPartnerMessagePreview_Response\x12\x97\x01\n\x1eGetMarketingMessagesForPartner\x12\x39.CMarketingMessage_GetMarketingMessagesForPartner_Request\x1a:.CMarketingMessage_GetMarketingMessagesForPartner_Response\x12\x8e\x01\n\x1bGetMarketingMessagesForApps\x12\x36.CMarketingMessage_GetMarketingMessagesForApps_Request\x1a\x37.CMarketingMessage_GetMarketingMessagesForApps_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_marketingmessages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_EMARKETINGMESSAGETYPE']._serialized_start=5192
  _globals['_EMARKETINGMESSAGETYPE']._serialized_end=5798
  _globals['_EMARKETINGMESSAGEVISIBILITY']._serialized_start=5801
  _globals['_EMARKETINGMESSAGEVISIBILITY']._serialized_end=5954
  _globals['_EMARKETINGMESSAGEASSOCIATIONTYPE']._serialized_start=5957
  _globals['_EMARKETINGMESSAGEASSOCIATIONTYPE']._serialized_end=6244
  _globals['_EMARKETINGMESSAGETEMPLATETYPE']._serialized_start=6247
  _globals['_EMARKETINGMESSAGETEMPLATETYPE']._serialized_end=6571
  _globals['_EMARKETINGMESSAGELOOKUPTYPE']._serialized_start=6574
  _globals['_EMARKETINGMESSAGELOOKUPTYPE']._serialized_end=6800
  _globals['_CMARKETINGMESSAGES_GETACTIVEMARKETINGMESSAGES_REQUEST']._serialized_start=134
  _globals['_CMARKETINGMESSAGES_GETACTIVEMARKETINGMESSAGES_REQUEST']._serialized_end=230
  _globals['_CMARKETINGMESSAGEPROTO']._serialized_start=233
  _globals['_CMARKETINGMESSAGEPROTO']._serialized_end=1048
  _globals['_CMARKETINGMESSAGES_GETACTIVEMARKETINGMESSAGES_RESPONSE']._serialized_start=1051
  _globals['_CMARKETINGMESSAGES_GETACTIVEMARKETINGMESSAGES_RESPONSE']._serialized_end=1181
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGESFORUSER_REQUEST']._serialized_start=1184
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGESFORUSER_REQUEST']._serialized_end=1459
  _globals['_CDISPLAYMARKETINGMESSAGE']._serialized_start=1462
  _globals['_CDISPLAYMARKETINGMESSAGE']._serialized_end=1737
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGESFORUSER_RESPONSE']._serialized_start=1740
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGESFORUSER_RESPONSE']._serialized_end=1990
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGESFORUSER_RESPONSE_MARKETINGMESSAGEFORUSER']._serialized_start=1899
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGESFORUSER_RESPONSE_MARKETINGMESSAGEFORUSER']._serialized_end=1990
  _globals['_CMARKETINGMESSAGES_DOESUSERHAVEPENDINGMARKETINGMESSAGES_REQUEST']._serialized_start=1993
  _globals['_CMARKETINGMESSAGES_DOESUSERHAVEPENDINGMARKETINGMESSAGES_REQUEST']._serialized_end=2157
  _globals['_CMARKETINGMESSAGES_DOESUSERHAVEPENDINGMARKETINGMESSAGES_RESPONSE']._serialized_start=2159
  _globals['_CMARKETINGMESSAGES_DOESUSERHAVEPENDINGMARKETINGMESSAGES_RESPONSE']._serialized_end=2286
  _globals['_CMARKETINGMESSAGES_GETDISPLAYMARKETINGMESSAGE_REQUEST']._serialized_start=2289
  _globals['_CMARKETINGMESSAGES_GETDISPLAYMARKETINGMESSAGE_REQUEST']._serialized_end=2446
  _globals['_CMARKETINGMESSAGES_GETDISPLAYMARKETINGMESSAGE_RESPONSE']._serialized_start=2448
  _globals['_CMARKETINGMESSAGES_GETDISPLAYMARKETINGMESSAGE_RESPONSE']._serialized_end=2548
  _globals['_CMARKETINGMESSAGES_MARKMESSAGESEEN_NOTIFICATION']._serialized_start=2551
  _globals['_CMARKETINGMESSAGES_MARKMESSAGESEEN_NOTIFICATION']._serialized_end=2731
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGE_REQUEST']._serialized_start=2733
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGE_REQUEST']._serialized_end=2794
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGE_RESPONSE']._serialized_start=2796
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGE_RESPONSE']._serialized_end=2887
  _globals['_CMARKETINGMESSAGES_CREATEMARKETINGMESSAGE_REQUEST']._serialized_start=2889
  _globals['_CMARKETINGMESSAGES_CREATEMARKETINGMESSAGE_REQUEST']._serialized_end=3001
  _globals['_CMARKETINGMESSAGES_CREATEMARKETINGMESSAGE_RESPONSE']._serialized_start=3003
  _globals['_CMARKETINGMESSAGES_CREATEMARKETINGMESSAGE_RESPONSE']._serialized_end=3068
  _globals['_CMARKETINGMESSAGES_UPDATEMARKETINGMESSAGE_REQUEST']._serialized_start=3070
  _globals['_CMARKETINGMESSAGES_UPDATEMARKETINGMESSAGE_REQUEST']._serialized_end=3195
  _globals['_CMARKETINGMESSAGES_UPDATEMARKETINGMESSAGE_RESPONSE']._serialized_start=3197
  _globals['_CMARKETINGMESSAGES_UPDATEMARKETINGMESSAGE_RESPONSE']._serialized_end=3249
  _globals['_CMARKETINGMESSAGES_DELETEMARKETINGMESSAGE_REQUEST']._serialized_start=3251
  _globals['_CMARKETINGMESSAGES_DELETEMARKETINGMESSAGE_REQUEST']._serialized_end=3315
  _globals['_CMARKETINGMESSAGES_DELETEMARKETINGMESSAGE_RESPONSE']._serialized_start=3317
  _globals['_CMARKETINGMESSAGES_DELETEMARKETINGMESSAGE_RESPONSE']._serialized_end=3369
  _globals['_CMARKETINGMESSAGES_FINDMARKETINGMESSAGES_REQUEST']._serialized_start=3372
  _globals['_CMARKETINGMESSAGES_FINDMARKETINGMESSAGES_REQUEST']._serialized_end=3626
  _globals['_CMARKETINGMESSAGES_FINDMARKETINGMESSAGES_RESPONSE']._serialized_start=3628
  _globals['_CMARKETINGMESSAGES_FINDMARKETINGMESSAGES_RESPONSE']._serialized_end=3722
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGEVIEWERSTATS_REQUEST']._serialized_start=3724
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGEVIEWERSTATS_REQUEST']._serialized_end=3796
  _globals['_CMARKETINGMESSAGEHOURLYSTATS']._serialized_start=3799
  _globals['_CMARKETINGMESSAGEHOURLYSTATS']._serialized_end=3986
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGEVIEWERSTATS_RESPONSE']._serialized_start=3988
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGEVIEWERSTATS_RESPONSE']._serialized_end=4094
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGESVIEWERRANGESTATS_REQUEST']._serialized_start=4096
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGESVIEWERRANGESTATS_REQUEST']._serialized_end=4205
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGESVIEWERRANGESTATS_RESPONSE']._serialized_start=4207
  _globals['_CMARKETINGMESSAGES_GETMARKETINGMESSAGESVIEWERRANGESTATS_RESPONSE']._serialized_end=4319
  _globals['_CMARKETINGMESSAGES_GETPARTNERREADYTOPUBLISHMESSAGES_REQUEST']._serialized_start=4321
  _globals['_CMARKETINGMESSAGES_GETPARTNERREADYTOPUBLISHMESSAGES_REQUEST']._serialized_end=4401
  _globals['_CMARKETINGMESSAGES_GETPARTNERREADYTOPUBLISHMESSAGES_RESPONSE']._serialized_start=4403
  _globals['_CMARKETINGMESSAGES_GETPARTNERREADYTOPUBLISHMESSAGES_RESPONSE']._serialized_end=4510
  _globals['_CMARKETINGMESSAGES_PARTNERPUBLISHMESSAGE_REQUEST']._serialized_start=4512
  _globals['_CMARKETINGMESSAGES_PARTNERPUBLISHMESSAGE_REQUEST']._serialized_end=4594
  _globals['_CMARKETINGMESSAGES_PARTNERPUBLISHMESSAGE_RESPONSE']._serialized_start=4596
  _globals['_CMARKETINGMESSAGES_PARTNERPUBLISHMESSAGE_RESPONSE']._serialized_end=4647
  _globals['_CMARKETINGMESSAGES_GETPARTNERMESSAGEPREVIEW_REQUEST']._serialized_start=4649
  _globals['_CMARKETINGMESSAGES_GETPARTNERMESSAGEPREVIEW_REQUEST']._serialized_end=4734
  _globals['_CMARKETINGMESSAGES_GETPARTNERMESSAGEPREVIEW_RESPONSE']._serialized_start=4736
  _globals['_CMARKETINGMESSAGES_GETPARTNERMESSAGEPREVIEW_RESPONSE']._serialized_end=4832
  _globals['_CMARKETINGMESSAGE_GETMARKETINGMESSAGESFORPARTNER_REQUEST']._serialized_start=4834
  _globals['_CMARKETINGMESSAGE_GETMARKETINGMESSAGESFORPARTNER_REQUEST']._serialized_end=4911
  _globals['_CMARKETINGMESSAGE_GETMARKETINGMESSAGESFORPARTNER_RESPONSE']._serialized_start=4913
  _globals['_CMARKETINGMESSAGE_GETMARKETINGMESSAGESFORPARTNER_RESPONSE']._serialized_end=5015
  _globals['_CMARKETINGMESSAGE_GETMARKETINGMESSAGESFORAPPS_REQUEST']._serialized_start=5017
  _globals['_CMARKETINGMESSAGE_GETMARKETINGMESSAGESFORAPPS_REQUEST']._serialized_end=5088
  _globals['_CMARKETINGMESSAGE_GETMARKETINGMESSAGESFORAPPS_RESPONSE']._serialized_start=5090
  _globals['_CMARKETINGMESSAGE_GETMARKETINGMESSAGESFORAPPS_RESPONSE']._serialized_end=5189
  _globals['_MARKETINGMESSAGES']._serialized_start=6803
  _globals['_MARKETINGMESSAGES']._serialized_end=9516
_builder.BuildServices(DESCRIPTOR, 'steammessages_marketingmessages_pb2', _globals)
# @@protoc_insertion_point(module_scope)
