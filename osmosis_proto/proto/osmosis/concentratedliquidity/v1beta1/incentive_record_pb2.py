# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: osmosis/concentratedliquidity/v1beta1/incentive_record.proto
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
    'osmosis/concentratedliquidity/v1beta1/incentive_record.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<osmosis/concentratedliquidity/v1beta1/incentive_record.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xa0\x02\n\x0fIncentiveRecord\x12-\n\x0cincentive_id\x18\x01 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"incentive_id\"\x12\x0f\n\x07pool_id\x18\x02 \x01(\x04\x12\x7f\n\x15incentive_record_body\x18\x04 \x01(\x0b\x32:.osmosis.concentratedliquidity.v1beta1.IncentiveRecordBodyB$\xc8\xde\x1f\x00\xf2\xde\x1f\x1cyaml:\"incentive_record_body\"\x12L\n\nmin_uptime\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:\"min_uptime\"\x98\xdf\x1f\x01\"\xbd\x02\n\x13IncentiveRecordBody\x12\x82\x01\n\x0eremaining_coin\x18\x01 \x01(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinBL\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:\"remaining_coins\"\xaa\xdf\x1f*github.com/cosmos/cosmos-sdk/types.DecCoin\x12R\n\remission_rate\x18\x02 \x01(\tB;\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xf2\xde\x1f\x14yaml:\"emission_rate\"\x12M\n\nstart_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:\"start_time\"\x90\xdf\x1f\x01\x42\x44ZBgithub.com/osmosis-labs/osmosis/v25/x/concentrated-liquidity/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentratedliquidity.v1beta1.incentive_record_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v25/x/concentrated-liquidity/types'
  _globals['_INCENTIVERECORD'].fields_by_name['incentive_id']._loaded_options = None
  _globals['_INCENTIVERECORD'].fields_by_name['incentive_id']._serialized_options = b'\362\336\037\023yaml:\"incentive_id\"'
  _globals['_INCENTIVERECORD'].fields_by_name['incentive_record_body']._loaded_options = None
  _globals['_INCENTIVERECORD'].fields_by_name['incentive_record_body']._serialized_options = b'\310\336\037\000\362\336\037\034yaml:\"incentive_record_body\"'
  _globals['_INCENTIVERECORD'].fields_by_name['min_uptime']._loaded_options = None
  _globals['_INCENTIVERECORD'].fields_by_name['min_uptime']._serialized_options = b'\310\336\037\000\362\336\037\021yaml:\"min_uptime\"\230\337\037\001'
  _globals['_INCENTIVERECORDBODY'].fields_by_name['remaining_coin']._loaded_options = None
  _globals['_INCENTIVERECORDBODY'].fields_by_name['remaining_coin']._serialized_options = b'\310\336\037\000\362\336\037\026yaml:\"remaining_coins\"\252\337\037*github.com/cosmos/cosmos-sdk/types.DecCoin'
  _globals['_INCENTIVERECORDBODY'].fields_by_name['emission_rate']._loaded_options = None
  _globals['_INCENTIVERECORDBODY'].fields_by_name['emission_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\362\336\037\024yaml:\"emission_rate\"'
  _globals['_INCENTIVERECORDBODY'].fields_by_name['start_time']._loaded_options = None
  _globals['_INCENTIVERECORDBODY'].fields_by_name['start_time']._serialized_options = b'\310\336\037\000\362\336\037\021yaml:\"start_time\"\220\337\037\001'
  _globals['_INCENTIVERECORD']._serialized_start=223
  _globals['_INCENTIVERECORD']._serialized_end=511
  _globals['_INCENTIVERECORDBODY']._serialized_start=514
  _globals['_INCENTIVERECORDBODY']._serialized_end=831
# @@protoc_insertion_point(module_scope)
