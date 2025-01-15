# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/indexer/protocol/v1/clob.proto
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
    'dydxprotocol/indexer/protocol/v1/clob.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dydxprotocol.indexer.protocol.v1 import subaccount_pb2 as dydxprotocol_dot_indexer_dot_protocol_dot_v1_dot_subaccount__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+dydxprotocol/indexer/protocol/v1/clob.proto\x12 dydxprotocol.indexer.protocol.v1\x1a\x31\x64ydxprotocol/indexer/protocol/v1/subaccount.proto\x1a\x14gogoproto/gogo.proto\"\xa2\x01\n\x0eIndexerOrderId\x12R\n\rsubaccount_id\x18\x01 \x01(\x0b\x32\x35.dydxprotocol.indexer.protocol.v1.IndexerSubaccountIdB\x04\xc8\xde\x1f\x00\x12\x11\n\tclient_id\x18\x02 \x01(\x07\x12\x13\n\x0border_flags\x18\x03 \x01(\r\x12\x14\n\x0c\x63lob_pair_id\x18\x04 \x01(\r\"\xba\x06\n\x0cIndexerOrder\x12H\n\x08order_id\x18\x01 \x01(\x0b\x32\x30.dydxprotocol.indexer.protocol.v1.IndexerOrderIdB\x04\xc8\xde\x1f\x00\x12\x41\n\x04side\x18\x02 \x01(\x0e\x32\x33.dydxprotocol.indexer.protocol.v1.IndexerOrder.Side\x12\x10\n\x08quantums\x18\x03 \x01(\x04\x12\x10\n\x08subticks\x18\x04 \x01(\x04\x12\x18\n\x0egood_til_block\x18\x05 \x01(\rH\x00\x12\x1d\n\x13good_til_block_time\x18\x06 \x01(\x07H\x00\x12Q\n\rtime_in_force\x18\x07 \x01(\x0e\x32:.dydxprotocol.indexer.protocol.v1.IndexerOrder.TimeInForce\x12\x13\n\x0breduce_only\x18\x08 \x01(\x08\x12\x17\n\x0f\x63lient_metadata\x18\t \x01(\r\x12T\n\x0e\x63ondition_type\x18\n \x01(\x0e\x32<.dydxprotocol.indexer.protocol.v1.IndexerOrder.ConditionType\x12*\n\"conditional_order_trigger_subticks\x18\x0b \x01(\x04\"9\n\x04Side\x12\x14\n\x10SIDE_UNSPECIFIED\x10\x00\x12\x0c\n\x08SIDE_BUY\x10\x01\x12\r\n\tSIDE_SELL\x10\x02\"\x80\x01\n\x0bTimeInForce\x12\x1d\n\x19TIME_IN_FORCE_UNSPECIFIED\x10\x00\x12\x15\n\x11TIME_IN_FORCE_IOC\x10\x01\x12\x1b\n\x17TIME_IN_FORCE_POST_ONLY\x10\x02\x12\x1e\n\x1aTIME_IN_FORCE_FILL_OR_KILL\x10\x03\"m\n\rConditionType\x12\x1e\n\x1a\x43ONDITION_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x43ONDITION_TYPE_STOP_LOSS\x10\x01\x12\x1e\n\x1a\x43ONDITION_TYPE_TAKE_PROFIT\x10\x02\x42\x10\n\x0egood_til_oneof*\xf8\x01\n\x0e\x43lobPairStatus\x12 \n\x1c\x43LOB_PAIR_STATUS_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x43LOB_PAIR_STATUS_ACTIVE\x10\x01\x12\x1b\n\x17\x43LOB_PAIR_STATUS_PAUSED\x10\x02\x12 \n\x1c\x43LOB_PAIR_STATUS_CANCEL_ONLY\x10\x03\x12\x1e\n\x1a\x43LOB_PAIR_STATUS_POST_ONLY\x10\x04\x12!\n\x1d\x43LOB_PAIR_STATUS_INITIALIZING\x10\x05\x12%\n!CLOB_PAIR_STATUS_FINAL_SETTLEMENT\x10\x06\x42\x45ZCgithub.com/dydxprotocol/v4-chain/protocol/indexer/protocol/v1/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.indexer.protocol.v1.clob_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZCgithub.com/dydxprotocol/v4-chain/protocol/indexer/protocol/v1/types'
  _globals['_INDEXERORDERID'].fields_by_name['subaccount_id']._loaded_options = None
  _globals['_INDEXERORDERID'].fields_by_name['subaccount_id']._serialized_options = b'\310\336\037\000'
  _globals['_INDEXERORDER'].fields_by_name['order_id']._loaded_options = None
  _globals['_INDEXERORDER'].fields_by_name['order_id']._serialized_options = b'\310\336\037\000'
  _globals['_CLOBPAIRSTATUS']._serialized_start=1149
  _globals['_CLOBPAIRSTATUS']._serialized_end=1397
  _globals['_INDEXERORDERID']._serialized_start=155
  _globals['_INDEXERORDERID']._serialized_end=317
  _globals['_INDEXERORDER']._serialized_start=320
  _globals['_INDEXERORDER']._serialized_end=1146
  _globals['_INDEXERORDER_SIDE']._serialized_start=829
  _globals['_INDEXERORDER_SIDE']._serialized_end=886
  _globals['_INDEXERORDER_TIMEINFORCE']._serialized_start=889
  _globals['_INDEXERORDER_TIMEINFORCE']._serialized_end=1017
  _globals['_INDEXERORDER_CONDITIONTYPE']._serialized_start=1019
  _globals['_INDEXERORDER_CONDITIONTYPE']._serialized_end=1128
# @@protoc_insertion_point(module_scope)
