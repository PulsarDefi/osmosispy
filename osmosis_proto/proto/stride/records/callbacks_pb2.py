# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: stride/records/callbacks.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stride.records import records_pb2 as stride_dot_records_dot_records__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1estride/records/callbacks.proto\x12\x0estride.records\x1a\x1cstride/records/records.proto"-\n\x10TransferCallback\x12\x19\n\x11\x64\x65posit_record_id\x18\x01 \x01(\x04"L\n\x18TransferLSMTokenCallback\x12\x30\n\x07\x64\x65posit\x18\x01 \x01(\x0b\x32\x1f.stride.records.LSMTokenDepositB3Z1github.com/Stride-Labs/stride/v24/x/records/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "stride.records.callbacks_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"Z1github.com/Stride-Labs/stride/v24/x/records/types"
    )
    _globals["_TRANSFERCALLBACK"]._serialized_start = 80
    _globals["_TRANSFERCALLBACK"]._serialized_end = 125
    _globals["_TRANSFERLSMTOKENCALLBACK"]._serialized_start = 127
    _globals["_TRANSFERLSMTOKENCALLBACK"]._serialized_end = 203
# @@protoc_insertion_point(module_scope)
