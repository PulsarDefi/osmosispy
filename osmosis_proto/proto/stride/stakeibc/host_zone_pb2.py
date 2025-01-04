# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: stride/stakeibc/host_zone.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stride.stakeibc import validator_pb2 as stride_dot_stakeibc_dot_validator__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1fstride/stakeibc/host_zone.proto\x12\x0fstride.stakeibc\x1a\x1fstride/stakeibc/validator.proto\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto"\xb1\x01\n\x13\x43ommunityPoolRebate\x12\x43\n\x0brebate_rate\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12U\n\x1dliquid_staked_st_token_amount\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int"\x9f\r\n\x08HostZone\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\x12\x14\n\x0c\x62\x65\x63h32prefix\x18\x11 \x01(\t\x12\x15\n\rconnection_id\x18\x02 \x01(\t\x12\x1b\n\x13transfer_channel_id\x18\x0c \x01(\t\x12\x11\n\tibc_denom\x18\x08 \x01(\t\x12\x12\n\nhost_denom\x18\t \x01(\t\x12\x18\n\x10unbonding_period\x18\x1a \x01(\x04\x12.\n\nvalidators\x18\x03 \x03(\x0b\x32\x1a.stride.stakeibc.Validator\x12\x31\n\x0f\x64\x65posit_address\x18\x12 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x38\n\x16withdrawal_ica_address\x18\x16 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x31\n\x0f\x66\x65\x65_ica_address\x18\x17 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x38\n\x16\x64\x65legation_ica_address\x18\x18 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x38\n\x16redemption_ica_address\x18\x19 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x44\n"community_pool_deposit_ica_address\x18\x1e \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x43\n!community_pool_return_ica_address\x18\x1f \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x46\n$community_pool_stake_holding_address\x18  \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12G\n%community_pool_redeem_holding_address\x18! \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x41\n\x1f\x63ommunity_pool_treasury_address\x18# \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12I\n\x11total_delegations\x18\r \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12Z\n\x14last_redemption_rate\x18\n \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12U\n\x0fredemption_rate\x18\x0b \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12Y\n\x13min_redemption_rate\x18\x14 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12Y\n\x13max_redemption_rate\x18\x15 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12_\n\x19min_inner_redemption_rate\x18\x1c \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12_\n\x19max_inner_redemption_rate\x18\x1d \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12\x1f\n\x17max_messages_per_ica_tx\x18$ \x01(\x04\x12\x1b\n\x13redemptions_enabled\x18% \x01(\x08\x12\x43\n\x15\x63ommunity_pool_rebate\x18" \x01(\x0b\x32$.stride.stakeibc.CommunityPoolRebate\x12 \n\x18lsm_liquid_stake_enabled\x18\x1b \x01(\x08\x12\x0e\n\x06halted\x18\x13 \x01(\x08J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\x0e\x10\x0fJ\x04\x08\x0f\x10\x10J\x04\x08\x10\x10\x11\x42\x34Z2github.com/Stride-Labs/stride/v24/x/stakeibc/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "stride.stakeibc.host_zone_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"Z2github.com/Stride-Labs/stride/v24/x/stakeibc/types"
    )
    _globals["_COMMUNITYPOOLREBATE"].fields_by_name[
        "rebate_rate"
    ]._loaded_options = None
    _globals["_COMMUNITYPOOLREBATE"].fields_by_name[
        "rebate_rate"
    ]._serialized_options = (
        b"\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec"
    )
    _globals["_COMMUNITYPOOLREBATE"].fields_by_name[
        "liquid_staked_st_token_amount"
    ]._loaded_options = None
    _globals["_COMMUNITYPOOLREBATE"].fields_by_name[
        "liquid_staked_st_token_amount"
    ]._serialized_options = (
        b"\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int"
    )
    _globals["_HOSTZONE"].fields_by_name["deposit_address"]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "deposit_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_HOSTZONE"].fields_by_name[
        "withdrawal_ica_address"
    ]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "withdrawal_ica_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_HOSTZONE"].fields_by_name["fee_ica_address"]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "fee_ica_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_HOSTZONE"].fields_by_name[
        "delegation_ica_address"
    ]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "delegation_ica_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_HOSTZONE"].fields_by_name[
        "redemption_ica_address"
    ]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "redemption_ica_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_HOSTZONE"].fields_by_name[
        "community_pool_deposit_ica_address"
    ]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "community_pool_deposit_ica_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_HOSTZONE"].fields_by_name[
        "community_pool_return_ica_address"
    ]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "community_pool_return_ica_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_HOSTZONE"].fields_by_name[
        "community_pool_stake_holding_address"
    ]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "community_pool_stake_holding_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_HOSTZONE"].fields_by_name[
        "community_pool_redeem_holding_address"
    ]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "community_pool_redeem_holding_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_HOSTZONE"].fields_by_name[
        "community_pool_treasury_address"
    ]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "community_pool_treasury_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_HOSTZONE"].fields_by_name["total_delegations"]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "total_delegations"
    ]._serialized_options = (
        b"\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int"
    )
    _globals["_HOSTZONE"].fields_by_name["last_redemption_rate"]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "last_redemption_rate"
    ]._serialized_options = b"\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec"
    _globals["_HOSTZONE"].fields_by_name["redemption_rate"]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "redemption_rate"
    ]._serialized_options = b"\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec"
    _globals["_HOSTZONE"].fields_by_name["min_redemption_rate"]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "min_redemption_rate"
    ]._serialized_options = b"\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec"
    _globals["_HOSTZONE"].fields_by_name["max_redemption_rate"]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "max_redemption_rate"
    ]._serialized_options = b"\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec"
    _globals["_HOSTZONE"].fields_by_name[
        "min_inner_redemption_rate"
    ]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "min_inner_redemption_rate"
    ]._serialized_options = b"\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec"
    _globals["_HOSTZONE"].fields_by_name[
        "max_inner_redemption_rate"
    ]._loaded_options = None
    _globals["_HOSTZONE"].fields_by_name[
        "max_inner_redemption_rate"
    ]._serialized_options = b"\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec"
    _globals["_COMMUNITYPOOLREBATE"]._serialized_start = 135
    _globals["_COMMUNITYPOOLREBATE"]._serialized_end = 312
    _globals["_HOSTZONE"]._serialized_start = 315
    _globals["_HOSTZONE"]._serialized_end = 2010
# @@protoc_insertion_point(module_scope)
