"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
this is a legacy package that requires additional migration logic
in order to use the correct package. Decision made to use legacy package path
until clear steps for migration logic and the unknowns for state breaking are
investigated for changing proto package.
"""

import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TickInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIQUIDITY_GROSS_FIELD_NUMBER: builtins.int
    LIQUIDITY_NET_FIELD_NUMBER: builtins.int
    SPREAD_REWARD_GROWTH_OPPOSITE_DIRECTION_OF_LAST_TRAVERSAL_FIELD_NUMBER: builtins.int
    UPTIME_TRACKERS_FIELD_NUMBER: builtins.int
    liquidity_gross: builtins.str
    liquidity_net: builtins.str
    @property
    def spread_reward_growth_opposite_direction_of_last_traversal(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]:
        """Total spread rewards accumulated in the opposite direction that the tick
        was last crossed. i.e. if the current tick is to the right of this tick
        (meaning its currently a greater price), then this is the total spread
        rewards accumulated below the tick. If the current tick is to the left of
        this tick (meaning its currently at a lower price), then this is the total
        spread rewards accumulated above the tick.

        Note: the way this value is used depends on the direction of spread rewards
        we are calculating for. If we are calculating spread rewards below the
        lower tick and the lower tick is the active tick, then this is the
        spreadRewardGrowthGlobal - the lower tick's
        spreadRewardGrowthOppositeDirectionOfLastTraversal. If we are calculating
        spread rewards above the upper tick and the upper tick is the active tick,
        then this is just the tick's
        spreadRewardGrowthOppositeDirectionOfLastTraversal value.
        """

    @property
    def uptime_trackers(self) -> global___UptimeTrackers:
        """uptime_trackers is a container encapsulating the uptime trackers.
        We use a container instead of a "repeated UptimeTracker" directly
        because we need the ability to serialize and deserialize the
        container easily for events when crossing a tick.
        """

    def __init__(
        self,
        *,
        liquidity_gross: builtins.str = ...,
        liquidity_net: builtins.str = ...,
        spread_reward_growth_opposite_direction_of_last_traversal: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
        uptime_trackers: global___UptimeTrackers | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["uptime_trackers", b"uptime_trackers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["liquidity_gross", b"liquidity_gross", "liquidity_net", b"liquidity_net", "spread_reward_growth_opposite_direction_of_last_traversal", b"spread_reward_growth_opposite_direction_of_last_traversal", "uptime_trackers", b"uptime_trackers"]) -> None: ...

global___TickInfo = TickInfo

@typing.final
class UptimeTrackers(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIST_FIELD_NUMBER: builtins.int
    @property
    def list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UptimeTracker]: ...
    def __init__(
        self,
        *,
        list: collections.abc.Iterable[global___UptimeTracker] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["list", b"list"]) -> None: ...

global___UptimeTrackers = UptimeTrackers

@typing.final
class UptimeTracker(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPTIME_GROWTH_OUTSIDE_FIELD_NUMBER: builtins.int
    @property
    def uptime_growth_outside(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]: ...
    def __init__(
        self,
        *,
        uptime_growth_outside: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["uptime_growth_outside", b"uptime_growth_outside"]) -> None: ...

global___UptimeTracker = UptimeTracker
