# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: contenthubs.proto
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
    'contenthubs.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63ontenthubs.proto\x1a\x18steammessages_base.proto\"\xe1\x04\n\x10\x43StorePageFilter\x12\x35\n\x0bsale_filter\x18\x01 \x01(\x0b\x32 .CStorePageFilter.SalePageFilter\x12>\n\x12\x63ontent_hub_filter\x18\x02 \x01(\x0b\x32\".CStorePageFilter.ContentHubFilter\x12\x34\n\rstore_filters\x18\x03 \x03(\x0b\x32\x1d.CStorePageFilter.StoreFilter\x1a$\n\x0eSalePageFilter\x12\x12\n\nsale_tagid\x18\x01 \x01(\r\x1a\xc2\x02\n\x10\x43ontentHubFilter\x12\x10\n\x08hub_type\x18\x01 \x01(\t\x12\x14\n\x0chub_category\x18\x02 \x01(\t\x12\x11\n\thub_tagid\x18\x03 \x01(\r\x12]\n\x0f\x64iscount_filter\x18\x04 \x01(\x0e\x32\x1e.EContentHubDiscountFilterType:$k_EContentHubDiscountFilterType_None\x12;\n\x05optin\x18\x05 \x01(\x0b\x32,.CStorePageFilter.ContentHubFilter.OptInInfo\x1aW\n\tOptInInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0boptin_tagid\x18\x02 \x01(\r\x12\x13\n\x0bprune_tagid\x18\x03 \x01(\r\x12\x12\n\noptin_only\x18\x04 \x01(\x08\x1a\x35\n\x0bStoreFilter\x12\x13\n\x0b\x66ilter_json\x18\x01 \x01(\t\x12\x11\n\tcache_key\x18\x02 \x01(\t*\xb5\x01\n\x1d\x45\x43ontentHubDiscountFilterType\x12(\n$k_EContentHubDiscountFilterType_None\x10\x00\x12\x31\n-k_EContentHubDiscountFilterType_DiscountsOnly\x10\x01\x12\x37\n3k_EContentHubDiscountFilterType_PrioritizeDiscounts\x10\x02\x42\tH\x01\x90\x01\x01\x80\xb5\x18\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'contenthubs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\001\200\265\030\001'
  _globals['_ECONTENTHUBDISCOUNTFILTERTYPE']._serialized_start=660
  _globals['_ECONTENTHUBDISCOUNTFILTERTYPE']._serialized_end=841
  _globals['_CSTOREPAGEFILTER']._serialized_start=48
  _globals['_CSTOREPAGEFILTER']._serialized_end=657
  _globals['_CSTOREPAGEFILTER_SALEPAGEFILTER']._serialized_start=241
  _globals['_CSTOREPAGEFILTER_SALEPAGEFILTER']._serialized_end=277
  _globals['_CSTOREPAGEFILTER_CONTENTHUBFILTER']._serialized_start=280
  _globals['_CSTOREPAGEFILTER_CONTENTHUBFILTER']._serialized_end=602
  _globals['_CSTOREPAGEFILTER_CONTENTHUBFILTER_OPTININFO']._serialized_start=515
  _globals['_CSTOREPAGEFILTER_CONTENTHUBFILTER_OPTININFO']._serialized_end=602
  _globals['_CSTOREPAGEFILTER_STOREFILTER']._serialized_start=604
  _globals['_CSTOREPAGEFILTER_STOREFILTER']._serialized_end=657
# @@protoc_insertion_point(module_scope)
