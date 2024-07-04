"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import cosmos.base.query.v1beta1.pagination_pb2
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import osmosis.concentratedliquidity.params_pb2
import osmosis.concentratedliquidity.v1beta1.incentive_record_pb2
import osmosis.concentratedliquidity.v1beta1.position_pb2
import osmosis.concentratedliquidity.v1beta1.tick_info_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class UserPositionsRequest(google.protobuf.message.Message):
    """=============================== UserPositions"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    POOL_ID_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    address: builtins.str
    pool_id: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        address: builtins.str = ...,
        pool_id: builtins.int = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "pagination", b"pagination", "pool_id", b"pool_id"]) -> None: ...

global___UserPositionsRequest = UserPositionsRequest

@typing.final
class UserPositionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITIONS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def positions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.concentratedliquidity.v1beta1.position_pb2.FullPositionBreakdown]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        positions: collections.abc.Iterable[osmosis.concentratedliquidity.v1beta1.position_pb2.FullPositionBreakdown] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination", "positions", b"positions"]) -> None: ...

global___UserPositionsResponse = UserPositionsResponse

@typing.final
class PositionByIdRequest(google.protobuf.message.Message):
    """=============================== PositionById"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_ID_FIELD_NUMBER: builtins.int
    position_id: builtins.int
    def __init__(
        self,
        *,
        position_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["position_id", b"position_id"]) -> None: ...

global___PositionByIdRequest = PositionByIdRequest

@typing.final
class PositionByIdResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_FIELD_NUMBER: builtins.int
    @property
    def position(self) -> osmosis.concentratedliquidity.v1beta1.position_pb2.FullPositionBreakdown: ...
    def __init__(
        self,
        *,
        position: osmosis.concentratedliquidity.v1beta1.position_pb2.FullPositionBreakdown | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["position", b"position"]) -> None: ...

global___PositionByIdResponse = PositionByIdResponse

@typing.final
class NumPoolPositionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["pool_id", b"pool_id"]) -> None: ...

global___NumPoolPositionsRequest = NumPoolPositionsRequest

@typing.final
class NumPoolPositionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_COUNT_FIELD_NUMBER: builtins.int
    position_count: builtins.int
    def __init__(
        self,
        *,
        position_count: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["position_count", b"position_count"]) -> None: ...

global___NumPoolPositionsResponse = NumPoolPositionsResponse

@typing.final
class PoolsRequest(google.protobuf.message.Message):
    """=============================== Pools"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an optional pagination for the request."""

    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination"]) -> None: ...

global___PoolsRequest = PoolsRequest

@typing.final
class PoolsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOLS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines the pagination in the response."""

    def __init__(
        self,
        *,
        pools: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination", "pools", b"pools"]) -> None: ...

global___PoolsResponse = PoolsResponse

@typing.final
class ParamsRequest(google.protobuf.message.Message):
    """=============================== ModuleParams"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ParamsRequest = ParamsRequest

