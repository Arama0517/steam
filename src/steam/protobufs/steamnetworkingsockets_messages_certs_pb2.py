# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steamnetworkingsockets_messages_certs.proto
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
    'steamnetworkingsockets_messages_certs.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+steamnetworkingsockets_messages_certs.proto\"\x81\x01\n\'CMsgSteamNetworkingIdentityLegacyBinary\x12\x10\n\x08steam_id\x18\x10 \x01(\x06\x12\x15\n\rgeneric_bytes\x18\x02 \x01(\x0c\x12\x16\n\x0egeneric_string\x18\x03 \x01(\t\x12\x15\n\ripv6_and_port\x18\x04 \x01(\x0c\"\x8a\x03\n\x1c\x43MsgSteamDatagramCertificate\x12\x41\n\x08key_type\x18\x01 \x01(\x0e\x32&.CMsgSteamDatagramCertificate.EKeyType:\x07INVALID\x12\x10\n\x08key_data\x18\x02 \x01(\x0c\x12\x17\n\x0flegacy_steam_id\x18\x04 \x01(\x06\x12H\n\x16legacy_identity_binary\x18\x0b \x01(\x0b\x32(.CMsgSteamNetworkingIdentityLegacyBinary\x12\x17\n\x0fidentity_string\x18\x0c \x01(\t\x12!\n\x19gameserver_datacenter_ids\x18\x05 \x03(\x07\x12\x14\n\x0ctime_created\x18\x08 \x01(\x07\x12\x13\n\x0btime_expiry\x18\t \x01(\x07\x12\x0f\n\x07\x61pp_ids\x18\n \x03(\r\x12\x14\n\x0cip_addresses\x18\r \x03(\t\"$\n\x08\x45KeyType\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07\x45\x44\x32\x35\x35\x31\x39\x10\x01\"u\n\"CMsgSteamDatagramCertificateSigned\x12\x0c\n\x04\x63\x65rt\x18\x04 \x01(\x0c\x12\x11\n\tca_key_id\x18\x05 \x01(\x06\x12\x14\n\x0c\x63\x61_signature\x18\x06 \x01(\x0c\x12\x18\n\x10private_key_data\x18\x01 \x01(\x0c\"R\n#CMsgSteamDatagramCertificateRequest\x12+\n\x04\x63\x65rt\x18\x01 \x01(\x0b\x32\x1d.CMsgSteamDatagramCertificateB\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steamnetworkingsockets_messages_certs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_CMSGSTEAMNETWORKINGIDENTITYLEGACYBINARY']._serialized_start=48
  _globals['_CMSGSTEAMNETWORKINGIDENTITYLEGACYBINARY']._serialized_end=177
  _globals['_CMSGSTEAMDATAGRAMCERTIFICATE']._serialized_start=180
  _globals['_CMSGSTEAMDATAGRAMCERTIFICATE']._serialized_end=574
  _globals['_CMSGSTEAMDATAGRAMCERTIFICATE_EKEYTYPE']._serialized_start=538
  _globals['_CMSGSTEAMDATAGRAMCERTIFICATE_EKEYTYPE']._serialized_end=574
  _globals['_CMSGSTEAMDATAGRAMCERTIFICATESIGNED']._serialized_start=576
  _globals['_CMSGSTEAMDATAGRAMCERTIFICATESIGNED']._serialized_end=693
  _globals['_CMSGSTEAMDATAGRAMCERTIFICATEREQUEST']._serialized_start=695
  _globals['_CMSGSTEAMDATAGRAMCERTIFICATEREQUEST']._serialized_end=777
# @@protoc_insertion_point(module_scope)
