# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/ratelimit/tx.proto
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
    'dydxprotocol/ratelimit/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from dydxprotocol.ratelimit import limit_params_pb2 as dydxprotocol_dot_ratelimit_dot_limit__params__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x64ydxprotocol/ratelimit/tx.proto\x12\x16\x64ydxprotocol.ratelimit\x1a\x17\x63osmos/msg/v1/msg.proto\x1a)dydxprotocol/ratelimit/limit_params.proto\x1a\x14gogoproto/gogo.proto\"w\n\x11MsgSetLimitParams\x12\x11\n\tauthority\x18\x01 \x01(\t\x12?\n\x0climit_params\x18\x02 \x01(\x0b\x32#.dydxprotocol.ratelimit.LimitParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x1b\n\x19MsgSetLimitParamsResponse2u\n\x03Msg\x12n\n\x0eSetLimitParams\x12).dydxprotocol.ratelimit.MsgSetLimitParams\x1a\x31.dydxprotocol.ratelimit.MsgSetLimitParamsResponseB=Z;github.com/dydxprotocol/v4-chain/protocol/x/ratelimit/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.ratelimit.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/dydxprotocol/v4-chain/protocol/x/ratelimit/types'
  _globals['_MSGSETLIMITPARAMS'].fields_by_name['limit_params']._loaded_options = None
  _globals['_MSGSETLIMITPARAMS'].fields_by_name['limit_params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGSETLIMITPARAMS']._loaded_options = None
  _globals['_MSGSETLIMITPARAMS']._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGSETLIMITPARAMS']._serialized_start=149
  _globals['_MSGSETLIMITPARAMS']._serialized_end=268
  _globals['_MSGSETLIMITPARAMSRESPONSE']._serialized_start=270
  _globals['_MSGSETLIMITPARAMSRESPONSE']._serialized_end=297
  _globals['_MSG']._serialized_start=299
  _globals['_MSG']._serialized_end=416
# @@protoc_insertion_point(module_scope)
