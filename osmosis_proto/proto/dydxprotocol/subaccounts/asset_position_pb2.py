# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/subaccounts/asset_position.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n-dydxprotocol/subaccounts/asset_position.proto\x12\x18\x64ydxprotocol.subaccounts\x1a\x14gogoproto/gogo.proto"\x8c\x01\n\rAssetPosition\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\r\x12Z\n\x08quantums\x18\x02 \x01(\x0c\x42H\xc8\xde\x1f\x00\xda\xde\x1f@github.com/dydxprotocol/v4-chain/protocol/dtypes.SerializableInt\x12\r\n\x05index\x18\x03 \x01(\x04\x42?Z=github.com/dydxprotocol/v4-chain/protocol/x/subaccounts/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.subaccounts.asset_position_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z=github.com/dydxprotocol/v4-chain/protocol/x/subaccounts/types"
    _globals["_ASSETPOSITION"].fields_by_name["quantums"]._loaded_options = None
    _globals["_ASSETPOSITION"].fields_by_name[
        "quantums"
    ]._serialized_options = (
        b"\310\336\037\000\332\336\037@github.com/dydxprotocol/v4-chain/protocol/dtypes.SerializableInt"
    )
    _globals["_ASSETPOSITION"]._serialized_start = 98
    _globals["_ASSETPOSITION"]._serialized_end = 238
# @@protoc_insertion_point(module_scope)
