# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/bridge/genesis.proto
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
    'dydxprotocol/bridge/genesis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from dydxprotocol.bridge import bridge_event_info_pb2 as dydxprotocol_dot_bridge_dot_bridge__event__info__pb2
from dydxprotocol.bridge import params_pb2 as dydxprotocol_dot_bridge_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!dydxprotocol/bridge/genesis.proto\x12\x13\x64ydxprotocol.bridge\x1a\x14gogoproto/gogo.proto\x1a+dydxprotocol/bridge/bridge_event_info.proto\x1a dydxprotocol/bridge/params.proto\"\x9b\x02\n\x0cGenesisState\x12<\n\x0c\x65vent_params\x18\x01 \x01(\x0b\x32 .dydxprotocol.bridge.EventParamsB\x04\xc8\xde\x1f\x00\x12@\n\x0epropose_params\x18\x02 \x01(\x0b\x32\".dydxprotocol.bridge.ProposeParamsB\x04\xc8\xde\x1f\x00\x12>\n\rsafety_params\x18\x03 \x01(\x0b\x32!.dydxprotocol.bridge.SafetyParamsB\x04\xc8\xde\x1f\x00\x12K\n\x17\x61\x63knowledged_event_info\x18\x04 \x01(\x0b\x32$.dydxprotocol.bridge.BridgeEventInfoB\x04\xc8\xde\x1f\x00\x42:Z8github.com/dydxprotocol/v4-chain/protocol/x/bridge/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.bridge.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/dydxprotocol/v4-chain/protocol/x/bridge/types'
  _globals['_GENESISSTATE'].fields_by_name['event_params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['event_params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['propose_params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['propose_params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['safety_params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['safety_params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['acknowledged_event_info']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['acknowledged_event_info']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=160
  _globals['_GENESISSTATE']._serialized_end=443
# @@protoc_insertion_point(module_scope)