@typing.final
class ParamsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> osmosis.concentratedliquidity.params_pb2.Params: ...
    def __init__(
        self,
        *,
        params: osmosis.concentratedliquidity.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params"]) -> None: ...

global___ParamsResponse = ParamsResponse

@typing.final
class TickLiquidityNet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIQUIDITY_NET_FIELD_NUMBER: builtins.int
    TICK_INDEX_FIELD_NUMBER: builtins.int
    liquidity_net: builtins.str
    tick_index: builtins.int
    def __init__(
        self,
        *,
        liquidity_net: builtins.str = ...,
        tick_index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["liquidity_net", b"liquidity_net", "tick_index", b"tick_index"]) -> None: ...

global___TickLiquidityNet = TickLiquidityNet

@typing.final
class LiquidityDepthWithRange(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIQUIDITY_AMOUNT_FIELD_NUMBER: builtins.int
    LOWER_TICK_FIELD_NUMBER: builtins.int
    UPPER_TICK_FIELD_NUMBER: builtins.int
    liquidity_amount: builtins.str
    lower_tick: builtins.int
    upper_tick: builtins.int
    def __init__(
        self,
        *,
        liquidity_amount: builtins.str = ...,
        lower_tick: builtins.int = ...,
        upper_tick: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["liquidity_amount", b"liquidity_amount", "lower_tick", b"lower_tick", "upper_tick", b"upper_tick"]) -> None: ...

global___LiquidityDepthWithRange = LiquidityDepthWithRange

@typing.final
class LiquidityNetInDirectionRequest(google.protobuf.message.Message):
    """=============================== LiquidityNetInDirection"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    TOKEN_IN_FIELD_NUMBER: builtins.int
    START_TICK_FIELD_NUMBER: builtins.int
    USE_CUR_TICK_FIELD_NUMBER: builtins.int
    BOUND_TICK_FIELD_NUMBER: builtins.int
    USE_NO_BOUND_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    token_in: builtins.str
    start_tick: builtins.int
    use_cur_tick: builtins.bool
    bound_tick: builtins.int
    use_no_bound: builtins.bool
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        token_in: builtins.str = ...,
        start_tick: builtins.int = ...,
        use_cur_tick: builtins.bool = ...,
        bound_tick: builtins.int = ...,
        use_no_bound: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["bound_tick", b"bound_tick", "pool_id", b"pool_id", "start_tick", b"start_tick", "token_in", b"token_in", "use_cur_tick", b"use_cur_tick", "use_no_bound", b"use_no_bound"]) -> None: ...

global___LiquidityNetInDirectionRequest = LiquidityNetInDirectionRequest

@typing.final
class LiquidityNetInDirectionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIQUIDITY_DEPTHS_FIELD_NUMBER: builtins.int
    CURRENT_TICK_FIELD_NUMBER: builtins.int
    CURRENT_LIQUIDITY_FIELD_NUMBER: builtins.int
    CURRENT_SQRT_PRICE_FIELD_NUMBER: builtins.int
    current_tick: builtins.int
    current_liquidity: builtins.str
    current_sqrt_price: builtins.str
    @property
    def liquidity_depths(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TickLiquidityNet]: ...
    def __init__(
        self,
        *,
        liquidity_depths: collections.abc.Iterable[global___TickLiquidityNet] | None = ...,
        current_tick: builtins.int = ...,
        current_liquidity: builtins.str = ...,
        current_sqrt_price: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["current_liquidity", b"current_liquidity", "current_sqrt_price", b"current_sqrt_price", "current_tick", b"current_tick", "liquidity_depths", b"liquidity_depths"]) -> None: ...

global___LiquidityNetInDirectionResponse = LiquidityNetInDirectionResponse

@typing.final
class LiquidityPerTickRangeRequest(google.protobuf.message.Message):
    """=============================== LiquidityPerTickRange"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["pool_id", b"pool_id"]) -> None: ...

global___LiquidityPerTickRangeRequest = LiquidityPerTickRangeRequest

@typing.final
class LiquidityPerTickRangeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIQUIDITY_FIELD_NUMBER: builtins.int
    BUCKET_INDEX_FIELD_NUMBER: builtins.int
    bucket_index: builtins.int
    @property
    def liquidity(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LiquidityDepthWithRange]: ...
    def __init__(
        self,
        *,
        liquidity: collections.abc.Iterable[global___LiquidityDepthWithRange] | None = ...,
        bucket_index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["bucket_index", b"bucket_index", "liquidity", b"liquidity"]) -> None: ...

global___LiquidityPerTickRangeResponse = LiquidityPerTickRangeResponse

@typing.final
class ClaimableSpreadRewardsRequest(google.protobuf.message.Message):
    """===================== QueryClaimableSpreadRewards"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_ID_FIELD_NUMBER: builtins.int
    position_id: builtins.int
    def __init__(
        self,
        *,
        position_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["position_id", b"position_id"]) -> None: ...

global___ClaimableSpreadRewardsRequest = ClaimableSpreadRewardsRequest

@typing.final
class ClaimableSpreadRewardsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLAIMABLE_SPREAD_REWARDS_FIELD_NUMBER: builtins.int
    @property
    def claimable_spread_rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        claimable_spread_rewards: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["claimable_spread_rewards", b"claimable_spread_rewards"]) -> None: ...

global___ClaimableSpreadRewardsResponse = ClaimableSpreadRewardsResponse

@typing.final
class ClaimableIncentivesRequest(google.protobuf.message.Message):
    """===================== QueryClaimableIncentives"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_ID_FIELD_NUMBER: builtins.int
    position_id: builtins.int
    def __init__(
        self,
        *,
        position_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["position_id", b"position_id"]) -> None: ...

global___ClaimableIncentivesRequest = ClaimableIncentivesRequest

@typing.final
class ClaimableIncentivesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLAIMABLE_INCENTIVES_FIELD_NUMBER: builtins.int
    FORFEITED_INCENTIVES_FIELD_NUMBER: builtins.int
    @property
    def claimable_incentives(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    @property
    def forfeited_incentives(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        claimable_incentives: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        forfeited_incentives: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["claimable_incentives", b"claimable_incentives", "forfeited_incentives", b"forfeited_incentives"]) -> None: ...

global___ClaimableIncentivesResponse = ClaimableIncentivesResponse

@typing.final
class PoolAccumulatorRewardsRequest(google.protobuf.message.Message):
    """===================== QueryPoolAccumulatorRewards"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["pool_id", b"pool_id"]) -> None: ...

global___PoolAccumulatorRewardsRequest = PoolAccumulatorRewardsRequest

@typing.final
class PoolAccumulatorRewardsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPREAD_REWARD_GROWTH_GLOBAL_FIELD_NUMBER: builtins.int
    UPTIME_GROWTH_GLOBAL_FIELD_NUMBER: builtins.int
    @property
    def spread_reward_growth_global(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]: ...
    @property
    def uptime_growth_global(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.concentratedliquidity.v1beta1.tick_info_pb2.UptimeTracker]: ...
    def __init__(
        self,
        *,
        spread_reward_growth_global: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
        uptime_growth_global: collections.abc.Iterable[osmosis.concentratedliquidity.v1beta1.tick_info_pb2.UptimeTracker] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["spread_reward_growth_global", b"spread_reward_growth_global", "uptime_growth_global", b"uptime_growth_global"]) -> None: ...

global___PoolAccumulatorRewardsResponse = PoolAccumulatorRewardsResponse

@typing.final
class TickAccumulatorTrackersRequest(google.protobuf.message.Message):
    """===================== QueryTickAccumulatorTrackers"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    TICK_INDEX_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    tick_index: builtins.int
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        tick_index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["pool_id", b"pool_id", "tick_index", b"tick_index"]) -> None: ...

global___TickAccumulatorTrackersRequest = TickAccumulatorTrackersRequest

@typing.final
class TickAccumulatorTrackersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPREAD_REWARD_GROWTH_OPPOSITE_DIRECTION_OF_LAST_TRAVERSAL_FIELD_NUMBER: builtins.int
    UPTIME_TRACKERS_FIELD_NUMBER: builtins.int
    @property
    def spread_reward_growth_opposite_direction_of_last_traversal(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]: ...
    @property
    def uptime_trackers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.concentratedliquidity.v1beta1.tick_info_pb2.UptimeTracker]: ...
    def __init__(
        self,
        *,
        spread_reward_growth_opposite_direction_of_last_traversal: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
        uptime_trackers: collections.abc.Iterable[osmosis.concentratedliquidity.v1beta1.tick_info_pb2.UptimeTracker] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["spread_reward_growth_opposite_direction_of_last_traversal", b"spread_reward_growth_opposite_direction_of_last_traversal", "uptime_trackers", b"uptime_trackers"]) -> None: ...

global___TickAccumulatorTrackersResponse = TickAccumulatorTrackersResponse

@typing.final
class IncentiveRecordsRequest(google.protobuf.message.Message):
    """===================== QueryIncentiveRecords"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination", "pool_id", b"pool_id"]) -> None: ...

global___IncentiveRecordsRequest = IncentiveRecordsRequest

@typing.final
class IncentiveRecordsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INCENTIVE_RECORDS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def incentive_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.concentratedliquidity.v1beta1.incentive_record_pb2.IncentiveRecord]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines the pagination in the response."""

    def __init__(
        self,
        *,
        incentive_records: collections.abc.Iterable[osmosis.concentratedliquidity.v1beta1.incentive_record_pb2.IncentiveRecord] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["incentive_records", b"incentive_records", "pagination", b"pagination"]) -> None: ...

global___IncentiveRecordsResponse = IncentiveRecordsResponse

@typing.final
class CFMMPoolIdLinkFromConcentratedPoolIdRequest(google.protobuf.message.Message):
    """=============================== CFMMPoolIdLinkFromConcentratedPoolId"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONCENTRATED_POOL_ID_FIELD_NUMBER: builtins.int
    concentrated_pool_id: builtins.int
    def __init__(
        self,
        *,
        concentrated_pool_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["concentrated_pool_id", b"concentrated_pool_id"]) -> None: ...

global___CFMMPoolIdLinkFromConcentratedPoolIdRequest = CFMMPoolIdLinkFromConcentratedPoolIdRequest

@typing.final
class CFMMPoolIdLinkFromConcentratedPoolIdResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CFMM_POOL_ID_FIELD_NUMBER: builtins.int
    cfmm_pool_id: builtins.int
    def __init__(
        self,
        *,
        cfmm_pool_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cfmm_pool_id", b"cfmm_pool_id"]) -> None: ...

global___CFMMPoolIdLinkFromConcentratedPoolIdResponse = CFMMPoolIdLinkFromConcentratedPoolIdResponse

@typing.final
class UserUnbondingPositionsRequest(google.protobuf.message.Message):
    """=============================== UserUnbondingPositions"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address"]) -> None: ...

