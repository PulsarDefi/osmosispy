# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/tx/v1beta1/service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()



from cosmos.base.abci.v1beta1 import abci_pb2 as cosmos_dot_base_dot_abci_dot_v1beta1_dot_abci__pb2
from cosmos.tx.v1beta1 import tx_pb2 as cosmos_dot_tx_dot_v1beta1_dot_tx__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/tx/v1beta1/service.proto\x12\x11\x63osmos.tx.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a#cosmos/base/abci/v1beta1/abci.proto\x1a\x1a\x63osmos/tx/v1beta1/tx.proto\x1a\x14gogoproto/gogo.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\"\x8e\x01\n\x12GetTxsEventRequest\x12\x0e\n\x06\x65vents\x18\x01 \x03(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x12,\n\x08order_by\x18\x03 \x01(\x0e\x32\x1a.cosmos.tx.v1beta1.OrderBy\"\xb2\x01\n\x13GetTxsEventResponse\x12\"\n\x03txs\x18\x01 \x03(\x0b\x32\x15.cosmos.tx.v1beta1.Tx\x12:\n\x0ctx_responses\x18\x02 \x03(\x0b\x32$.cosmos.base.abci.v1beta1.TxResponse\x12;\n\npagination\x18\x03 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"V\n\x12\x42roadcastTxRequest\x12\x10\n\x08tx_bytes\x18\x01 \x01(\x0c\x12.\n\x04mode\x18\x02 \x01(\x0e\x32 .cosmos.tx.v1beta1.BroadcastMode\"P\n\x13\x42roadcastTxResponse\x12\x39\n\x0btx_response\x18\x01 \x01(\x0b\x32$.cosmos.base.abci.v1beta1.TxResponse\"J\n\x0fSimulateRequest\x12%\n\x02tx\x18\x01 \x01(\x0b\x32\x15.cosmos.tx.v1beta1.TxB\x02\x18\x01\x12\x10\n\x08tx_bytes\x18\x02 \x01(\x0c\"y\n\x10SimulateResponse\x12\x33\n\x08gas_info\x18\x01 \x01(\x0b\x32!.cosmos.base.abci.v1beta1.GasInfo\x12\x30\n\x06result\x18\x02 \x01(\x0b\x32 .cosmos.base.abci.v1beta1.Result\"\x1c\n\x0cGetTxRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\"m\n\rGetTxResponse\x12!\n\x02tx\x18\x01 \x01(\x0b\x32\x15.cosmos.tx.v1beta1.Tx\x12\x39\n\x0btx_response\x18\x02 \x01(\x0b\x32$.cosmos.base.abci.v1beta1.TxResponse*H\n\x07OrderBy\x12\x18\n\x14ORDER_BY_UNSPECIFIED\x10\x00\x12\x10\n\x0cORDER_BY_ASC\x10\x01\x12\x11\n\rORDER_BY_DESC\x10\x02*|\n\rBroadcastMode\x12\x1e\n\x1a\x42ROADCAST_MODE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x42ROADCAST_MODE_BLOCK\x10\x01\x12\x17\n\x13\x42ROADCAST_MODE_SYNC\x10\x02\x12\x18\n\x14\x42ROADCAST_MODE_ASYNC\x10\x03\x32\xf8\x03\n\x07Service\x12{\n\x08Simulate\x12\".cosmos.tx.v1beta1.SimulateRequest\x1a#.cosmos.tx.v1beta1.SimulateResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/cosmos/tx/v1beta1/simulate:\x01*\x12q\n\x05GetTx\x12\x1f.cosmos.tx.v1beta1.GetTxRequest\x1a .cosmos.tx.v1beta1.GetTxResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/tx/v1beta1/txs/{hash}\x12\x7f\n\x0b\x42roadcastTx\x12%.cosmos.tx.v1beta1.BroadcastTxRequest\x1a&.cosmos.tx.v1beta1.BroadcastTxResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/cosmos/tx/v1beta1/txs:\x01*\x12|\n\x0bGetTxsEvent\x12%.cosmos.tx.v1beta1.GetTxsEventRequest\x1a&.cosmos.tx.v1beta1.GetTxsEventResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/cosmos/tx/v1beta1/txsB+Z%github.com/cosmos/cosmos-sdk/types/tx\xc0\xe3\x1e\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.tx.v1beta1.service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z%github.com/cosmos/cosmos-sdk/types/tx\300\343\036\001'
  _SIMULATEREQUEST.fields_by_name['tx']._options = None
  _SIMULATEREQUEST.fields_by_name['tx']._serialized_options = b'\030\001'
  _SERVICE.methods_by_name['Simulate']._options = None
  _SERVICE.methods_by_name['Simulate']._serialized_options = b'\202\323\344\223\002 \"\033/cosmos/tx/v1beta1/simulate:\001*'
  _SERVICE.methods_by_name['GetTx']._options = None
  _SERVICE.methods_by_name['GetTx']._serialized_options = b'\202\323\344\223\002\037\022\035/cosmos/tx/v1beta1/txs/{hash}'
  _SERVICE.methods_by_name['BroadcastTx']._options = None
  _SERVICE.methods_by_name['BroadcastTx']._serialized_options = b'\202\323\344\223\002\033\"\026/cosmos/tx/v1beta1/txs:\001*'
  _SERVICE.methods_by_name['GetTxsEvent']._options = None
  _SERVICE.methods_by_name['GetTxsEvent']._serialized_options = b'\202\323\344\223\002\030\022\026/cosmos/tx/v1beta1/txs'
  _ORDERBY._serialized_start=1051
  _ORDERBY._serialized_end=1123
  _BROADCASTMODE._serialized_start=1125
  _BROADCASTMODE._serialized_end=1249
  _GETTXSEVENTREQUEST._serialized_start=216
  _GETTXSEVENTREQUEST._serialized_end=358
  _GETTXSEVENTRESPONSE._serialized_start=361
  _GETTXSEVENTRESPONSE._serialized_end=539
  _BROADCASTTXREQUEST._serialized_start=541
  _BROADCASTTXREQUEST._serialized_end=627
  _BROADCASTTXRESPONSE._serialized_start=629
  _BROADCASTTXRESPONSE._serialized_end=709
  _SIMULATEREQUEST._serialized_start=711
  _SIMULATEREQUEST._serialized_end=785
  _SIMULATERESPONSE._serialized_start=787
  _SIMULATERESPONSE._serialized_end=908
  _GETTXREQUEST._serialized_start=910
  _GETTXREQUEST._serialized_end=938
  _GETTXRESPONSE._serialized_start=940
  _GETTXRESPONSE._serialized_end=1049
  _SERVICE._serialized_start=1252
  _SERVICE._serialized_end=1756
# @@protoc_insertion_point(module_scope)
