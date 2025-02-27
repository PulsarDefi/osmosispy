# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/blocktime/query.proto
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
from dydxprotocol.blocktime import blocktime_pb2 as dydxprotocol_dot_blocktime_dot_blocktime__pb2
from dydxprotocol.blocktime import params_pb2 as dydxprotocol_dot_blocktime_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n"dydxprotocol/blocktime/query.proto\x12\x16\x64ydxprotocol.blocktime\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a&dydxprotocol/blocktime/blocktime.proto\x1a#dydxprotocol/blocktime/params.proto"\x1d\n\x1bQuerySynchronyParamsRequest"]\n\x1cQuerySynchronyParamsResponse\x12=\n\x06params\x18\x01 \x01(\x0b\x32\'.dydxprotocol.blocktime.SynchronyParamsB\x04\xc8\xde\x1f\x00"\x1c\n\x1aQueryDowntimeParamsRequest"[\n\x1bQueryDowntimeParamsResponse\x12<\n\x06params\x18\x01 \x01(\x0b\x32&.dydxprotocol.blocktime.DowntimeParamsB\x04\xc8\xde\x1f\x00"\x1f\n\x1dQueryPreviousBlockInfoRequest"Q\n\x1eQueryPreviousBlockInfoResponse\x12/\n\x04info\x18\x01 \x01(\x0b\x32!.dydxprotocol.blocktime.BlockInfo"\x1d\n\x1bQueryAllDowntimeInfoRequest"U\n\x1cQueryAllDowntimeInfoResponse\x12\x35\n\x04info\x18\x01 \x01(\x0b\x32\'.dydxprotocol.blocktime.AllDowntimeInfo2\xa5\x05\n\x05Query\x12\xad\x01\n\x0e\x44owntimeParams\x12\x32.dydxprotocol.blocktime.QueryDowntimeParamsRequest\x1a\x33.dydxprotocol.blocktime.QueryDowntimeParamsResponse"2\x82\xd3\xe4\x93\x02,\x12*/dydxprotocol/v4/blocktime/downtime_params\x12\x82\x01\n\x11PreviousBlockInfo\x12\x35.dydxprotocol.blocktime.QueryPreviousBlockInfoRequest\x1a\x36.dydxprotocol.blocktime.QueryPreviousBlockInfoResponse\x12\xb2\x01\n\x0f\x41llDowntimeInfo\x12\x33.dydxprotocol.blocktime.QueryAllDowntimeInfoRequest\x1a\x34.dydxprotocol.blocktime.QueryAllDowntimeInfoResponse"4\x82\xd3\xe4\x93\x02.\x12,/dydxprotocol/v4/blocktime/all_downtime_info\x12\xb1\x01\n\x0fSynchronyParams\x12\x33.dydxprotocol.blocktime.QuerySynchronyParamsRequest\x1a\x34.dydxprotocol.blocktime.QuerySynchronyParamsResponse"3\x82\xd3\xe4\x93\x02-\x12+/dydxprotocol/v4/blocktime/synchrony_paramsB=Z;github.com/dydxprotocol/v4-chain/protocol/x/blocktime/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.blocktime.query_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z;github.com/dydxprotocol/v4-chain/protocol/x/blocktime/types"
    _globals["_QUERYSYNCHRONYPARAMSRESPONSE"].fields_by_name["params"]._loaded_options = None
    _globals["_QUERYSYNCHRONYPARAMSRESPONSE"].fields_by_name["params"]._serialized_options = b"\310\336\037\000"
    _globals["_QUERYDOWNTIMEPARAMSRESPONSE"].fields_by_name["params"]._loaded_options = None
    _globals["_QUERYDOWNTIMEPARAMSRESPONSE"].fields_by_name["params"]._serialized_options = b"\310\336\037\000"
    _globals["_QUERY"].methods_by_name["DowntimeParams"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "DowntimeParams"
    ]._serialized_options = b"\202\323\344\223\002,\022*/dydxprotocol/v4/blocktime/downtime_params"
    _globals["_QUERY"].methods_by_name["AllDowntimeInfo"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "AllDowntimeInfo"
    ]._serialized_options = b"\202\323\344\223\002.\022,/dydxprotocol/v4/blocktime/all_downtime_info"
    _globals["_QUERY"].methods_by_name["SynchronyParams"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "SynchronyParams"
    ]._serialized_options = b"\202\323\344\223\002-\022+/dydxprotocol/v4/blocktime/synchrony_params"
    _globals["_QUERYSYNCHRONYPARAMSREQUEST"]._serialized_start = 191
    _globals["_QUERYSYNCHRONYPARAMSREQUEST"]._serialized_end = 220
    _globals["_QUERYSYNCHRONYPARAMSRESPONSE"]._serialized_start = 222
    _globals["_QUERYSYNCHRONYPARAMSRESPONSE"]._serialized_end = 315
    _globals["_QUERYDOWNTIMEPARAMSREQUEST"]._serialized_start = 317
    _globals["_QUERYDOWNTIMEPARAMSREQUEST"]._serialized_end = 345
    _globals["_QUERYDOWNTIMEPARAMSRESPONSE"]._serialized_start = 347
    _globals["_QUERYDOWNTIMEPARAMSRESPONSE"]._serialized_end = 438
    _globals["_QUERYPREVIOUSBLOCKINFOREQUEST"]._serialized_start = 440
    _globals["_QUERYPREVIOUSBLOCKINFOREQUEST"]._serialized_end = 471
    _globals["_QUERYPREVIOUSBLOCKINFORESPONSE"]._serialized_start = 473
    _globals["_QUERYPREVIOUSBLOCKINFORESPONSE"]._serialized_end = 554
    _globals["_QUERYALLDOWNTIMEINFOREQUEST"]._serialized_start = 556
    _globals["_QUERYALLDOWNTIMEINFOREQUEST"]._serialized_end = 585
    _globals["_QUERYALLDOWNTIMEINFORESPONSE"]._serialized_start = 587
    _globals["_QUERYALLDOWNTIMEINFORESPONSE"]._serialized_end = 672
    _globals["_QUERY"]._serialized_start = 675
    _globals["_QUERY"]._serialized_end = 1352
# @@protoc_insertion_point(module_scope)
