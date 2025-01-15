# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/clob/matches.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from dydxprotocol.subaccounts import subaccount_pb2 as dydxprotocol_dot_subaccounts_dot_subaccount__pb2
from dydxprotocol.clob import order_pb2 as dydxprotocol_dot_clob_dot_order__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1f\x64ydxprotocol/clob/matches.proto\x12\x11\x64ydxprotocol.clob\x1a\x14gogoproto/gogo.proto\x1a)dydxprotocol/subaccounts/subaccount.proto\x1a\x1d\x64ydxprotocol/clob/order.proto"\xf8\x01\n\tClobMatch\x12\x36\n\x0cmatch_orders\x18\x01 \x01(\x0b\x32\x1e.dydxprotocol.clob.MatchOrdersH\x00\x12S\n\x1bmatch_perpetual_liquidation\x18\x02 \x01(\x0b\x32,.dydxprotocol.clob.MatchPerpetualLiquidationH\x00\x12U\n\x1cmatch_perpetual_deleveraging\x18\x03 \x01(\x0b\x32-.dydxprotocol.clob.MatchPerpetualDeleveragingH\x00\x42\x07\n\x05match"Z\n\tMakerFill\x12\x13\n\x0b\x66ill_amount\x18\x01 \x01(\x04\x12\x38\n\x0emaker_order_id\x18\x02 \x01(\x0b\x32\x1a.dydxprotocol.clob.OrderIdB\x04\xc8\xde\x1f\x00"z\n\x0bMatchOrders\x12\x38\n\x0etaker_order_id\x18\x01 \x01(\x0b\x32\x1a.dydxprotocol.clob.OrderIdB\x04\xc8\xde\x1f\x00\x12\x31\n\x05\x66ills\x18\x02 \x03(\x0b\x32\x1c.dydxprotocol.clob.MakerFillB\x04\xc8\xde\x1f\x00"\xe0\x01\n\x19MatchPerpetualLiquidation\x12@\n\nliquidated\x18\x01 \x01(\x0b\x32&.dydxprotocol.subaccounts.SubaccountIdB\x04\xc8\xde\x1f\x00\x12\x14\n\x0c\x63lob_pair_id\x18\x02 \x01(\r\x12\x14\n\x0cperpetual_id\x18\x03 \x01(\r\x12\x12\n\ntotal_size\x18\x04 \x01(\x04\x12\x0e\n\x06is_buy\x18\x05 \x01(\x08\x12\x31\n\x05\x66ills\x18\x06 \x03(\x0b\x32\x1c.dydxprotocol.clob.MakerFillB\x04\xc8\xde\x1f\x00"\xc7\x02\n\x1aMatchPerpetualDeleveraging\x12@\n\nliquidated\x18\x01 \x01(\x0b\x32&.dydxprotocol.subaccounts.SubaccountIdB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cperpetual_id\x18\x02 \x01(\r\x12G\n\x05\x66ills\x18\x03 \x03(\x0b\x32\x32.dydxprotocol.clob.MatchPerpetualDeleveraging.FillB\x04\xc8\xde\x1f\x00\x12\x1b\n\x13is_final_settlement\x18\x04 \x01(\x08\x1ak\n\x04\x46ill\x12N\n\x18offsetting_subaccount_id\x18\x01 \x01(\x0b\x32&.dydxprotocol.subaccounts.SubaccountIdB\x04\xc8\xde\x1f\x00\x12\x13\n\x0b\x66ill_amount\x18\x02 \x01(\x04\x42\x38Z6github.com/dydxprotocol/v4-chain/protocol/x/clob/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.clob.matches_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z6github.com/dydxprotocol/v4-chain/protocol/x/clob/types"
    _globals["_MAKERFILL"].fields_by_name["maker_order_id"]._loaded_options = None
    _globals["_MAKERFILL"].fields_by_name["maker_order_id"]._serialized_options = b"\310\336\037\000"
    _globals["_MATCHORDERS"].fields_by_name["taker_order_id"]._loaded_options = None
    _globals["_MATCHORDERS"].fields_by_name["taker_order_id"]._serialized_options = b"\310\336\037\000"
    _globals["_MATCHORDERS"].fields_by_name["fills"]._loaded_options = None
    _globals["_MATCHORDERS"].fields_by_name["fills"]._serialized_options = b"\310\336\037\000"
    _globals["_MATCHPERPETUALLIQUIDATION"].fields_by_name["liquidated"]._loaded_options = None
    _globals["_MATCHPERPETUALLIQUIDATION"].fields_by_name["liquidated"]._serialized_options = b"\310\336\037\000"
    _globals["_MATCHPERPETUALLIQUIDATION"].fields_by_name["fills"]._loaded_options = None
    _globals["_MATCHPERPETUALLIQUIDATION"].fields_by_name["fills"]._serialized_options = b"\310\336\037\000"
    _globals["_MATCHPERPETUALDELEVERAGING_FILL"].fields_by_name["offsetting_subaccount_id"]._loaded_options = None
    _globals["_MATCHPERPETUALDELEVERAGING_FILL"].fields_by_name[
        "offsetting_subaccount_id"
    ]._serialized_options = b"\310\336\037\000"
    _globals["_MATCHPERPETUALDELEVERAGING"].fields_by_name["liquidated"]._loaded_options = None
    _globals["_MATCHPERPETUALDELEVERAGING"].fields_by_name["liquidated"]._serialized_options = b"\310\336\037\000"
    _globals["_MATCHPERPETUALDELEVERAGING"].fields_by_name["fills"]._loaded_options = None
    _globals["_MATCHPERPETUALDELEVERAGING"].fields_by_name["fills"]._serialized_options = b"\310\336\037\000"
    _globals["_CLOBMATCH"]._serialized_start = 151
    _globals["_CLOBMATCH"]._serialized_end = 399
    _globals["_MAKERFILL"]._serialized_start = 401
    _globals["_MAKERFILL"]._serialized_end = 491
    _globals["_MATCHORDERS"]._serialized_start = 493
    _globals["_MATCHORDERS"]._serialized_end = 615
    _globals["_MATCHPERPETUALLIQUIDATION"]._serialized_start = 618
    _globals["_MATCHPERPETUALLIQUIDATION"]._serialized_end = 842
    _globals["_MATCHPERPETUALDELEVERAGING"]._serialized_start = 845
    _globals["_MATCHPERPETUALDELEVERAGING"]._serialized_end = 1172
    _globals["_MATCHPERPETUALDELEVERAGING_FILL"]._serialized_start = 1065
    _globals["_MATCHPERPETUALDELEVERAGING_FILL"]._serialized_end = 1172
# @@protoc_insertion_point(module_scope)
