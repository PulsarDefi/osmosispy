# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/bridge/params.proto
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
    b'\n dydxprotocol/bridge/params.proto\x12\x13\x64ydxprotocol.bridge\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto"G\n\x0b\x45ventParams\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x14\n\x0c\x65th_chain_id\x18\x02 \x01(\x04\x12\x13\n\x0b\x65th_address\x18\x03 \x01(\t"\xda\x01\n\rProposeParams\x12\x1d\n\x15max_bridges_per_block\x18\x01 \x01(\r\x12\x43\n\x16propose_delay_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x15\n\rskip_rate_ppm\x18\x03 \x01(\r\x12N\n!skip_if_block_delayed_by_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01"9\n\x0cSafetyParams\x12\x13\n\x0bis_disabled\x18\x01 \x01(\x08\x12\x14\n\x0c\x64\x65lay_blocks\x18\x02 \x01(\rB:Z8github.com/dydxprotocol/v4-chain/protocol/x/bridge/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.bridge.params_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z8github.com/dydxprotocol/v4-chain/protocol/x/bridge/types"
    _globals["_PROPOSEPARAMS"].fields_by_name["propose_delay_duration"]._loaded_options = None
    _globals["_PROPOSEPARAMS"].fields_by_name[
        "propose_delay_duration"
    ]._serialized_options = b"\310\336\037\000\230\337\037\001"
    _globals["_PROPOSEPARAMS"].fields_by_name["skip_if_block_delayed_by_duration"]._loaded_options = None
    _globals["_PROPOSEPARAMS"].fields_by_name[
        "skip_if_block_delayed_by_duration"
    ]._serialized_options = b"\310\336\037\000\230\337\037\001"
    _globals["_EVENTPARAMS"]._serialized_start = 111
    _globals["_EVENTPARAMS"]._serialized_end = 182
    _globals["_PROPOSEPARAMS"]._serialized_start = 185
    _globals["_PROPOSEPARAMS"]._serialized_end = 403
    _globals["_SAFETYPARAMS"]._serialized_start = 405
    _globals["_SAFETYPARAMS"]._serialized_end = 462
# @@protoc_insertion_point(module_scope)
