# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/sumtree/v1beta1/tree.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"osmosis/sumtree/v1beta1/tree.proto\x12\x15osmosis.store.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"6\n\x04Node\x12.\n\x08\x63hildren\x18\x01 \x03(\x0b\x32\x1c.osmosis.store.v1beta1.Child\"\\\n\x05\x43hild\x12\r\n\x05index\x18\x01 \x01(\x0c\x12\x44\n\x0c\x61\x63\x63umulation\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\"2\n\x04Leaf\x12*\n\x04leaf\x18\x01 \x01(\x0b\x32\x1c.osmosis.store.v1beta1.ChildB3Z1github.com/osmosis-labs/osmosis/osmoutils/sumtreeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.sumtree.v1beta1.tree_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/osmosis-labs/osmosis/osmoutils/sumtree'
  _CHILD.fields_by_name['accumulation']._options = None
  _CHILD.fields_by_name['accumulation']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _NODE._serialized_start=115
  _NODE._serialized_end=169
  _CHILD._serialized_start=171
  _CHILD._serialized_end=263
  _LEAF._serialized_start=265
  _LEAF._serialized_end=315
# @@protoc_insertion_point(module_scope)
