# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/clob/finalize_block.proto
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
    'dydxprotocol/clob/finalize_block.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dydxprotocol.clob import clob_pair_pb2 as dydxprotocol_dot_clob_dot_clob__pair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&dydxprotocol/clob/finalize_block.proto\x12\x11\x64ydxprotocol.clob\x1a!dydxprotocol/clob/clob_pair.proto\"`\n\x1c\x43lobStagedFinalizeBlockEvent\x12\x37\n\x10\x63reate_clob_pair\x18\x01 \x01(\x0b\x32\x1b.dydxprotocol.clob.ClobPairH\x00\x42\x07\n\x05\x65ventB8Z6github.com/dydxprotocol/v4-chain/protocol/x/clob/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.clob.finalize_block_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/dydxprotocol/v4-chain/protocol/x/clob/types'
  _globals['_CLOBSTAGEDFINALIZEBLOCKEVENT']._serialized_start=96
  _globals['_CLOBSTAGEDFINALIZEBLOCKEVENT']._serialized_end=192
# @@protoc_insertion_point(module_scope)
