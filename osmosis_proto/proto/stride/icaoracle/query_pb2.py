# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: stride/icaoracle/query.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stride.icaoracle import icaoracle_pb2 as stride_dot_icaoracle_dot_icaoracle__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cstride/icaoracle/query.proto\x12\x10stride.icaoracle\x1a stride/icaoracle/icaoracle.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x14gogoproto/gogo.proto"&\n\x12QueryOracleRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t"?\n\x13QueryOracleResponse\x12(\n\x06oracle\x18\x01 \x01(\x0b\x32\x18.stride.icaoracle.Oracle"\x18\n\x16QueryAllOraclesRequest"J\n\x17QueryAllOraclesResponse\x12/\n\x07oracles\x18\x01 \x03(\x0b\x32\x18.stride.icaoracle.OracleB\x04\xc8\xde\x1f\x00"+\n\x19QueryActiveOraclesRequest\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08"M\n\x1aQueryActiveOraclesResponse\x12/\n\x07oracles\x18\x01 \x03(\x0b\x32\x18.stride.icaoracle.OracleB\x04\xc8\xde\x1f\x00"B\n\x13QueryMetricsRequest\x12\x12\n\nmetric_key\x18\x01 \x01(\t\x12\x17\n\x0foracle_chain_id\x18\x02 \x01(\t"G\n\x14QueryMetricsResponse\x12/\n\x07metrics\x18\x01 \x03(\x0b\x32\x18.stride.icaoracle.MetricB\x04\xc8\xde\x1f\x00\x32\xdb\x04\n\x05Query\x12\x8e\x01\n\x06Oracle\x12$.stride.icaoracle.QueryOracleRequest\x1a%.stride.icaoracle.QueryOracleResponse"7\x82\xd3\xe4\x93\x02\x31\x12//Stride-Labs/stride/icaoracle/oracle/{chain_id}\x12\x90\x01\n\nAllOracles\x12(.stride.icaoracle.QueryAllOraclesRequest\x1a).stride.icaoracle.QueryAllOraclesResponse"-\x82\xd3\xe4\x93\x02\'\x12%/Stride-Labs/stride/icaoracle/oracles\x12\xa3\x01\n\rActiveOracles\x12+.stride.icaoracle.QueryActiveOraclesRequest\x1a,.stride.icaoracle.QueryActiveOraclesResponse"7\x82\xd3\xe4\x93\x02\x31\x12//Stride-Labs/stride/icaoracle/oracles/by_active\x12\x87\x01\n\x07Metrics\x12%.stride.icaoracle.QueryMetricsRequest\x1a&.stride.icaoracle.QueryMetricsResponse"-\x82\xd3\xe4\x93\x02\'\x12%/Stride-Labs/stride/icaoracle/metricsB5Z3github.com/Stride-Labs/stride/v24/x/icaoracle/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "stride.icaoracle.query_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"Z3github.com/Stride-Labs/stride/v24/x/icaoracle/types"
    )
    _globals["_QUERYALLORACLESRESPONSE"].fields_by_name[
        "oracles"
    ]._loaded_options = None
    _globals["_QUERYALLORACLESRESPONSE"].fields_by_name[
        "oracles"
    ]._serialized_options = b"\310\336\037\000"
    _globals["_QUERYACTIVEORACLESRESPONSE"].fields_by_name[
        "oracles"
    ]._loaded_options = None
    _globals["_QUERYACTIVEORACLESRESPONSE"].fields_by_name[
        "oracles"
    ]._serialized_options = b"\310\336\037\000"
    _globals["_QUERYMETRICSRESPONSE"].fields_by_name["metrics"]._loaded_options = None
    _globals["_QUERYMETRICSRESPONSE"].fields_by_name[
        "metrics"
    ]._serialized_options = b"\310\336\037\000"
    _globals["_QUERY"].methods_by_name["Oracle"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "Oracle"
    ]._serialized_options = (
        b"\202\323\344\223\0021\022//Stride-Labs/stride/icaoracle/oracle/{chain_id}"
    )
    _globals["_QUERY"].methods_by_name["AllOracles"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "AllOracles"
    ]._serialized_options = (
        b"\202\323\344\223\002'\022%/Stride-Labs/stride/icaoracle/oracles"
    )
    _globals["_QUERY"].methods_by_name["ActiveOracles"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "ActiveOracles"
    ]._serialized_options = (
        b"\202\323\344\223\0021\022//Stride-Labs/stride/icaoracle/oracles/by_active"
    )
    _globals["_QUERY"].methods_by_name["Metrics"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "Metrics"
    ]._serialized_options = (
        b"\202\323\344\223\002'\022%/Stride-Labs/stride/icaoracle/metrics"
    )
    _globals["_QUERYORACLEREQUEST"]._serialized_start = 136
    _globals["_QUERYORACLEREQUEST"]._serialized_end = 174
    _globals["_QUERYORACLERESPONSE"]._serialized_start = 176
    _globals["_QUERYORACLERESPONSE"]._serialized_end = 239
    _globals["_QUERYALLORACLESREQUEST"]._serialized_start = 241
    _globals["_QUERYALLORACLESREQUEST"]._serialized_end = 265
    _globals["_QUERYALLORACLESRESPONSE"]._serialized_start = 267
    _globals["_QUERYALLORACLESRESPONSE"]._serialized_end = 341
    _globals["_QUERYACTIVEORACLESREQUEST"]._serialized_start = 343
    _globals["_QUERYACTIVEORACLESREQUEST"]._serialized_end = 386
    _globals["_QUERYACTIVEORACLESRESPONSE"]._serialized_start = 388
    _globals["_QUERYACTIVEORACLESRESPONSE"]._serialized_end = 465
    _globals["_QUERYMETRICSREQUEST"]._serialized_start = 467
    _globals["_QUERYMETRICSREQUEST"]._serialized_end = 533
    _globals["_QUERYMETRICSRESPONSE"]._serialized_start = 535
    _globals["_QUERYMETRICSRESPONSE"]._serialized_end = 606
    _globals["_QUERY"]._serialized_start = 609
    _globals["_QUERY"]._serialized_end = 1212
# @@protoc_insertion_point(module_scope)
