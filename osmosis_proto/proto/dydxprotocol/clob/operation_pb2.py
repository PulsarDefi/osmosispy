# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/clob/operation.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dydxprotocol.clob import matches_pb2 as dydxprotocol_dot_clob_dot_matches__pb2
from dydxprotocol.clob import order_pb2 as dydxprotocol_dot_clob_dot_order__pb2
from dydxprotocol.clob import order_removals_pb2 as dydxprotocol_dot_clob_dot_order__removals__pb2
from dydxprotocol.clob import tx_pb2 as dydxprotocol_dot_clob_dot_tx__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n!dydxprotocol/clob/operation.proto\x12\x11\x64ydxprotocol.clob\x1a\x1f\x64ydxprotocol/clob/matches.proto\x1a\x1d\x64ydxprotocol/clob/order.proto\x1a&dydxprotocol/clob/order_removals.proto\x1a\x1a\x64ydxprotocol/clob/tx.proto"\x9d\x02\n\tOperation\x12-\n\x05match\x18\x01 \x01(\x0b\x32\x1c.dydxprotocol.clob.ClobMatchH\x00\x12\x46\n\x1ashort_term_order_placement\x18\x02 \x01(\x0b\x32 .dydxprotocol.clob.MsgPlaceOrderH\x00\x12J\n\x1dshort_term_order_cancellation\x18\x03 \x01(\x0b\x32!.dydxprotocol.clob.MsgCancelOrderH\x00\x12@\n\x1apreexisting_stateful_order\x18\x04 \x01(\x0b\x32\x1a.dydxprotocol.clob.OrderIdH\x00\x42\x0b\n\toperation"\x93\x02\n\x11InternalOperation\x12-\n\x05match\x18\x01 \x01(\x0b\x32\x1c.dydxprotocol.clob.ClobMatchH\x00\x12\x46\n\x1ashort_term_order_placement\x18\x02 \x01(\x0b\x32 .dydxprotocol.clob.MsgPlaceOrderH\x00\x12@\n\x1apreexisting_stateful_order\x18\x03 \x01(\x0b\x32\x1a.dydxprotocol.clob.OrderIdH\x00\x12\x38\n\rorder_removal\x18\x04 \x01(\x0b\x32\x1f.dydxprotocol.clob.OrderRemovalH\x00\x42\x0b\n\toperationB8Z6github.com/dydxprotocol/v4-chain/protocol/x/clob/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.clob.operation_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z6github.com/dydxprotocol/v4-chain/protocol/x/clob/types"
    _globals["_OPERATION"]._serialized_start = 189
    _globals["_OPERATION"]._serialized_end = 474
    _globals["_INTERNALOPERATION"]._serialized_start = 477
    _globals["_INTERNALOPERATION"]._serialized_end = 752
# @@protoc_insertion_point(module_scope)
