# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/daemons/bridge/bridge.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from dydxprotocol.bridge import bridge_event_pb2 as dydxprotocol_dot_bridge_dot_bridge__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n(dydxprotocol/daemons/bridge/bridge.proto\x12\x1b\x64ydxprotocol.daemons.bridge\x1a\x14gogoproto/gogo.proto\x1a&dydxprotocol/bridge/bridge_event.proto"W\n\x16\x41\x64\x64\x42ridgeEventsRequest\x12=\n\rbridge_events\x18\x01 \x03(\x0b\x32 .dydxprotocol.bridge.BridgeEventB\x04\xc8\xde\x1f\x00"\x19\n\x17\x41\x64\x64\x42ridgeEventsResponse2\x8d\x01\n\rBridgeService\x12|\n\x0f\x41\x64\x64\x42ridgeEvents\x12\x33.dydxprotocol.daemons.bridge.AddBridgeEventsRequest\x1a\x34.dydxprotocol.daemons.bridge.AddBridgeEventsResponseB>Z<github.com/dydxprotocol/v4-chain/protocol/daemons/bridge/apib\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.daemons.bridge.bridge_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z<github.com/dydxprotocol/v4-chain/protocol/daemons/bridge/api"
    _globals["_ADDBRIDGEEVENTSREQUEST"].fields_by_name["bridge_events"]._loaded_options = None
    _globals["_ADDBRIDGEEVENTSREQUEST"].fields_by_name["bridge_events"]._serialized_options = b"\310\336\037\000"
    _globals["_ADDBRIDGEEVENTSREQUEST"]._serialized_start = 135
    _globals["_ADDBRIDGEEVENTSREQUEST"]._serialized_end = 222
    _globals["_ADDBRIDGEEVENTSRESPONSE"]._serialized_start = 224
    _globals["_ADDBRIDGEEVENTSRESPONSE"]._serialized_end = 249
    _globals["_BRIDGESERVICE"]._serialized_start = 252
    _globals["_BRIDGESERVICE"]._serialized_end = 393
# @@protoc_insertion_point(module_scope)
