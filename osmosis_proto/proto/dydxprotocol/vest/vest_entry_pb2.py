# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/vest/vest_entry.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'dydxprotocol/vest/vest_entry.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"dydxprotocol/vest/vest_entry.proto\x12\x11\x64ydxprotocol.vest\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\"\xbe\x01\n\tVestEntry\x12\x16\n\x0evester_account\x18\x01 \x01(\t\x12\x18\n\x10treasury_account\x18\x02 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x03 \x01(\t\x12\x38\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x36\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x42\x38Z6github.com/dydxprotocol/v4-chain/protocol/x/vest/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.vest.vest_entry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/dydxprotocol/v4-chain/protocol/x/vest/types'
  _globals['_VESTENTRY'].fields_by_name['start_time']._loaded_options = None
  _globals['_VESTENTRY'].fields_by_name['start_time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_VESTENTRY'].fields_by_name['end_time']._loaded_options = None
  _globals['_VESTENTRY'].fields_by_name['end_time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_VESTENTRY']._serialized_start=113
  _globals['_VESTENTRY']._serialized_end=303
# @@protoc_insertion_point(module_scope)
