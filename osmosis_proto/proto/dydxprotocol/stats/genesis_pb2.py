# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/stats/genesis.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from dydxprotocol.stats import params_pb2 as dydxprotocol_dot_stats_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n dydxprotocol/stats/genesis.proto\x12\x12\x64ydxprotocol.stats\x1a\x14gogoproto/gogo.proto\x1a\x1f\x64ydxprotocol/stats/params.proto"@\n\x0cGenesisState\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32\x1a.dydxprotocol.stats.ParamsB\x04\xc8\xde\x1f\x00\x42\x39Z7github.com/dydxprotocol/v4-chain/protocol/x/stats/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.stats.genesis_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z7github.com/dydxprotocol/v4-chain/protocol/x/stats/types"
    _globals["_GENESISSTATE"].fields_by_name["params"]._loaded_options = None
    _globals["_GENESISSTATE"].fields_by_name["params"]._serialized_options = b"\310\336\037\000"
    _globals["_GENESISSTATE"]._serialized_start = 111
    _globals["_GENESISSTATE"]._serialized_end = 175
# @@protoc_insertion_point(module_scope)
