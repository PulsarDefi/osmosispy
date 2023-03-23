"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import osmosis.lockup.lock_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MsgCreateGauge(google.protobuf.message.Message):
    """MsgCreateGauge creates a gague to distribute rewards to users"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IS_PERPETUAL_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    DISTRIBUTE_TO_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    NUM_EPOCHS_PAID_OVER_FIELD_NUMBER: builtins.int
    is_perpetual: builtins.bool
    """is_perpetual shows if it's a perpetual or non-perpetual gauge
    Non-perpetual gauges distribute their tokens equally per epoch while the
    gauge is in the active period. Perpetual gauges distribute all their tokens
    at a single time and only distribute their tokens again once the gauge is
    refilled
    """
    owner: builtins.str
    """owner is the address of gauge creator"""
    @property
    def distribute_to(self) -> osmosis.lockup.lock_pb2.QueryCondition:
        """distribute_to show which lock the gauge should distribute to by time
        duration or by timestamp
        """
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """coins are coin(s) to be distributed by the gauge"""
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """start_time is the distribution start time"""
    num_epochs_paid_over: builtins.int
    """num_epochs_paid_over is the number of epochs distribution will be completed
    over
    """
    def __init__(
        self,
        *,
        is_perpetual: builtins.bool = ...,
        owner: builtins.str = ...,
        distribute_to: osmosis.lockup.lock_pb2.QueryCondition | None = ...,
        coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        num_epochs_paid_over: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["distribute_to", b"distribute_to", "start_time", b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["coins", b"coins", "distribute_to", b"distribute_to", "is_perpetual", b"is_perpetual", "num_epochs_paid_over", b"num_epochs_paid_over", "owner", b"owner", "start_time", b"start_time"]) -> None: ...

global___MsgCreateGauge = MsgCreateGauge

@typing_extensions.final
class MsgCreateGaugeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgCreateGaugeResponse = MsgCreateGaugeResponse

@typing_extensions.final
class MsgAddToGauge(google.protobuf.message.Message):
    """MsgAddToGauge adds coins to a previously created gauge"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    GAUGE_ID_FIELD_NUMBER: builtins.int
    REWARDS_FIELD_NUMBER: builtins.int
    owner: builtins.str
    """owner is the gauge owner's address"""
    gauge_id: builtins.int
    """gauge_id is the ID of gauge that rewards are getting added to"""
    @property
    def rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """rewards are the coin(s) to add to gauge"""
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
        gauge_id: builtins.int = ...,
        rewards: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gauge_id", b"gauge_id", "owner", b"owner", "rewards", b"rewards"]) -> None: ...

global___MsgAddToGauge = MsgAddToGauge

@typing_extensions.final
class MsgAddToGaugeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgAddToGaugeResponse = MsgAddToGaugeResponse
