# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: osmosis/concentratedliquidity/v1beta1/query.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from osmosis.concentratedliquidity import params_pb2 as osmosis_dot_concentratedliquidity_dot_params__pb2
from osmosis.concentratedliquidity.v1beta1 import (
    tick_info_pb2 as osmosis_dot_concentratedliquidity_dot_v1beta1_dot_tick__info__pb2,
)
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from osmosis.concentratedliquidity.v1beta1 import (
    position_pb2 as osmosis_dot_concentratedliquidity_dot_v1beta1_dot_position__pb2,
)
from osmosis.concentratedliquidity.v1beta1 import (
    incentive_record_pb2 as osmosis_dot_concentratedliquidity_dot_v1beta1_dot_incentive__record__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n1osmosis/concentratedliquidity/v1beta1/query.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x14gogoproto/gogo.proto\x1a*osmosis/concentratedliquidity/params.proto\x1a\x35osmosis/concentratedliquidity/v1beta1/tick_info.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x34osmosis/concentratedliquidity/v1beta1/position.proto\x1a<osmosis/concentratedliquidity/v1beta1/incentive_record.proto\"\x9c\x01\n\x14UserPositionsRequest\x12#\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"address\"\x12#\n\x07pool_id\x18\x02 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\x12:\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xab\x01\n\x15UserPositionsResponse\x12U\n\tpositions\x18\x01 \x03(\x0b\x32<.osmosis.concentratedliquidity.v1beta1.FullPositionBreakdownB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"B\n\x13PositionByIdRequest\x12+\n\x0bposition_id\x18\x01 \x01(\x04\x42\x16\xf2\xde\x1f\x12yaml:\"position_id\"\"l\n\x14PositionByIdResponse\x12T\n\x08position\x18\x01 \x01(\x0b\x32<.osmosis.concentratedliquidity.v1beta1.FullPositionBreakdownB\x04\xc8\xde\x1f\x00\">\n\x17NumPoolPositionsRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\"M\n\x18NumPoolPositionsResponse\x12\x31\n\x0eposition_count\x18\x01 \x01(\x04\x42\x19\xf2\xde\x1f\x15yaml:\"position_count\"\"J\n\x0cPoolsRequest\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"|\n\rPoolsResponse\x12.\n\x05pools\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x0f\n\rParamsRequest\"M\n\x0eParamsResponse\x12;\n\x06params\x18\x01 \x01(\x0b\x32%.osmosis.concentratedliquidity.ParamsB\x04\xc8\xde\x1f\x00\"\x91\x01\n\x10TickLiquidityNet\x12R\n\rliquidity_net\x18\x01 \x01(\tB;\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xf2\xde\x1f\x14yaml:\"liquidity_net\"\x12)\n\ntick_index\x18\x02 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"tick_index\"\"\xc6\x01\n\x17LiquidityDepthWithRange\x12U\n\x10liquidity_amount\x18\x01 \x01(\tB;\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xf2\xde\x1f\x14yaml:\"liquidity_net\"\x12)\n\nlower_tick\x18\x02 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"lower_tick\"\x12)\n\nupper_tick\x18\x03 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"upper_tick\"\"\xa0\x02\n\x1eLiquidityNetInDirectionRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\x12%\n\x08token_in\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:\"token_in\"\x12)\n\nstart_tick\x18\x03 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"start_tick\"\x12-\n\x0cuse_cur_tick\x18\x04 \x01(\x08\x42\x17\xf2\xde\x1f\x13yaml:\"use_cur_tick\"\x12)\n\nbound_tick\x18\x05 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"bound_tick\"\x12-\n\x0cuse_no_bound\x18\x06 \x01(\x08\x42\x17\xf2\xde\x1f\x13yaml:\"use_no_bound\"\"\xde\x02\n\x1fLiquidityNetInDirectionResponse\x12W\n\x10liquidity_depths\x18\x01 \x03(\x0b\x32\x37.osmosis.concentratedliquidity.v1beta1.TickLiquidityNetB\x04\xc8\xde\x1f\x00\x12\x14\n\x0c\x63urrent_tick\x18\x02 \x01(\x03\x12Z\n\x11\x63urrent_liquidity\x18\x03 \x01(\tB?\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xf2\xde\x1f\x18yaml:\"current_liquidity\"\x12p\n\x12\x63urrent_sqrt_price\x18\x04 \x01(\tBT\xc8\xde\x1f\x00\xda\xde\x1f/github.com/osmosis-labs/osmosis/osmomath.BigDec\xf2\xde\x1f\x19yaml:\"current_sqrt_price\"\"C\n\x1cLiquidityPerTickRangeRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\"\xa7\x01\n\x1dLiquidityPerTickRangeResponse\x12W\n\tliquidity\x18\x01 \x03(\x0b\x32>.osmosis.concentratedliquidity.v1beta1.LiquidityDepthWithRangeB\x04\xc8\xde\x1f\x00\x12-\n\x0c\x62ucket_index\x18\x02 \x01(\x03\x42\x17\xf2\xde\x1f\x13yaml:\"bucket_index\"\"L\n\x1d\x43laimableSpreadRewardsRequest\x12+\n\x0bposition_id\x18\x01 \x01(\x04\x42\x16\xf2\xde\x1f\x12yaml:\"position_id\"\"\x86\x01\n\x1e\x43laimableSpreadRewardsResponse\x12\x64\n\x18\x63laimable_spread_rewards\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:\"claimable_spread_rewards\"\"I\n\x1a\x43laimableIncentivesRequest\x12+\n\x0bposition_id\x18\x01 \x01(\x04\x42\x16\xf2\xde\x1f\x12yaml:\"position_id\"\"\xd9\x01\n\x1b\x43laimableIncentivesResponse\x12\\\n\x14\x63laimable_incentives\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB#\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:\"claimable_incentives\"\x12\\\n\x14\x66orfeited_incentives\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB#\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:\"forfeited_incentives\"\"D\n\x1dPoolAccumulatorRewardsRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\"\x91\x02\n\x1ePoolAccumulatorRewardsResponse\x12v\n\x1bspread_reward_growth_global\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\x12w\n\x14uptime_growth_global\x18\x02 \x03(\x0b\x32\x34.osmosis.concentratedliquidity.v1beta1.UptimeTrackerB#\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:\"uptime_growth_global\"\"p\n\x1eTickAccumulatorTrackersRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\x12)\n\ntick_index\x18\x02 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"tick_index\"\"\xa7\x02\n\x1fTickAccumulatorTrackersResponse\x12\x94\x01\n9spread_reward_growth_opposite_direction_of_last_traversal\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\x12m\n\x0fuptime_trackers\x18\x02 \x03(\x0b\x32\x34.osmosis.concentratedliquidity.v1beta1.UptimeTrackerB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:\"uptime_trackers\"\"z\n\x17IncentiveRecordsRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xb0\x01\n\x18IncentiveRecordsResponse\x12W\n\x11incentive_records\x18\x01 \x03(\x0b\x32\x36.osmosis.concentratedliquidity.v1beta1.IncentiveRecordB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"l\n+CFMMPoolIdLinkFromConcentratedPoolIdRequest\x12=\n\x14\x63oncentrated_pool_id\x18\x01 \x01(\x04\x42\x1f\xf2\xde\x1f\x1byaml:\"concentrated_pool_id\"\"]\n,CFMMPoolIdLinkFromConcentratedPoolIdResponse\x12-\n\x0c\x63\x66mm_pool_id\x18\x01 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"cfmm_pool_id\"\"D\n\x1dUserUnbondingPositionsRequest\x12#\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"address\"\"\x89\x01\n\x1eUserUnbondingPositionsResponse\x12g\n\x1apositions_with_period_lock\x18\x01 \x03(\x0b\x32=.osmosis.concentratedliquidity.v1beta1.PositionWithPeriodLockB\x04\xc8\xde\x1f\x00\"\x1a\n\x18GetTotalLiquidityRequest\"\x81\x01\n\x19GetTotalLiquidityResponse\x12\x64\n\x0ftotal_liquidity\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\xc3\x01\n\x1eNumNextInitializedTicksRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\x12\x31\n\x0etoken_in_denom\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:\"token_in_denom\"\x12I\n\x1anum_next_initialized_ticks\x18\x03 \x01(\x04\x42%\xf2\xde\x1f!yaml:\"num_next_initialized_ticks\"\"\xec\x01\n\x1fNumNextInitializedTicksResponse\x12W\n\x10liquidity_depths\x18\x01 \x03(\x0b\x32\x37.osmosis.concentratedliquidity.v1beta1.TickLiquidityNetB\x04\xc8\xde\x1f\x00\x12\x14\n\x0c\x63urrent_tick\x18\x02 \x01(\x03\x12Z\n\x11\x63urrent_liquidity\x18\x03 \x01(\tB?\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xf2\xde\x1f\x18yaml:\"current_liquidity\"2\xf1\x1a\n\x05Query\x12\xa8\x01\n\x05Pools\x12\x33.osmosis.concentratedliquidity.v1beta1.PoolsRequest\x1a\x34.osmosis.concentratedliquidity.v1beta1.PoolsResponse\"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/concentratedliquidity/v1beta1/pools\x12\xac\x01\n\x06Params\x12\x34.osmosis.concentratedliquidity.v1beta1.ParamsRequest\x1a\x35.osmosis.concentratedliquidity.v1beta1.ParamsResponse\"5\x82\xd3\xe4\x93\x02/\x12-/osmosis/concentratedliquidity/v1beta1/params\x12\xce\x01\n\rUserPositions\x12;.osmosis.concentratedliquidity.v1beta1.UserPositionsRequest\x1a<.osmosis.concentratedliquidity.v1beta1.UserPositionsResponse\"B\x82\xd3\xe4\x93\x02<\x12:/osmosis/concentratedliquidity/v1beta1/positions/{address}\x12\xeb\x01\n\x15LiquidityPerTickRange\x12\x43.osmosis.concentratedliquidity.v1beta1.LiquidityPerTickRangeRequest\x1a\x44.osmosis.concentratedliquidity.v1beta1.LiquidityPerTickRangeResponse\"G\x82\xd3\xe4\x93\x02\x41\x12?/osmosis/concentratedliquidity/v1beta1/liquidity_per_tick_range\x12\xf3\x01\n\x17LiquidityNetInDirection\x12\x45.osmosis.concentratedliquidity.v1beta1.LiquidityNetInDirectionRequest\x1a\x46.osmosis.concentratedliquidity.v1beta1.LiquidityNetInDirectionResponse\"I\x82\xd3\xe4\x93\x02\x43\x12\x41/osmosis/concentratedliquidity/v1beta1/liquidity_net_in_direction\x12\xee\x01\n\x16\x43laimableSpreadRewards\x12\x44.osmosis.concentratedliquidity.v1beta1.ClaimableSpreadRewardsRequest\x1a\x45.osmosis.concentratedliquidity.v1beta1.ClaimableSpreadRewardsResponse\"G\x82\xd3\xe4\x93\x02\x41\x12?/osmosis/concentratedliquidity/v1beta1/claimable_spread_rewards\x12\xe1\x01\n\x13\x43laimableIncentives\x12\x41.osmosis.concentratedliquidity.v1beta1.ClaimableIncentivesRequest\x1a\x42.osmosis.concentratedliquidity.v1beta1.ClaimableIncentivesResponse\"C\x82\xd3\xe4\x93\x02=\x12;/osmosis/concentratedliquidity/v1beta1/claimable_incentives\x12\xc6\x01\n\x0cPositionById\x12:.osmosis.concentratedliquidity.v1beta1.PositionByIdRequest\x1a;.osmosis.concentratedliquidity.v1beta1.PositionByIdResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/osmosis/concentratedliquidity/v1beta1/position_by_id\x12\xe8\x01\n\x16PoolAccumulatorRewards\x12\x44.osmosis.concentratedliquidity.v1beta1.PoolAccumulatorRewardsRequest\x1a\x45.osmosis.concentratedliquidity.v1beta1.PoolAccumulatorRewardsResponse\"A\x82\xd3\xe4\x93\x02;\x12\x39/osmosis/concentratedliquidity/v1beta1/pool_accum_rewards\x12\xd5\x01\n\x10IncentiveRecords\x12>.osmosis.concentratedliquidity.v1beta1.IncentiveRecordsRequest\x1a?.osmosis.concentratedliquidity.v1beta1.IncentiveRecordsResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/osmosis/concentratedliquidity/v1beta1/incentive_records\x12\xec\x01\n\x17TickAccumulatorTrackers\x12\x45.osmosis.concentratedliquidity.v1beta1.TickAccumulatorTrackersRequest\x1a\x46.osmosis.concentratedliquidity.v1beta1.TickAccumulatorTrackersResponse\"B\x82\xd3\xe4\x93\x02<\x12:/osmosis/concentratedliquidity/v1beta1/tick_accum_trackers\x12\xba\x02\n$CFMMPoolIdLinkFromConcentratedPoolId\x12R.osmosis.concentratedliquidity.v1beta1.CFMMPoolIdLinkFromConcentratedPoolIdRequest\x1aS.osmosis.concentratedliquidity.v1beta1.CFMMPoolIdLinkFromConcentratedPoolIdResponse\"i\x82\xd3\xe4\x93\x02\x63\x12\x61/osmosis/concentratedliquidity/v1beta1/cfmm_pool_id_link_from_concentrated/{concentrated_pool_id}\x12\xf8\x01\n\x16UserUnbondingPositions\x12\x44.osmosis.concentratedliquidity.v1beta1.UserUnbondingPositionsRequest\x1a\x45.osmosis.concentratedliquidity.v1beta1.UserUnbondingPositionsResponse\"Q\x82\xd3\xe4\x93\x02K\x12I/osmosis/concentratedliquidity/v1beta1/user_unbonding_positions/{address}\x12\xda\x01\n\x11GetTotalLiquidity\x12?.osmosis.concentratedliquidity.v1beta1.GetTotalLiquidityRequest\x1a@.osmosis.concentratedliquidity.v1beta1.GetTotalLiquidityResponse\"B\x82\xd3\xe4\x93\x02<\x12:/osmosis/concentratedliquidity/v1beta1/get_total_liquidity\x12\xf3\x01\n\x17NumNextInitializedTicks\x12\x45.osmosis.concentratedliquidity.v1beta1.NumNextInitializedTicksRequest\x1a\x46.osmosis.concentratedliquidity.v1beta1.NumNextInitializedTicksResponse\"I\x82\xd3\xe4\x93\x02\x43\x12\x41/osmosis/concentratedliquidity/v1beta1/num_next_initialized_ticksBPZNgithub.com/osmosis-labs/osmosis/v25/x/concentrated-liquidity/client/queryprotob\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentratedliquidity.v1beta1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = (
        b'ZNgithub.com/osmosis-labs/osmosis/v25/x/concentrated-liquidity/client/queryproto'
    )
    _globals['_USERPOSITIONSREQUEST'].fields_by_name['address']._loaded_options = None
    _globals['_USERPOSITIONSREQUEST'].fields_by_name[
        'address'
    ]._serialized_options = b'\362\336\037\016yaml:\"address\"'
    _globals['_USERPOSITIONSREQUEST'].fields_by_name['pool_id']._loaded_options = None
    _globals['_USERPOSITIONSREQUEST'].fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _globals['_USERPOSITIONSRESPONSE'].fields_by_name['positions']._loaded_options = None
    _globals['_USERPOSITIONSRESPONSE'].fields_by_name['positions']._serialized_options = b'\310\336\037\000'
    _globals['_POSITIONBYIDREQUEST'].fields_by_name['position_id']._loaded_options = None
    _globals['_POSITIONBYIDREQUEST'].fields_by_name[
        'position_id'
    ]._serialized_options = b'\362\336\037\022yaml:\"position_id\"'
    _globals['_POSITIONBYIDRESPONSE'].fields_by_name['position']._loaded_options = None
    _globals['_POSITIONBYIDRESPONSE'].fields_by_name['position']._serialized_options = b'\310\336\037\000'
    _globals['_NUMPOOLPOSITIONSREQUEST'].fields_by_name['pool_id']._loaded_options = None
    _globals['_NUMPOOLPOSITIONSREQUEST'].fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _globals['_NUMPOOLPOSITIONSRESPONSE'].fields_by_name['position_count']._loaded_options = None
    _globals['_NUMPOOLPOSITIONSRESPONSE'].fields_by_name[
        'position_count'
    ]._serialized_options = b'\362\336\037\025yaml:\"position_count\"'
    _globals['_POOLSRESPONSE'].fields_by_name['pools']._loaded_options = None
    _globals['_POOLSRESPONSE'].fields_by_name['pools']._serialized_options = b'\312\264-\005PoolI'
    _globals['_PARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_PARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
    _globals['_TICKLIQUIDITYNET'].fields_by_name['liquidity_net']._loaded_options = None
    _globals['_TICKLIQUIDITYNET'].fields_by_name[
        'liquidity_net'
    ]._serialized_options = (
        b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\362\336\037\024yaml:\"liquidity_net\"'
    )
    _globals['_TICKLIQUIDITYNET'].fields_by_name['tick_index']._loaded_options = None
    _globals['_TICKLIQUIDITYNET'].fields_by_name[
        'tick_index'
    ]._serialized_options = b'\362\336\037\021yaml:\"tick_index\"'
    _globals['_LIQUIDITYDEPTHWITHRANGE'].fields_by_name['liquidity_amount']._loaded_options = None
    _globals['_LIQUIDITYDEPTHWITHRANGE'].fields_by_name[
        'liquidity_amount'
    ]._serialized_options = (
        b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\362\336\037\024yaml:\"liquidity_net\"'
    )
    _globals['_LIQUIDITYDEPTHWITHRANGE'].fields_by_name['lower_tick']._loaded_options = None
    _globals['_LIQUIDITYDEPTHWITHRANGE'].fields_by_name[
        'lower_tick'
    ]._serialized_options = b'\362\336\037\021yaml:\"lower_tick\"'
    _globals['_LIQUIDITYDEPTHWITHRANGE'].fields_by_name['upper_tick']._loaded_options = None
    _globals['_LIQUIDITYDEPTHWITHRANGE'].fields_by_name[
        'upper_tick'
    ]._serialized_options = b'\362\336\037\021yaml:\"upper_tick\"'
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name['pool_id']._loaded_options = None
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name['token_in']._loaded_options = None
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name[
        'token_in'
    ]._serialized_options = b'\362\336\037\017yaml:\"token_in\"'
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name['start_tick']._loaded_options = None
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name[
        'start_tick'
    ]._serialized_options = b'\362\336\037\021yaml:\"start_tick\"'
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name['use_cur_tick']._loaded_options = None
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name[
        'use_cur_tick'
    ]._serialized_options = b'\362\336\037\023yaml:\"use_cur_tick\"'
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name['bound_tick']._loaded_options = None
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name[
        'bound_tick'
    ]._serialized_options = b'\362\336\037\021yaml:\"bound_tick\"'
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name['use_no_bound']._loaded_options = None
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST'].fields_by_name[
        'use_no_bound'
    ]._serialized_options = b'\362\336\037\023yaml:\"use_no_bound\"'
    _globals['_LIQUIDITYNETINDIRECTIONRESPONSE'].fields_by_name['liquidity_depths']._loaded_options = None
    _globals['_LIQUIDITYNETINDIRECTIONRESPONSE'].fields_by_name[
        'liquidity_depths'
    ]._serialized_options = b'\310\336\037\000'
    _globals['_LIQUIDITYNETINDIRECTIONRESPONSE'].fields_by_name['current_liquidity']._loaded_options = None
    _globals['_LIQUIDITYNETINDIRECTIONRESPONSE'].fields_by_name[
        'current_liquidity'
    ]._serialized_options = (
        b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\362\336\037\030yaml:\"current_liquidity\"'
    )
    _globals['_LIQUIDITYNETINDIRECTIONRESPONSE'].fields_by_name['current_sqrt_price']._loaded_options = None
    _globals['_LIQUIDITYNETINDIRECTIONRESPONSE'].fields_by_name[
        'current_sqrt_price'
    ]._serialized_options = b'\310\336\037\000\332\336\037/github.com/osmosis-labs/osmosis/osmomath.BigDec\362\336\037\031yaml:\"current_sqrt_price\"'
    _globals['_LIQUIDITYPERTICKRANGEREQUEST'].fields_by_name['pool_id']._loaded_options = None
    _globals['_LIQUIDITYPERTICKRANGEREQUEST'].fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _globals['_LIQUIDITYPERTICKRANGERESPONSE'].fields_by_name['liquidity']._loaded_options = None
    _globals['_LIQUIDITYPERTICKRANGERESPONSE'].fields_by_name['liquidity']._serialized_options = b'\310\336\037\000'
    _globals['_LIQUIDITYPERTICKRANGERESPONSE'].fields_by_name['bucket_index']._loaded_options = None
    _globals['_LIQUIDITYPERTICKRANGERESPONSE'].fields_by_name[
        'bucket_index'
    ]._serialized_options = b'\362\336\037\023yaml:\"bucket_index\"'
    _globals['_CLAIMABLESPREADREWARDSREQUEST'].fields_by_name['position_id']._loaded_options = None
    _globals['_CLAIMABLESPREADREWARDSREQUEST'].fields_by_name[
        'position_id'
    ]._serialized_options = b'\362\336\037\022yaml:\"position_id\"'
    _globals['_CLAIMABLESPREADREWARDSRESPONSE'].fields_by_name['claimable_spread_rewards']._loaded_options = None
    _globals['_CLAIMABLESPREADREWARDSRESPONSE'].fields_by_name[
        'claimable_spread_rewards'
    ]._serialized_options = b'\310\336\037\000\362\336\037\037yaml:\"claimable_spread_rewards\"'
    _globals['_CLAIMABLEINCENTIVESREQUEST'].fields_by_name['position_id']._loaded_options = None
    _globals['_CLAIMABLEINCENTIVESREQUEST'].fields_by_name[
        'position_id'
    ]._serialized_options = b'\362\336\037\022yaml:\"position_id\"'
    _globals['_CLAIMABLEINCENTIVESRESPONSE'].fields_by_name['claimable_incentives']._loaded_options = None
    _globals['_CLAIMABLEINCENTIVESRESPONSE'].fields_by_name[
        'claimable_incentives'
    ]._serialized_options = b'\310\336\037\000\362\336\037\033yaml:\"claimable_incentives\"'
    _globals['_CLAIMABLEINCENTIVESRESPONSE'].fields_by_name['forfeited_incentives']._loaded_options = None
    _globals['_CLAIMABLEINCENTIVESRESPONSE'].fields_by_name[
        'forfeited_incentives'
    ]._serialized_options = b'\310\336\037\000\362\336\037\033yaml:\"forfeited_incentives\"'
    _globals['_POOLACCUMULATORREWARDSREQUEST'].fields_by_name['pool_id']._loaded_options = None
    _globals['_POOLACCUMULATORREWARDSREQUEST'].fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _globals['_POOLACCUMULATORREWARDSRESPONSE'].fields_by_name['spread_reward_growth_global']._loaded_options = None
    _globals['_POOLACCUMULATORREWARDSRESPONSE'].fields_by_name[
        'spread_reward_growth_global'
    ]._serialized_options = b'\310\336\037\000\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _globals['_POOLACCUMULATORREWARDSRESPONSE'].fields_by_name['uptime_growth_global']._loaded_options = None
    _globals['_POOLACCUMULATORREWARDSRESPONSE'].fields_by_name[
        'uptime_growth_global'
    ]._serialized_options = b'\310\336\037\000\362\336\037\033yaml:\"uptime_growth_global\"'
    _globals['_TICKACCUMULATORTRACKERSREQUEST'].fields_by_name['pool_id']._loaded_options = None
    _globals['_TICKACCUMULATORTRACKERSREQUEST'].fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _globals['_TICKACCUMULATORTRACKERSREQUEST'].fields_by_name['tick_index']._loaded_options = None
    _globals['_TICKACCUMULATORTRACKERSREQUEST'].fields_by_name[
        'tick_index'
    ]._serialized_options = b'\362\336\037\021yaml:\"tick_index\"'
    _globals['_TICKACCUMULATORTRACKERSRESPONSE'].fields_by_name[
        'spread_reward_growth_opposite_direction_of_last_traversal'
    ]._loaded_options = None
    _globals['_TICKACCUMULATORTRACKERSRESPONSE'].fields_by_name[
        'spread_reward_growth_opposite_direction_of_last_traversal'
    ]._serialized_options = b'\310\336\037\000\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _globals['_TICKACCUMULATORTRACKERSRESPONSE'].fields_by_name['uptime_trackers']._loaded_options = None
    _globals['_TICKACCUMULATORTRACKERSRESPONSE'].fields_by_name[
        'uptime_trackers'
    ]._serialized_options = b'\310\336\037\000\362\336\037\026yaml:\"uptime_trackers\"'
    _globals['_INCENTIVERECORDSREQUEST'].fields_by_name['pool_id']._loaded_options = None
    _globals['_INCENTIVERECORDSREQUEST'].fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _globals['_INCENTIVERECORDSRESPONSE'].fields_by_name['incentive_records']._loaded_options = None
    _globals['_INCENTIVERECORDSRESPONSE'].fields_by_name['incentive_records']._serialized_options = b'\310\336\037\000'
    _globals['_CFMMPOOLIDLINKFROMCONCENTRATEDPOOLIDREQUEST'].fields_by_name[
        'concentrated_pool_id'
    ]._loaded_options = None
    _globals['_CFMMPOOLIDLINKFROMCONCENTRATEDPOOLIDREQUEST'].fields_by_name[
        'concentrated_pool_id'
    ]._serialized_options = b'\362\336\037\033yaml:\"concentrated_pool_id\"'
    _globals['_CFMMPOOLIDLINKFROMCONCENTRATEDPOOLIDRESPONSE'].fields_by_name['cfmm_pool_id']._loaded_options = None
    _globals['_CFMMPOOLIDLINKFROMCONCENTRATEDPOOLIDRESPONSE'].fields_by_name[
        'cfmm_pool_id'
    ]._serialized_options = b'\362\336\037\023yaml:\"cfmm_pool_id\"'
    _globals['_USERUNBONDINGPOSITIONSREQUEST'].fields_by_name['address']._loaded_options = None
    _globals['_USERUNBONDINGPOSITIONSREQUEST'].fields_by_name[
        'address'
    ]._serialized_options = b'\362\336\037\016yaml:\"address\"'
    _globals['_USERUNBONDINGPOSITIONSRESPONSE'].fields_by_name['positions_with_period_lock']._loaded_options = None
    _globals['_USERUNBONDINGPOSITIONSRESPONSE'].fields_by_name[
        'positions_with_period_lock'
    ]._serialized_options = b'\310\336\037\000'
    _globals['_GETTOTALLIQUIDITYRESPONSE'].fields_by_name['total_liquidity']._loaded_options = None
    _globals['_GETTOTALLIQUIDITYRESPONSE'].fields_by_name[
        'total_liquidity'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_NUMNEXTINITIALIZEDTICKSREQUEST'].fields_by_name['pool_id']._loaded_options = None
    _globals['_NUMNEXTINITIALIZEDTICKSREQUEST'].fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _globals['_NUMNEXTINITIALIZEDTICKSREQUEST'].fields_by_name['token_in_denom']._loaded_options = None
    _globals['_NUMNEXTINITIALIZEDTICKSREQUEST'].fields_by_name[
        'token_in_denom'
    ]._serialized_options = b'\362\336\037\025yaml:\"token_in_denom\"'
    _globals['_NUMNEXTINITIALIZEDTICKSREQUEST'].fields_by_name['num_next_initialized_ticks']._loaded_options = None
    _globals['_NUMNEXTINITIALIZEDTICKSREQUEST'].fields_by_name[
        'num_next_initialized_ticks'
    ]._serialized_options = b'\362\336\037!yaml:\"num_next_initialized_ticks\"'
    _globals['_NUMNEXTINITIALIZEDTICKSRESPONSE'].fields_by_name['liquidity_depths']._loaded_options = None
    _globals['_NUMNEXTINITIALIZEDTICKSRESPONSE'].fields_by_name[
        'liquidity_depths'
    ]._serialized_options = b'\310\336\037\000'
    _globals['_NUMNEXTINITIALIZEDTICKSRESPONSE'].fields_by_name['current_liquidity']._loaded_options = None
    _globals['_NUMNEXTINITIALIZEDTICKSRESPONSE'].fields_by_name[
        'current_liquidity'
    ]._serialized_options = (
        b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\362\336\037\030yaml:\"current_liquidity\"'
    )
    _globals['_QUERY'].methods_by_name['Pools']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'Pools'
    ]._serialized_options = b'\202\323\344\223\002.\022,/osmosis/concentratedliquidity/v1beta1/pools'
    _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'Params'
    ]._serialized_options = b'\202\323\344\223\002/\022-/osmosis/concentratedliquidity/v1beta1/params'
    _globals['_QUERY'].methods_by_name['UserPositions']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'UserPositions'
    ]._serialized_options = b'\202\323\344\223\002<\022:/osmosis/concentratedliquidity/v1beta1/positions/{address}'
    _globals['_QUERY'].methods_by_name['LiquidityPerTickRange']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'LiquidityPerTickRange'
    ]._serialized_options = b'\202\323\344\223\002A\022?/osmosis/concentratedliquidity/v1beta1/liquidity_per_tick_range'
    _globals['_QUERY'].methods_by_name['LiquidityNetInDirection']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'LiquidityNetInDirection'
    ]._serialized_options = (
        b'\202\323\344\223\002C\022A/osmosis/concentratedliquidity/v1beta1/liquidity_net_in_direction'
    )
    _globals['_QUERY'].methods_by_name['ClaimableSpreadRewards']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'ClaimableSpreadRewards'
    ]._serialized_options = b'\202\323\344\223\002A\022?/osmosis/concentratedliquidity/v1beta1/claimable_spread_rewards'
    _globals['_QUERY'].methods_by_name['ClaimableIncentives']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'ClaimableIncentives'
    ]._serialized_options = b'\202\323\344\223\002=\022;/osmosis/concentratedliquidity/v1beta1/claimable_incentives'
    _globals['_QUERY'].methods_by_name['PositionById']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'PositionById'
    ]._serialized_options = b'\202\323\344\223\0027\0225/osmosis/concentratedliquidity/v1beta1/position_by_id'
    _globals['_QUERY'].methods_by_name['PoolAccumulatorRewards']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'PoolAccumulatorRewards'
    ]._serialized_options = b'\202\323\344\223\002;\0229/osmosis/concentratedliquidity/v1beta1/pool_accum_rewards'
    _globals['_QUERY'].methods_by_name['IncentiveRecords']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'IncentiveRecords'
    ]._serialized_options = b'\202\323\344\223\002:\0228/osmosis/concentratedliquidity/v1beta1/incentive_records'
    _globals['_QUERY'].methods_by_name['TickAccumulatorTrackers']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'TickAccumulatorTrackers'
    ]._serialized_options = b'\202\323\344\223\002<\022:/osmosis/concentratedliquidity/v1beta1/tick_accum_trackers'
    _globals['_QUERY'].methods_by_name['CFMMPoolIdLinkFromConcentratedPoolId']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'CFMMPoolIdLinkFromConcentratedPoolId'
    ]._serialized_options = b'\202\323\344\223\002c\022a/osmosis/concentratedliquidity/v1beta1/cfmm_pool_id_link_from_concentrated/{concentrated_pool_id}'
    _globals['_QUERY'].methods_by_name['UserUnbondingPositions']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'UserUnbondingPositions'
    ]._serialized_options = (
        b'\202\323\344\223\002K\022I/osmosis/concentratedliquidity/v1beta1/user_unbonding_positions/{address}'
    )
    _globals['_QUERY'].methods_by_name['GetTotalLiquidity']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'GetTotalLiquidity'
    ]._serialized_options = b'\202\323\344\223\002<\022:/osmosis/concentratedliquidity/v1beta1/get_total_liquidity'
    _globals['_QUERY'].methods_by_name['NumNextInitializedTicks']._loaded_options = None
    _globals['_QUERY'].methods_by_name[
        'NumNextInitializedTicks'
    ]._serialized_options = (
        b'\202\323\344\223\002C\022A/osmosis/concentratedliquidity/v1beta1/num_next_initialized_ticks'
    )
    _globals['_USERPOSITIONSREQUEST']._serialized_start = 490
    _globals['_USERPOSITIONSREQUEST']._serialized_end = 646
    _globals['_USERPOSITIONSRESPONSE']._serialized_start = 649
    _globals['_USERPOSITIONSRESPONSE']._serialized_end = 820
    _globals['_POSITIONBYIDREQUEST']._serialized_start = 822
    _globals['_POSITIONBYIDREQUEST']._serialized_end = 888
    _globals['_POSITIONBYIDRESPONSE']._serialized_start = 890
    _globals['_POSITIONBYIDRESPONSE']._serialized_end = 998
    _globals['_NUMPOOLPOSITIONSREQUEST']._serialized_start = 1000
    _globals['_NUMPOOLPOSITIONSREQUEST']._serialized_end = 1062
    _globals['_NUMPOOLPOSITIONSRESPONSE']._serialized_start = 1064
    _globals['_NUMPOOLPOSITIONSRESPONSE']._serialized_end = 1141
    _globals['_POOLSREQUEST']._serialized_start = 1143
    _globals['_POOLSREQUEST']._serialized_end = 1217
    _globals['_POOLSRESPONSE']._serialized_start = 1219
    _globals['_POOLSRESPONSE']._serialized_end = 1343
    _globals['_PARAMSREQUEST']._serialized_start = 1345
    _globals['_PARAMSREQUEST']._serialized_end = 1360
    _globals['_PARAMSRESPONSE']._serialized_start = 1362
    _globals['_PARAMSRESPONSE']._serialized_end = 1439
    _globals['_TICKLIQUIDITYNET']._serialized_start = 1442
    _globals['_TICKLIQUIDITYNET']._serialized_end = 1587
    _globals['_LIQUIDITYDEPTHWITHRANGE']._serialized_start = 1590
    _globals['_LIQUIDITYDEPTHWITHRANGE']._serialized_end = 1788
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST']._serialized_start = 1791
    _globals['_LIQUIDITYNETINDIRECTIONREQUEST']._serialized_end = 2079
    _globals['_LIQUIDITYNETINDIRECTIONRESPONSE']._serialized_start = 2082
    _globals['_LIQUIDITYNETINDIRECTIONRESPONSE']._serialized_end = 2432
    _globals['_LIQUIDITYPERTICKRANGEREQUEST']._serialized_start = 2434
    _globals['_LIQUIDITYPERTICKRANGEREQUEST']._serialized_end = 2501
    _globals['_LIQUIDITYPERTICKRANGERESPONSE']._serialized_start = 2504
    _globals['_LIQUIDITYPERTICKRANGERESPONSE']._serialized_end = 2671
    _globals['_CLAIMABLESPREADREWARDSREQUEST']._serialized_start = 2673
    _globals['_CLAIMABLESPREADREWARDSREQUEST']._serialized_end = 2749
    _globals['_CLAIMABLESPREADREWARDSRESPONSE']._serialized_start = 2752
    _globals['_CLAIMABLESPREADREWARDSRESPONSE']._serialized_end = 2886
    _globals['_CLAIMABLEINCENTIVESREQUEST']._serialized_start = 2888
    _globals['_CLAIMABLEINCENTIVESREQUEST']._serialized_end = 2961
    _globals['_CLAIMABLEINCENTIVESRESPONSE']._serialized_start = 2964
    _globals['_CLAIMABLEINCENTIVESRESPONSE']._serialized_end = 3181
    _globals['_POOLACCUMULATORREWARDSREQUEST']._serialized_start = 3183
    _globals['_POOLACCUMULATORREWARDSREQUEST']._serialized_end = 3251
    _globals['_POOLACCUMULATORREWARDSRESPONSE']._serialized_start = 3254
    _globals['_POOLACCUMULATORREWARDSRESPONSE']._serialized_end = 3527
    _globals['_TICKACCUMULATORTRACKERSREQUEST']._serialized_start = 3529
    _globals['_TICKACCUMULATORTRACKERSREQUEST']._serialized_end = 3641
    _globals['_TICKACCUMULATORTRACKERSRESPONSE']._serialized_start = 3644
    _globals['_TICKACCUMULATORTRACKERSRESPONSE']._serialized_end = 3939
    _globals['_INCENTIVERECORDSREQUEST']._serialized_start = 3941
    _globals['_INCENTIVERECORDSREQUEST']._serialized_end = 4063
    _globals['_INCENTIVERECORDSRESPONSE']._serialized_start = 4066
    _globals['_INCENTIVERECORDSRESPONSE']._serialized_end = 4242
    _globals['_CFMMPOOLIDLINKFROMCONCENTRATEDPOOLIDREQUEST']._serialized_start = 4244
    _globals['_CFMMPOOLIDLINKFROMCONCENTRATEDPOOLIDREQUEST']._serialized_end = 4352
    _globals['_CFMMPOOLIDLINKFROMCONCENTRATEDPOOLIDRESPONSE']._serialized_start = 4354
    _globals['_CFMMPOOLIDLINKFROMCONCENTRATEDPOOLIDRESPONSE']._serialized_end = 4447
    _globals['_USERUNBONDINGPOSITIONSREQUEST']._serialized_start = 4449
    _globals['_USERUNBONDINGPOSITIONSREQUEST']._serialized_end = 4517
    _globals['_USERUNBONDINGPOSITIONSRESPONSE']._serialized_start = 4520
    _globals['_USERUNBONDINGPOSITIONSRESPONSE']._serialized_end = 4657
    _globals['_GETTOTALLIQUIDITYREQUEST']._serialized_start = 4659
    _globals['_GETTOTALLIQUIDITYREQUEST']._serialized_end = 4685
    _globals['_GETTOTALLIQUIDITYRESPONSE']._serialized_start = 4688
    _globals['_GETTOTALLIQUIDITYRESPONSE']._serialized_end = 4817
    _globals['_NUMNEXTINITIALIZEDTICKSREQUEST']._serialized_start = 4820
    _globals['_NUMNEXTINITIALIZEDTICKSREQUEST']._serialized_end = 5015
    _globals['_NUMNEXTINITIALIZEDTICKSRESPONSE']._serialized_start = 5018
    _globals['_NUMNEXTINITIALIZEDTICKSRESPONSE']._serialized_end = 5254
    _globals['_QUERY']._serialized_start = 5257
    _globals['_QUERY']._serialized_end = 8698
# @@protoc_insertion_point(module_scope)
