# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/stats/params.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1f\x64ydxprotocol/stats/params.proto\x12\x12\x64ydxprotocol.stats\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto"F\n\x06Params\x12<\n\x0fwindow_duration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x42\x39Z7github.com/dydxprotocol/v4-chain/protocol/x/stats/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.stats.params_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z7github.com/dydxprotocol/v4-chain/protocol/x/stats/types"
    _globals["_PARAMS"].fields_by_name["window_duration"]._loaded_options = None
    _globals["_PARAMS"].fields_by_name["window_duration"]._serialized_options = b"\310\336\037\000\230\337\037\001"
    _globals["_PARAMS"]._serialized_start = 109
    _globals["_PARAMS"]._serialized_end = 179
# @@protoc_insertion_point(module_scope)
