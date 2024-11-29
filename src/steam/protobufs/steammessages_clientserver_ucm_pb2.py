# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_clientserver_ucm.proto
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
    'steammessages_clientserver_ucm.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$steammessages_clientserver_ucm.proto\x1a\x18steammessages_base.proto\"\x81\x03\n\x1a\x43MsgClientUCMAddScreenshot\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x11\n\tthumbname\x18\x03 \x01(\t\x12\x13\n\x0bvr_filename\x18\x0e \x01(\t\x12\x17\n\x0frtime32_created\x18\x04 \x01(\x07\x12\r\n\x05width\x18\x05 \x01(\r\x12\x0e\n\x06height\x18\x06 \x01(\r\x12\x13\n\x0bpermissions\x18\x07 \x01(\r\x12\x0f\n\x07\x63\x61ption\x18\x08 \x01(\t\x12\x15\n\rshortcut_name\x18\t \x01(\t\x12,\n\x03tag\x18\n \x03(\x0b\x32\x1f.CMsgClientUCMAddScreenshot.Tag\x12\x16\n\x0etagged_steamid\x18\x0b \x03(\x06\x12\x13\n\x0bspoiler_tag\x18\x0c \x01(\x08\x12\x1e\n\x16tagged_publishedfileid\x18\r \x03(\x04\x1a*\n\x03Tag\x12\x10\n\x08tag_name\x18\x01 \x01(\t\x12\x11\n\ttag_value\x18\x02 \x01(\t\"}\n\"CMsgClientUCMAddScreenshotResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12*\n\x0cscreenshotid\x18\x02 \x01(\x06:\x14\x31\x38\x34\x34\x36\x37\x34\x34\x30\x37\x33\x37\x30\x39\x35\x35\x31\x36\x31\x35\x12\x17\n\x0fpublishedfileid\x18\x03 \x01(\x04\"K\n\x1d\x43MsgClientUCMDeleteScreenshot\x12*\n\x0cscreenshotid\x18\x01 \x01(\x06:\x14\x31\x38\x34\x34\x36\x37\x34\x34\x30\x37\x33\x37\x30\x39\x35\x35\x31\x36\x31\x35\";\n%CMsgClientUCMDeleteScreenshotResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\"\xd1\x02\n\x18\x43MsgClientUCMPublishFile\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x19\n\x11preview_file_name\x18\x03 \x01(\t\x12\x17\n\x0f\x63onsumer_app_id\x18\x04 \x01(\r\x12\r\n\x05title\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x0c\n\x04tags\x18\x08 \x03(\t\x12\x15\n\rworkshop_file\x18\t \x01(\x08\x12\x12\n\nvisibility\x18\n \x01(\x05\x12\x11\n\tfile_type\x18\x0b \x01(\r\x12\x0b\n\x03url\x18\x0c \x01(\t\x12\x16\n\x0evideo_provider\x18\r \x01(\r\x12\x1a\n\x12video_account_name\x18\x0e \x01(\t\x12\x18\n\x10video_identifier\x18\x0f \x01(\t\x12\x13\n\x0bin_progress\x18\x10 \x01(\x08\"\xa1\x01\n CMsgClientUCMPublishFileResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12/\n\x11published_file_id\x18\x02 \x01(\x06:\x14\x31\x38\x34\x34\x36\x37\x34\x34\x30\x37\x33\x37\x30\x39\x35\x35\x31\x36\x31\x35\x12\x38\n)needs_workshop_legal_agreement_acceptance\x18\x03 \x01(\x08:\x05\x66\x61lse\"\xf0\x08\n CMsgClientUCMUpdatePublishedFile\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x19\n\x11published_file_id\x18\x02 \x01(\x06\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x19\n\x11preview_file_name\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12\x12\n\nvisibility\x18\x08 \x01(\x05\x12\x13\n\x0bupdate_file\x18\t \x01(\x08\x12\x1b\n\x13update_preview_file\x18\n \x01(\x08\x12\x14\n\x0cupdate_title\x18\x0b \x01(\x08\x12\x1a\n\x12update_description\x18\x0c \x01(\x08\x12\x13\n\x0bupdate_tags\x18\r \x01(\x08\x12\x19\n\x11update_visibility\x18\x0e \x01(\x08\x12\x1a\n\x12\x63hange_description\x18\x0f \x01(\t\x12\x12\n\nupdate_url\x18\x10 \x01(\x08\x12\x0b\n\x03url\x18\x11 \x01(\t\x12\x1f\n\x17update_content_manifest\x18\x12 \x01(\x08\x12\x18\n\x10\x63ontent_manifest\x18\x13 \x01(\x06\x12\x10\n\x08metadata\x18\x14 \x01(\t\x12\x17\n\x0fupdate_metadata\x18\x15 \x01(\x08\x12\x13\n\x08language\x18\x16 \x01(\x05:\x01\x30\x12\x16\n\x0eremoved_kvtags\x18\x17 \x03(\t\x12=\n\x06kvtags\x18\x18 \x03(\x0b\x32-.CMsgClientUCMUpdatePublishedFile.KeyValueTag\x12\x45\n\x08previews\x18\x19 \x03(\x0b\x32\x33.CMsgClientUCMUpdatePublishedFile.AdditionalPreview\x12\x1a\n\x12previews_to_remove\x18\x1a \x03(\x05\x12\x19\n\x11\x63lear_in_progress\x18\x1b \x01(\x08\x12\x19\n\x11remove_all_kvtags\x18\x1c \x01(\x08\x12\"\n\x1a\x63ontent_descriptors_to_add\x18\x1d \x03(\x05\x12%\n\x1d\x63ontent_descriptors_to_remove\x18\x1e \x03(\x05\x12\x1f\n\x10\x61llow_admin_tags\x18\x1f \x01(\x08:\x05\x66\x61lse\x12\x19\n\x11\x65xternal_asset_id\x18  \x01(\x04\x12\x17\n\x0fgame_branch_min\x18! \x01(\t\x12\x17\n\x0fgame_branch_max\x18\" \x01(\t\x1a)\n\x0bKeyValueTag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1a\x8c\x01\n\x11\x41\x64\x64itionalPreview\x12\x1a\n\x12original_file_name\x18\x01 \x01(\t\x12\x1a\n\x12internal_file_name\x18\x02 \x01(\t\x12\x0f\n\x07videoid\x18\x03 \x01(\t\x12\x14\n\x0cpreview_type\x18\x04 \x01(\r\x12\x18\n\x0cupdate_index\x18\x05 \x01(\x05:\x02-1\"x\n(CMsgClientUCMUpdatePublishedFileResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x38\n)needs_workshop_legal_agreement_acceptance\x18\x02 \x01(\x08:\x05\x66\x61lse\"M\n CMsgClientUCMDeletePublishedFile\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\">\n(CMsgClientUCMDeletePublishedFileResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\"\x8c\x01\n4CMsgClientUCMEnumerateUserSubscribedFilesWithUpdates\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x13\n\x0bstart_index\x18\x02 \x01(\r\x12\x12\n\nstart_time\x18\x03 \x01(\x07\x12\x1b\n\x10\x64\x65sired_revision\x18\x04 \x01(\r:\x01\x30\"\xe4\x04\n<CMsgClientUCMEnumerateUserSubscribedFilesWithUpdatesResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12g\n\x10subscribed_files\x18\x02 \x03(\x0b\x32M.CMsgClientUCMEnumerateUserSubscribedFilesWithUpdatesResponse.PublishedFileId\x12\x15\n\rtotal_results\x18\x03 \x01(\r\x1ai\n\x0e\x41uthorSnapshot\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x17\n\x0fgame_branch_min\x18\x02 \x01(\t\x12\x17\n\x0fgame_branch_max\x18\x03 \x01(\t\x12\x12\n\nmanifestid\x18\x04 \x01(\x06\x1a\xa4\x02\n\x0fPublishedFileId\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\x12\x1d\n\x12rtime32_subscribed\x18\x02 \x01(\x07:\x01\x30\x12\r\n\x05\x61ppid\x18\x03 \x01(\r\x12\x15\n\rfile_hcontent\x18\x04 \x01(\x06\x12\x11\n\tfile_size\x18\x05 \x01(\r\x12\x1c\n\x14rtime32_last_updated\x18\x06 \x01(\x07\x12\x18\n\x10is_depot_content\x18\x07 \x01(\x08\x12\x66\n\x10\x61uthor_snapshots\x18\x08 \x03(\x0b\x32L.CMsgClientUCMEnumerateUserSubscribedFilesWithUpdatesResponse.AuthorSnapshot\"\xb5\x01\n!CMsgClientUCMPublishedFileUpdated\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12\x14\n\x0ctime_updated\x18\x03 \x01(\r\x12\x10\n\x08hcontent\x18\x04 \x01(\x06\x12\x11\n\tfile_size\x18\x05 \x01(\x07\x12\x18\n\x10is_depot_content\x18\x06 \x01(\x08\x12\x10\n\x08revision\x18\x07 \x01(\r\"k\n$CMsgClientWorkshopItemChangesRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x19\n\x11last_time_updated\x18\x02 \x01(\r\x12\x18\n\x10num_items_needed\x18\x03 \x01(\r\"\xfb\x01\n%CMsgClientWorkshopItemChangesResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x13\n\x0bupdate_time\x18\x02 \x01(\r\x12O\n\x0eworkshop_items\x18\x05 \x03(\x0b\x32\x37.CMsgClientWorkshopItemChangesResponse.WorkshopItemInfo\x1aX\n\x10WorkshopItemInfo\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\x12\x14\n\x0ctime_updated\x18\x02 \x01(\r\x12\x13\n\x0bmanifest_id\x18\x03 \x01(\x06\"d\n\'CMsgClientUCMSetUserPublishedFileAction\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\x05\"E\n/CMsgClientUCMSetUserPublishedFileActionResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\"g\n0CMsgClientUCMEnumeratePublishedFilesByUserAction\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x13\n\x0bstart_index\x18\x02 \x01(\r\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\x05\"\x94\x02\n8CMsgClientUCMEnumeratePublishedFilesByUserActionResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x62\n\x0fpublished_files\x18\x02 \x03(\x0b\x32I.CMsgClientUCMEnumeratePublishedFilesByUserActionResponse.PublishedFileId\x12\x15\n\rtotal_results\x18\x03 \x01(\r\x1aI\n\x0fPublishedFileId\x12\x19\n\x11published_file_id\x18\x01 \x01(\x06\x12\x1b\n\x10rtime_time_stamp\x18\x02 \x01(\x07:\x01\x30\"\x1e\n\x1c\x43MsgClientScreenshotsChangedB\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_clientserver_ucm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_CMSGCLIENTUCMADDSCREENSHOT']._serialized_start=67
  _globals['_CMSGCLIENTUCMADDSCREENSHOT']._serialized_end=452
  _globals['_CMSGCLIENTUCMADDSCREENSHOT_TAG']._serialized_start=410
  _globals['_CMSGCLIENTUCMADDSCREENSHOT_TAG']._serialized_end=452
  _globals['_CMSGCLIENTUCMADDSCREENSHOTRESPONSE']._serialized_start=454
  _globals['_CMSGCLIENTUCMADDSCREENSHOTRESPONSE']._serialized_end=579
  _globals['_CMSGCLIENTUCMDELETESCREENSHOT']._serialized_start=581
  _globals['_CMSGCLIENTUCMDELETESCREENSHOT']._serialized_end=656
  _globals['_CMSGCLIENTUCMDELETESCREENSHOTRESPONSE']._serialized_start=658
  _globals['_CMSGCLIENTUCMDELETESCREENSHOTRESPONSE']._serialized_end=717
  _globals['_CMSGCLIENTUCMPUBLISHFILE']._serialized_start=720
  _globals['_CMSGCLIENTUCMPUBLISHFILE']._serialized_end=1057
  _globals['_CMSGCLIENTUCMPUBLISHFILERESPONSE']._serialized_start=1060
  _globals['_CMSGCLIENTUCMPUBLISHFILERESPONSE']._serialized_end=1221
  _globals['_CMSGCLIENTUCMUPDATEPUBLISHEDFILE']._serialized_start=1224
  _globals['_CMSGCLIENTUCMUPDATEPUBLISHEDFILE']._serialized_end=2360
  _globals['_CMSGCLIENTUCMUPDATEPUBLISHEDFILE_KEYVALUETAG']._serialized_start=2176
  _globals['_CMSGCLIENTUCMUPDATEPUBLISHEDFILE_KEYVALUETAG']._serialized_end=2217
  _globals['_CMSGCLIENTUCMUPDATEPUBLISHEDFILE_ADDITIONALPREVIEW']._serialized_start=2220
  _globals['_CMSGCLIENTUCMUPDATEPUBLISHEDFILE_ADDITIONALPREVIEW']._serialized_end=2360
  _globals['_CMSGCLIENTUCMUPDATEPUBLISHEDFILERESPONSE']._serialized_start=2362
  _globals['_CMSGCLIENTUCMUPDATEPUBLISHEDFILERESPONSE']._serialized_end=2482
  _globals['_CMSGCLIENTUCMDELETEPUBLISHEDFILE']._serialized_start=2484
  _globals['_CMSGCLIENTUCMDELETEPUBLISHEDFILE']._serialized_end=2561
  _globals['_CMSGCLIENTUCMDELETEPUBLISHEDFILERESPONSE']._serialized_start=2563
  _globals['_CMSGCLIENTUCMDELETEPUBLISHEDFILERESPONSE']._serialized_end=2625
  _globals['_CMSGCLIENTUCMENUMERATEUSERSUBSCRIBEDFILESWITHUPDATES']._serialized_start=2628
  _globals['_CMSGCLIENTUCMENUMERATEUSERSUBSCRIBEDFILESWITHUPDATES']._serialized_end=2768
  _globals['_CMSGCLIENTUCMENUMERATEUSERSUBSCRIBEDFILESWITHUPDATESRESPONSE']._serialized_start=2771
  _globals['_CMSGCLIENTUCMENUMERATEUSERSUBSCRIBEDFILESWITHUPDATESRESPONSE']._serialized_end=3383
  _globals['_CMSGCLIENTUCMENUMERATEUSERSUBSCRIBEDFILESWITHUPDATESRESPONSE_AUTHORSNAPSHOT']._serialized_start=2983
  _globals['_CMSGCLIENTUCMENUMERATEUSERSUBSCRIBEDFILESWITHUPDATESRESPONSE_AUTHORSNAPSHOT']._serialized_end=3088
  _globals['_CMSGCLIENTUCMENUMERATEUSERSUBSCRIBEDFILESWITHUPDATESRESPONSE_PUBLISHEDFILEID']._serialized_start=3091
  _globals['_CMSGCLIENTUCMENUMERATEUSERSUBSCRIBEDFILESWITHUPDATESRESPONSE_PUBLISHEDFILEID']._serialized_end=3383
  _globals['_CMSGCLIENTUCMPUBLISHEDFILEUPDATED']._serialized_start=3386
  _globals['_CMSGCLIENTUCMPUBLISHEDFILEUPDATED']._serialized_end=3567
  _globals['_CMSGCLIENTWORKSHOPITEMCHANGESREQUEST']._serialized_start=3569
  _globals['_CMSGCLIENTWORKSHOPITEMCHANGESREQUEST']._serialized_end=3676
  _globals['_CMSGCLIENTWORKSHOPITEMCHANGESRESPONSE']._serialized_start=3679
  _globals['_CMSGCLIENTWORKSHOPITEMCHANGESRESPONSE']._serialized_end=3930
  _globals['_CMSGCLIENTWORKSHOPITEMCHANGESRESPONSE_WORKSHOPITEMINFO']._serialized_start=3842
  _globals['_CMSGCLIENTWORKSHOPITEMCHANGESRESPONSE_WORKSHOPITEMINFO']._serialized_end=3930
  _globals['_CMSGCLIENTUCMSETUSERPUBLISHEDFILEACTION']._serialized_start=3932
  _globals['_CMSGCLIENTUCMSETUSERPUBLISHEDFILEACTION']._serialized_end=4032
  _globals['_CMSGCLIENTUCMSETUSERPUBLISHEDFILEACTIONRESPONSE']._serialized_start=4034
  _globals['_CMSGCLIENTUCMSETUSERPUBLISHEDFILEACTIONRESPONSE']._serialized_end=4103
  _globals['_CMSGCLIENTUCMENUMERATEPUBLISHEDFILESBYUSERACTION']._serialized_start=4105
  _globals['_CMSGCLIENTUCMENUMERATEPUBLISHEDFILESBYUSERACTION']._serialized_end=4208
  _globals['_CMSGCLIENTUCMENUMERATEPUBLISHEDFILESBYUSERACTIONRESPONSE']._serialized_start=4211
  _globals['_CMSGCLIENTUCMENUMERATEPUBLISHEDFILESBYUSERACTIONRESPONSE']._serialized_end=4487
  _globals['_CMSGCLIENTUCMENUMERATEPUBLISHEDFILESBYUSERACTIONRESPONSE_PUBLISHEDFILEID']._serialized_start=4414
  _globals['_CMSGCLIENTUCMENUMERATEPUBLISHEDFILESBYUSERACTIONRESPONSE_PUBLISHEDFILEID']._serialized_end=4487
  _globals['_CMSGCLIENTSCREENSHOTSCHANGED']._serialized_start=4489
  _globals['_CMSGCLIENTSCREENSHOTSCHANGED']._serialized_end=4519
# @@protoc_insertion_point(module_scope)
