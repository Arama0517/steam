# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enums_productinfo.proto
"""Generated protocol buffer code."""

from google.protobuf import (
    descriptor as _descriptor,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='enums_productinfo.proto',
    package='',
    syntax='proto2',
    serialized_options=b'H\001\220\001\001\200\265\030\001',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x17\x65nums_productinfo.proto\x1a\x18steammessages_base.proto*\xfb\x01\n\x14\x45\x43ontentDescriptorID\x12\x36\n2k_EContentDescriptor_FrequentNudityOrSexualContent\x10\x01\x12/\n+k_EContentDescriptor_FrequentViolenceOrGore\x10\x02\x12,\n(k_EContentDescriptor_StrongSexualContent\x10\x03\x12!\n\x1dk_EContentDescriptor_UNUSED_4\x10\x04\x12)\n%k_EContentDescriptor_AnyMatureContent\x10\x05\x42\tH\x01\x90\x01\x01\x80\xb5\x18\x01',
    dependencies=[
        steammessages__base__pb2.DESCRIPTOR,
    ],
)

_ECONTENTDESCRIPTORID = _descriptor.EnumDescriptor(
    name='EContentDescriptorID',
    full_name='EContentDescriptorID',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='k_EContentDescriptor_FrequentNudityOrSexualContent',
            index=0,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name='k_EContentDescriptor_FrequentViolenceOrGore',
            index=1,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name='k_EContentDescriptor_StrongSexualContent',
            index=2,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name='k_EContentDescriptor_UNUSED_4',
            index=3,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name='k_EContentDescriptor_AnyMatureContent',
            index=4,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=54,
    serialized_end=305,
)
_sym_db.RegisterEnumDescriptor(_ECONTENTDESCRIPTORID)

EContentDescriptorID = enum_type_wrapper.EnumTypeWrapper(_ECONTENTDESCRIPTORID)
k_EContentDescriptor_FrequentNudityOrSexualContent = 1
k_EContentDescriptor_FrequentViolenceOrGore = 2
k_EContentDescriptor_StrongSexualContent = 3
k_EContentDescriptor_UNUSED_4 = 4
k_EContentDescriptor_AnyMatureContent = 5


DESCRIPTOR.enum_types_by_name['EContentDescriptorID'] = _ECONTENTDESCRIPTORID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
