# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: osmosis/concentratedliquidity/v1beta1/position.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n4osmosis/concentratedliquidity/v1beta1/position.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19osmosis/lockup/lock.proto\"\xc2\x02\n\x08Position\x12+\n\x0bposition_id\x18\x01 \x01(\x04\x42\x16\xf2\xde\x1f\x12yaml:\"position_id\"\x12#\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"address\"\x12#\n\x07pool_id\x18\x03 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\x12\x12\n\nlower_tick\x18\x04 \x01(\x03\x12\x12\n\nupper_tick\x18\x05 \x01(\x03\x12K\n\tjoin_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"join_time\"\x90\xdf\x1f\x01\x12J\n\tliquidity\x18\x07 \x01(\tB7\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xf2\xde\x1f\x10yaml:\"liquidity\"\"\xba\x04\n\x15\x46ullPositionBreakdown\x12G\n\x08position\x18\x01 \x01(\x0b\x32/.osmosis.concentratedliquidity.v1beta1.PositionB\x04\xc8\xde\x1f\x00\x12Z\n\x06\x61sset0\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB/\xc8\xde\x1f\x00\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\x12Z\n\x06\x61sset1\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB/\xc8\xde\x1f\x00\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\x12\x64\n\x18\x63laimable_spread_rewards\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:\"claimable_spread_rewards\"\x12\\\n\x14\x63laimable_incentives\x18\x05 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB#\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:\"claimable_incentives\"\x12\\\n\x14\x66orfeited_incentives\x18\x06 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB#\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:\"forfeited_incentives\"\"\x92\x01\n\x16PositionWithPeriodLock\x12G\n\x08position\x18\x01 \x01(\x0b\x32/.osmosis.concentratedliquidity.v1beta1.PositionB\x04\xc8\xde\x1f\x00\x12/\n\x05locks\x18\x02 \x01(\x0b\x32\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00\x42\x44ZBgithub.com/osmosis-labs/osmosis/v25/x/concentrated-liquidity/modelb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentratedliquidity.v1beta1.position_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v25/x/concentrated-liquidity/model'
    _globals['_POSITION'].fields_by_name['position_id']._loaded_options = None
    _globals['_POSITION'].fields_by_name['position_id']._serialized_options = b'\362\336\037\022yaml:\"position_id\"'
    _globals['_POSITION'].fields_by_name['address']._loaded_options = None
    _globals['_POSITION'].fields_by_name['address']._serialized_options = b'\362\336\037\016yaml:\"address\"'
    _globals['_POSITION'].fields_by_name['pool_id']._loaded_options = None
    _globals['_POSITION'].fields_by_name['pool_id']._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _globals['_POSITION'].fields_by_name['join_time']._loaded_options = None
    _globals['_POSITION'].fields_by_name[
        'join_time'
    ]._serialized_options = b'\310\336\037\000\362\336\037\020yaml:\"join_time\"\220\337\037\001'
    _globals['_POSITION'].fields_by_name['liquidity']._loaded_options = None
    _globals['_POSITION'].fields_by_name[
        'liquidity'
    ]._serialized_options = (
        b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\362\336\037\020yaml:\"liquidity\"'
    )
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name['position']._loaded_options = None
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name['position']._serialized_options = b'\310\336\037\000'
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name['asset0']._loaded_options = None
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name[
        'asset0'
    ]._serialized_options = b'\310\336\037\000\252\337\037\'github.com/cosmos/cosmos-sdk/types.Coin'
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name['asset1']._loaded_options = None
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name[
        'asset1'
    ]._serialized_options = b'\310\336\037\000\252\337\037\'github.com/cosmos/cosmos-sdk/types.Coin'
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name['claimable_spread_rewards']._loaded_options = None
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name[
        'claimable_spread_rewards'
    ]._serialized_options = b'\310\336\037\000\362\336\037\037yaml:\"claimable_spread_rewards\"'
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name['claimable_incentives']._loaded_options = None
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name[
        'claimable_incentives'
    ]._serialized_options = b'\310\336\037\000\362\336\037\033yaml:\"claimable_incentives\"'
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name['forfeited_incentives']._loaded_options = None
    _globals['_FULLPOSITIONBREAKDOWN'].fields_by_name[
        'forfeited_incentives'
    ]._serialized_options = b'\310\336\037\000\362\336\037\033yaml:\"forfeited_incentives\"'
    _globals['_POSITIONWITHPERIODLOCK'].fields_by_name['position']._loaded_options = None
    _globals['_POSITIONWITHPERIODLOCK'].fields_by_name['position']._serialized_options = b'\310\336\037\000'
    _globals['_POSITIONWITHPERIODLOCK'].fields_by_name['locks']._loaded_options = None
    _globals['_POSITIONWITHPERIODLOCK'].fields_by_name['locks']._serialized_options = b'\310\336\037\000'
    _globals['_POSITION']._serialized_start = 210
    _globals['_POSITION']._serialized_end = 532
    _globals['_FULLPOSITIONBREAKDOWN']._serialized_start = 535
    _globals['_FULLPOSITIONBREAKDOWN']._serialized_end = 1105
    _globals['_POSITIONWITHPERIODLOCK']._serialized_start = 1108
    _globals['_POSITIONWITHPERIODLOCK']._serialized_end = 1254
# @@protoc_insertion_point(module_scope)