global___UserUnbondingPositionsRequest = UserUnbondingPositionsRequest

@typing.final
class UserUnbondingPositionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITIONS_WITH_PERIOD_LOCK_FIELD_NUMBER: builtins.int
    @property
    def positions_with_period_lock(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.concentratedliquidity.v1beta1.position_pb2.PositionWithPeriodLock]: ...
    def __init__(
        self,
        *,
        positions_with_period_lock: collections.abc.Iterable[osmosis.concentratedliquidity.v1beta1.position_pb2.PositionWithPeriodLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["positions_with_period_lock", b"positions_with_period_lock"]) -> None: ...

global___UserUnbondingPositionsResponse = UserUnbondingPositionsResponse

@typing.final
class GetTotalLiquidityRequest(google.protobuf.message.Message):
    """=============================== GetTotalLiquidity"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetTotalLiquidityRequest = GetTotalLiquidityRequest

@typing.final
class GetTotalLiquidityResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOTAL_LIQUIDITY_FIELD_NUMBER: builtins.int
    @property
    def total_liquidity(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        total_liquidity: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["total_liquidity", b"total_liquidity"]) -> None: ...

global___GetTotalLiquidityResponse = GetTotalLiquidityResponse

@typing.final
class NumNextInitializedTicksRequest(google.protobuf.message.Message):
    """=============================== NumNextInitializedTicks"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    TOKEN_IN_DENOM_FIELD_NUMBER: builtins.int
    NUM_NEXT_INITIALIZED_TICKS_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    token_in_denom: builtins.str
    num_next_initialized_ticks: builtins.int
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        token_in_denom: builtins.str = ...,
        num_next_initialized_ticks: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["num_next_initialized_ticks", b"num_next_initialized_ticks", "pool_id", b"pool_id", "token_in_denom", b"token_in_denom"]) -> None: ...

global___NumNextInitializedTicksRequest = NumNextInitializedTicksRequest

@typing.final
class NumNextInitializedTicksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIQUIDITY_DEPTHS_FIELD_NUMBER: builtins.int
    CURRENT_TICK_FIELD_NUMBER: builtins.int
    CURRENT_LIQUIDITY_FIELD_NUMBER: builtins.int
    current_tick: builtins.int
    current_liquidity: builtins.str
    @property
    def liquidity_depths(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TickLiquidityNet]: ...
    def __init__(
        self,
        *,
        liquidity_depths: collections.abc.Iterable[global___TickLiquidityNet] | None = ...,
        current_tick: builtins.int = ...,
        current_liquidity: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["current_liquidity", b"current_liquidity", "current_tick", b"current_tick", "liquidity_depths", b"liquidity_depths"]) -> None: ...

global___NumNextInitializedTicksResponse = NumNextInitializedTicksResponse
