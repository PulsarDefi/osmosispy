# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/bridge/bridge_event.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n&dydxprotocol/bridge/bridge_event.proto\x12\x13\x64ydxprotocol.bridge\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto"\x8d\x01\n\x0b\x42ridgeEvent\x12\n\n\x02id\x18\x01 \x01(\r\x12-\n\x04\x63oin\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12)\n\x07\x61\x64\x64ress\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x18\n\x10\x65th_block_height\x18\x04 \x01(\x04\x42:Z8github.com/dydxprotocol/v4-chain/protocol/x/bridge/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.bridge.bridge_event_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z8github.com/dydxprotocol/v4-chain/protocol/x/bridge/types"
    _globals["_BRIDGEEVENT"].fields_by_name["coin"]._loaded_options = None
    _globals["_BRIDGEEVENT"].fields_by_name["coin"]._serialized_options = b"\310\336\037\000"
    _globals["_BRIDGEEVENT"].fields_by_name["address"]._loaded_options = None
    _globals["_BRIDGEEVENT"].fields_by_name["address"]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_BRIDGEEVENT"]._serialized_start = 145
    _globals["_BRIDGEEVENT"]._serialized_end = 286
# @@protoc_insertion_point(module_scope)
