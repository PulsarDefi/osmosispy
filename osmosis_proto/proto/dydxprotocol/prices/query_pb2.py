# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/prices/query.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from dydxprotocol.prices import market_param_pb2 as dydxprotocol_dot_prices_dot_market__param__pb2
from dydxprotocol.prices import market_price_pb2 as dydxprotocol_dot_prices_dot_market__price__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1f\x64ydxprotocol/prices/query.proto\x12\x13\x64ydxprotocol.prices\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a&dydxprotocol/prices/market_param.proto\x1a&dydxprotocol/prices/market_price.proto"%\n\x17QueryMarketPriceRequest\x12\n\n\x02id\x18\x01 \x01(\r"X\n\x18QueryMarketPriceResponse\x12<\n\x0cmarket_price\x18\x01 \x01(\x0b\x32 .dydxprotocol.prices.MarketPriceB\x04\xc8\xde\x1f\x00"Y\n\x1bQueryAllMarketPricesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest"\x9a\x01\n\x1cQueryAllMarketPricesResponse\x12=\n\rmarket_prices\x18\x01 \x03(\x0b\x32 .dydxprotocol.prices.MarketPriceB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse"%\n\x17QueryMarketParamRequest\x12\n\n\x02id\x18\x01 \x01(\r"X\n\x18QueryMarketParamResponse\x12<\n\x0cmarket_param\x18\x01 \x01(\x0b\x32 .dydxprotocol.prices.MarketParamB\x04\xc8\xde\x1f\x00"Y\n\x1bQueryAllMarketParamsRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest"\x9a\x01\n\x1cQueryAllMarketParamsResponse\x12=\n\rmarket_params\x18\x01 \x03(\x0b\x32 .dydxprotocol.prices.MarketParamB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse"\x1a\n\x18QueryNextMarketIdRequest"3\n\x19QueryNextMarketIdResponse\x12\x16\n\x0enext_market_id\x18\x01 \x01(\r2\x9c\x06\n\x05Query\x12\x94\x01\n\x0bMarketPrice\x12,.dydxprotocol.prices.QueryMarketPriceRequest\x1a-.dydxprotocol.prices.QueryMarketPriceResponse"(\x82\xd3\xe4\x93\x02"\x12 /dydxprotocol/prices/market/{id}\x12\x9b\x01\n\x0f\x41llMarketPrices\x12\x30.dydxprotocol.prices.QueryAllMarketPricesRequest\x1a\x31.dydxprotocol.prices.QueryAllMarketPricesResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/dydxprotocol/prices/market\x12\x9b\x01\n\x0bMarketParam\x12,.dydxprotocol.prices.QueryMarketParamRequest\x1a-.dydxprotocol.prices.QueryMarketParamResponse"/\x82\xd3\xe4\x93\x02)\x12\'/dydxprotocol/prices/params/market/{id}\x12\xa2\x01\n\x0f\x41llMarketParams\x12\x30.dydxprotocol.prices.QueryAllMarketParamsRequest\x1a\x31.dydxprotocol.prices.QueryAllMarketParamsResponse"*\x82\xd3\xe4\x93\x02$\x12"/dydxprotocol/prices/params/market\x12\x9a\x01\n\x0cNextMarketId\x12-.dydxprotocol.prices.QueryNextMarketIdRequest\x1a..dydxprotocol.prices.QueryNextMarketIdResponse"+\x82\xd3\xe4\x93\x02%\x12#/dydxprotocol/prices/next_market_idB:Z8github.com/dydxprotocol/v4-chain/protocol/x/prices/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.prices.query_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z8github.com/dydxprotocol/v4-chain/protocol/x/prices/types"
    _globals["_QUERYMARKETPRICERESPONSE"].fields_by_name["market_price"]._loaded_options = None
    _globals["_QUERYMARKETPRICERESPONSE"].fields_by_name["market_price"]._serialized_options = b"\310\336\037\000"
    _globals["_QUERYALLMARKETPRICESRESPONSE"].fields_by_name["market_prices"]._loaded_options = None
    _globals["_QUERYALLMARKETPRICESRESPONSE"].fields_by_name["market_prices"]._serialized_options = b"\310\336\037\000"
    _globals["_QUERYMARKETPARAMRESPONSE"].fields_by_name["market_param"]._loaded_options = None
    _globals["_QUERYMARKETPARAMRESPONSE"].fields_by_name["market_param"]._serialized_options = b"\310\336\037\000"
    _globals["_QUERYALLMARKETPARAMSRESPONSE"].fields_by_name["market_params"]._loaded_options = None
    _globals["_QUERYALLMARKETPARAMSRESPONSE"].fields_by_name["market_params"]._serialized_options = b"\310\336\037\000"
    _globals["_QUERY"].methods_by_name["MarketPrice"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "MarketPrice"
    ]._serialized_options = b'\202\323\344\223\002"\022 /dydxprotocol/prices/market/{id}'
    _globals["_QUERY"].methods_by_name["AllMarketPrices"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "AllMarketPrices"
    ]._serialized_options = b"\202\323\344\223\002\035\022\033/dydxprotocol/prices/market"
    _globals["_QUERY"].methods_by_name["MarketParam"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "MarketParam"
    ]._serialized_options = b"\202\323\344\223\002)\022'/dydxprotocol/prices/params/market/{id}"
    _globals["_QUERY"].methods_by_name["AllMarketParams"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "AllMarketParams"
    ]._serialized_options = b'\202\323\344\223\002$\022"/dydxprotocol/prices/params/market'
    _globals["_QUERY"].methods_by_name["NextMarketId"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "NextMarketId"
    ]._serialized_options = b"\202\323\344\223\002%\022#/dydxprotocol/prices/next_market_id"
    _globals["_QUERYMARKETPRICEREQUEST"]._serialized_start = 232
    _globals["_QUERYMARKETPRICEREQUEST"]._serialized_end = 269
    _globals["_QUERYMARKETPRICERESPONSE"]._serialized_start = 271
    _globals["_QUERYMARKETPRICERESPONSE"]._serialized_end = 359
    _globals["_QUERYALLMARKETPRICESREQUEST"]._serialized_start = 361
    _globals["_QUERYALLMARKETPRICESREQUEST"]._serialized_end = 450
    _globals["_QUERYALLMARKETPRICESRESPONSE"]._serialized_start = 453
    _globals["_QUERYALLMARKETPRICESRESPONSE"]._serialized_end = 607
    _globals["_QUERYMARKETPARAMREQUEST"]._serialized_start = 609
    _globals["_QUERYMARKETPARAMREQUEST"]._serialized_end = 646
    _globals["_QUERYMARKETPARAMRESPONSE"]._serialized_start = 648
    _globals["_QUERYMARKETPARAMRESPONSE"]._serialized_end = 736
    _globals["_QUERYALLMARKETPARAMSREQUEST"]._serialized_start = 738
    _globals["_QUERYALLMARKETPARAMSREQUEST"]._serialized_end = 827
    _globals["_QUERYALLMARKETPARAMSRESPONSE"]._serialized_start = 830
    _globals["_QUERYALLMARKETPARAMSRESPONSE"]._serialized_end = 984
    _globals["_QUERYNEXTMARKETIDREQUEST"]._serialized_start = 986
    _globals["_QUERYNEXTMARKETIDREQUEST"]._serialized_end = 1012
    _globals["_QUERYNEXTMARKETIDRESPONSE"]._serialized_start = 1014
    _globals["_QUERYNEXTMARKETIDRESPONSE"]._serialized_end = 1065
    _globals["_QUERY"]._serialized_start = 1068
    _globals["_QUERY"]._serialized_end = 1864
# @@protoc_insertion_point(module_scope)
