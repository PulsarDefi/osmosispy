# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: stride/claim/genesis.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from stride.claim import claim_pb2 as stride_dot_claim_dot_claim__pb2
from stride.claim import params_pb2 as stride_dot_claim_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1astride/claim/genesis.proto\x12\x0cstride.claim\x1a\x14gogoproto/gogo.proto\x1a\x18stride/claim/claim.proto\x1a\x19stride/claim/params.proto"\x9b\x01\n\x0cGenesisState\x12;\n\x06params\x18\x01 \x01(\x0b\x32\x14.stride.claim.ParamsB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"params"\x12N\n\rclaim_records\x18\x02 \x03(\x0b\x32\x19.stride.claim.ClaimRecordB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"claim_records"B1Z/github.com/Stride-Labs/stride/v24/x/claim/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "stride.claim.genesis_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"Z/github.com/Stride-Labs/stride/v24/x/claim/types"
    )
    _globals["_GENESISSTATE"].fields_by_name["params"]._loaded_options = None
    _globals["_GENESISSTATE"].fields_by_name[
        "params"
    ]._serialized_options = b'\310\336\037\000\362\336\037\ryaml:"params"'
    _globals["_GENESISSTATE"].fields_by_name["claim_records"]._loaded_options = None
    _globals["_GENESISSTATE"].fields_by_name[
        "claim_records"
    ]._serialized_options = b'\310\336\037\000\362\336\037\024yaml:"claim_records"'
    _globals["_GENESISSTATE"]._serialized_start = 120
    _globals["_GENESISSTATE"]._serialized_end = 275
# @@protoc_insertion_point(module_scope)
