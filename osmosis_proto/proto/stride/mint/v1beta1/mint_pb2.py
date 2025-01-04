# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: stride/mint/v1beta1/mint.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1estride/mint/v1beta1/mint.proto\x12\x13stride.mint.v1beta1\x1a\x14gogoproto/gogo.proto"m\n\x06Minter\x12\x63\n\x10\x65poch_provisions\x18\x01 \x01(\tBI\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x17yaml:"epoch_provisions""\xa9\x03\n\x17\x44istributionProportions\x12Q\n\x07staking\x18\x01 \x01(\tB@\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0eyaml:"staking"\x12\x66\n\x15\x63ommunity_pool_growth\x18\x02 \x01(\tBG\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x15yaml:"community_pool"\x12o\n\x1e\x63ommunity_pool_security_budget\x18\x03 \x01(\tBG\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x15yaml:"community_pool"\x12\x62\n\x11strategic_reserve\x18\x04 \x01(\tBG\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x15yaml:"community_pool""\xbb\x04\n\x06Params\x12\x12\n\nmint_denom\x18\x01 \x01(\t\x12s\n\x18genesis_epoch_provisions\x18\x02 \x01(\tBQ\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x1fyaml:"genesis_epoch_provisions"\x12\x35\n\x10\x65poch_identifier\x18\x03 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"epoch_identifier"\x12I\n\x1areduction_period_in_epochs\x18\x04 \x01(\x03\x42%\xf2\xde\x1f!yaml:"reduction_period_in_epochs"\x12\x63\n\x10reduction_factor\x18\x05 \x01(\tBI\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x17yaml:"reduction_factor"\x12T\n\x18\x64istribution_proportions\x18\x06 \x01(\x0b\x32,.stride.mint.v1beta1.DistributionProportionsB\x04\xc8\xde\x1f\x00\x12\x65\n(minting_rewards_distribution_start_epoch\x18\x07 \x01(\x03\x42\x33\xf2\xde\x1f/yaml:"minting_rewards_distribution_start_epoch":\x04\x98\xa0\x1f\x00\x42\x30Z.github.com/Stride-Labs/stride/v24/x/mint/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "stride.mint.v1beta1.mint_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"Z.github.com/Stride-Labs/stride/v24/x/mint/types"
    )
    _globals["_MINTER"].fields_by_name["epoch_provisions"]._loaded_options = None
    _globals["_MINTER"].fields_by_name[
        "epoch_provisions"
    ]._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\027yaml:"epoch_provisions"'
    _globals["_DISTRIBUTIONPROPORTIONS"].fields_by_name[
        "staking"
    ]._loaded_options = None
    _globals["_DISTRIBUTIONPROPORTIONS"].fields_by_name[
        "staking"
    ]._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\016yaml:"staking"'
    _globals["_DISTRIBUTIONPROPORTIONS"].fields_by_name[
        "community_pool_growth"
    ]._loaded_options = None
    _globals["_DISTRIBUTIONPROPORTIONS"].fields_by_name[
        "community_pool_growth"
    ]._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\025yaml:"community_pool"'
    _globals["_DISTRIBUTIONPROPORTIONS"].fields_by_name[
        "community_pool_security_budget"
    ]._loaded_options = None
    _globals["_DISTRIBUTIONPROPORTIONS"].fields_by_name[
        "community_pool_security_budget"
    ]._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\025yaml:"community_pool"'
    _globals["_DISTRIBUTIONPROPORTIONS"].fields_by_name[
        "strategic_reserve"
    ]._loaded_options = None
    _globals["_DISTRIBUTIONPROPORTIONS"].fields_by_name[
        "strategic_reserve"
    ]._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\025yaml:"community_pool"'
    _globals["_PARAMS"].fields_by_name[
        "genesis_epoch_provisions"
    ]._loaded_options = None
    _globals["_PARAMS"].fields_by_name[
        "genesis_epoch_provisions"
    ]._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\037yaml:"genesis_epoch_provisions"'
    _globals["_PARAMS"].fields_by_name["epoch_identifier"]._loaded_options = None
    _globals["_PARAMS"].fields_by_name[
        "epoch_identifier"
    ]._serialized_options = b'\362\336\037\027yaml:"epoch_identifier"'
    _globals["_PARAMS"].fields_by_name[
        "reduction_period_in_epochs"
    ]._loaded_options = None
    _globals["_PARAMS"].fields_by_name[
        "reduction_period_in_epochs"
    ]._serialized_options = b'\362\336\037!yaml:"reduction_period_in_epochs"'
    _globals["_PARAMS"].fields_by_name["reduction_factor"]._loaded_options = None
    _globals["_PARAMS"].fields_by_name[
        "reduction_factor"
    ]._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\027yaml:"reduction_factor"'
    _globals["_PARAMS"].fields_by_name[
        "distribution_proportions"
    ]._loaded_options = None
    _globals["_PARAMS"].fields_by_name[
        "distribution_proportions"
    ]._serialized_options = b"\310\336\037\000"
    _globals["_PARAMS"].fields_by_name[
        "minting_rewards_distribution_start_epoch"
    ]._loaded_options = None
    _globals["_PARAMS"].fields_by_name[
        "minting_rewards_distribution_start_epoch"
    ]._serialized_options = (
        b'\362\336\037/yaml:"minting_rewards_distribution_start_epoch"'
    )
    _globals["_PARAMS"]._loaded_options = None
    _globals["_PARAMS"]._serialized_options = b"\230\240\037\000"
    _globals["_MINTER"]._serialized_start = 77
    _globals["_MINTER"]._serialized_end = 186
    _globals["_DISTRIBUTIONPROPORTIONS"]._serialized_start = 189
    _globals["_DISTRIBUTIONPROPORTIONS"]._serialized_end = 614
    _globals["_PARAMS"]._serialized_start = 617
    _globals["_PARAMS"]._serialized_end = 1188
# @@protoc_insertion_point(module_scope)
