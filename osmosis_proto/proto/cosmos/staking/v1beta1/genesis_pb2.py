# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/staking/v1beta1/genesis.proto\x12\x16\x63osmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$cosmos/staking/v1beta1/staking.proto\"\xdd\x04\n\x0cGenesisState\x12\x34\n\x06params\x18\x01 \x01(\x0b\x32\x1e.cosmos.staking.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12\x63\n\x10last_total_power\x18\x02 \x01(\x0c\x42I\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:\"last_total_power\"\xc8\xde\x1f\x00\x12o\n\x15last_validator_powers\x18\x03 \x03(\x0b\x32*.cosmos.staking.v1beta1.LastValidatorPowerB$\xf2\xde\x1f\x1cyaml:\"last_validator_powers\"\xc8\xde\x1f\x00\x12;\n\nvalidators\x18\x04 \x03(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\x12=\n\x0b\x64\x65legations\x18\x05 \x03(\x0b\x32\".cosmos.staking.v1beta1.DelegationB\x04\xc8\xde\x1f\x00\x12p\n\x15unbonding_delegations\x18\x06 \x03(\x0b\x32+.cosmos.staking.v1beta1.UnbondingDelegationB$\xf2\xde\x1f\x1cyaml:\"unbonding_delegations\"\xc8\xde\x1f\x00\x12\x41\n\rredelegations\x18\x07 \x03(\x0b\x32$.cosmos.staking.v1beta1.RedelegationB\x04\xc8\xde\x1f\x00\x12\x10\n\x08\x65xported\x18\x08 \x01(\x08\">\n\x12LastValidatorPower\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\r\n\x05power\x18\x02 \x01(\x03:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['last_total_power']._options = None
  _GENESISSTATE.fields_by_name['last_total_power']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\027yaml:\"last_total_power\"\310\336\037\000'
  _GENESISSTATE.fields_by_name['last_validator_powers']._options = None
  _GENESISSTATE.fields_by_name['last_validator_powers']._serialized_options = b'\362\336\037\034yaml:\"last_validator_powers\"\310\336\037\000'
  _GENESISSTATE.fields_by_name['validators']._options = None
  _GENESISSTATE.fields_by_name['validators']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['delegations']._options = None
  _GENESISSTATE.fields_by_name['delegations']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['unbonding_delegations']._options = None
  _GENESISSTATE.fields_by_name['unbonding_delegations']._serialized_options = b'\362\336\037\034yaml:\"unbonding_delegations\"\310\336\037\000'
  _GENESISSTATE.fields_by_name['redelegations']._options = None
  _GENESISSTATE.fields_by_name['redelegations']._serialized_options = b'\310\336\037\000'
  _LASTVALIDATORPOWER._options = None
  _LASTVALIDATORPOWER._serialized_options = b'\350\240\037\000\210\240\037\000'
  _GENESISSTATE._serialized_start=125
  _GENESISSTATE._serialized_end=730
  _LASTVALIDATORPOWER._serialized_start=732
  _LASTVALIDATORPOWER._serialized_end=794
# @@protoc_insertion_point(module_scope)
