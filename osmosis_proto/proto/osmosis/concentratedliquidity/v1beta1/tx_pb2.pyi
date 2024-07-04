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
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MsgCreatePosition(google.protobuf.message.Message):
    """===================== MsgCreatePosition"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    LOWER_TICK_FIELD_NUMBER: builtins.int
    UPPER_TICK_FIELD_NUMBER: builtins.int
    TOKENS_PROVIDED_FIELD_NUMBER: builtins.int
    TOKEN_MIN_AMOUNT0_FIELD_NUMBER: builtins.int
    TOKEN_MIN_AMOUNT1_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    sender: builtins.str
    lower_tick: builtins.int
    upper_tick: builtins.int
    token_min_amount0: builtins.str
    token_min_amount1: builtins.str
    @property
    def tokens_provided(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """tokens_provided is the amount of tokens provided for the position.
        It must at a minimum be of length 1 (for a single sided position)
        and at a maximum be of length 2 (for a position that straddles the current
        tick).
        """

    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        sender: builtins.str = ...,
        lower_tick: builtins.int = ...,
        upper_tick: builtins.int = ...,
        tokens_provided: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        token_min_amount0: builtins.str = ...,
        token_min_amount1: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lower_tick", b"lower_tick", "pool_id", b"pool_id", "sender", b"sender", "token_min_amount0", b"token_min_amount0", "token_min_amount1", b"token_min_amount1", "tokens_provided", b"tokens_provided", "upper_tick", b"upper_tick"]) -> None: ...

global___MsgCreatePosition = MsgCreatePosition

@typing.final
class MsgCreatePositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_ID_FIELD_NUMBER: builtins.int
    AMOUNT0_FIELD_NUMBER: builtins.int
    AMOUNT1_FIELD_NUMBER: builtins.int
    LIQUIDITY_CREATED_FIELD_NUMBER: builtins.int
    LOWER_TICK_FIELD_NUMBER: builtins.int
    UPPER_TICK_FIELD_NUMBER: builtins.int
    position_id: builtins.int
    amount0: builtins.str
    amount1: builtins.str
    liquidity_created: builtins.str
    lower_tick: builtins.int
    """the lower and upper tick are in the response because there are
    instances in which multiple ticks represent the same price, so
    we may move their provided tick to the canonical tick that represents
    the same price.
    """
    upper_tick: builtins.int
    def __init__(
        self,
        *,
        position_id: builtins.int = ...,
        amount0: builtins.str = ...,
        amount1: builtins.str = ...,
        liquidity_created: builtins.str = ...,
        lower_tick: builtins.int = ...,
        upper_tick: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["amount0", b"amount0", "amount1", b"amount1", "liquidity_created", b"liquidity_created", "lower_tick", b"lower_tick", "position_id", b"position_id", "upper_tick", b"upper_tick"]) -> None: ...

global___MsgCreatePositionResponse = MsgCreatePositionResponse

@typing.final
class MsgAddToPosition(google.protobuf.message.Message):
    """===================== MsgAddToPosition"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_ID_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    AMOUNT0_FIELD_NUMBER: builtins.int
    AMOUNT1_FIELD_NUMBER: builtins.int
    TOKEN_MIN_AMOUNT0_FIELD_NUMBER: builtins.int
    TOKEN_MIN_AMOUNT1_FIELD_NUMBER: builtins.int
    position_id: builtins.int
    sender: builtins.str
    amount0: builtins.str
    """amount0 represents the amount of token0 willing to put in."""
    amount1: builtins.str
    """amount1 represents the amount of token1 willing to put in."""
    token_min_amount0: builtins.str
    """token_min_amount0 represents the minimum amount of token0 desired from the
    new position being created. Note that this field indicates the min amount0
    corresponding to the liquidity that is being added, not the total
    liquidity of the position.
    """
    token_min_amount1: builtins.str
    """token_min_amount1 represents the minimum amount of token1 desired from the
    new position being created. Note that this field indicates the min amount1
    corresponding to the liquidity that is being added, not the total
    liquidity of the position.
    """
    def __init__(
        self,
        *,
        position_id: builtins.int = ...,
        sender: builtins.str = ...,
        amount0: builtins.str = ...,
        amount1: builtins.str = ...,
        token_min_amount0: builtins.str = ...,
        token_min_amount1: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["amount0", b"amount0", "amount1", b"amount1", "position_id", b"position_id", "sender", b"sender", "token_min_amount0", b"token_min_amount0", "token_min_amount1", b"token_min_amount1"]) -> None: ...

global___MsgAddToPosition = MsgAddToPosition

@typing.final
class MsgAddToPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_ID_FIELD_NUMBER: builtins.int
    AMOUNT0_FIELD_NUMBER: builtins.int
    AMOUNT1_FIELD_NUMBER: builtins.int
    position_id: builtins.int
    amount0: builtins.str
    amount1: builtins.str
    def __init__(
        self,
        *,
        position_id: builtins.int = ...,
        amount0: builtins.str = ...,
        amount1: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["amount0", b"amount0", "amount1", b"amount1", "position_id", b"position_id"]) -> None: ...

global___MsgAddToPositionResponse = MsgAddToPositionResponse

@typing.final
class MsgWithdrawPosition(google.protobuf.message.Message):
    """===================== MsgWithdrawPosition"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_ID_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    LIQUIDITY_AMOUNT_FIELD_NUMBER: builtins.int
    position_id: builtins.int
    sender: builtins.str
    liquidity_amount: builtins.str
    def __init__(
        self,
        *,
        position_id: builtins.int = ...,
        sender: builtins.str = ...,
        liquidity_amount: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["liquidity_amount", b"liquidity_amount", "position_id", b"position_id", "sender", b"sender"]) -> None: ...

global___MsgWithdrawPosition = MsgWithdrawPosition

@typing.final
class MsgWithdrawPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AMOUNT0_FIELD_NUMBER: builtins.int
    AMOUNT1_FIELD_NUMBER: builtins.int
    amount0: builtins.str
    amount1: builtins.str
    def __init__(
        self,
        *,
        amount0: builtins.str = ...,
        amount1: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["amount0", b"amount0", "amount1", b"amount1"]) -> None: ...

global___MsgWithdrawPositionResponse = MsgWithdrawPositionResponse

@typing.final
class MsgCollectSpreadRewards(google.protobuf.message.Message):
    """===================== MsgCollectSpreadRewards"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_IDS_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    sender: builtins.str
    @property
    def position_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        position_ids: collections.abc.Iterable[builtins.int] | None = ...,
        sender: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["position_ids", b"position_ids", "sender", b"sender"]) -> None: ...

global___MsgCollectSpreadRewards = MsgCollectSpreadRewards

@typing.final
class MsgCollectSpreadRewardsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COLLECTED_SPREAD_REWARDS_FIELD_NUMBER: builtins.int
    @property
    def collected_spread_rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        collected_spread_rewards: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["collected_spread_rewards", b"collected_spread_rewards"]) -> None: ...

global___MsgCollectSpreadRewardsResponse = MsgCollectSpreadRewardsResponse

@typing.final
class MsgCollectIncentives(google.protobuf.message.Message):
    """===================== MsgCollectIncentives"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_IDS_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    sender: builtins.str
    @property
    def position_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        position_ids: collections.abc.Iterable[builtins.int] | None = ...,
        sender: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["position_ids", b"position_ids", "sender", b"sender"]) -> None: ...

global___MsgCollectIncentives = MsgCollectIncentives

@typing.final
class MsgCollectIncentivesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COLLECTED_INCENTIVES_FIELD_NUMBER: builtins.int
    FORFEITED_INCENTIVES_FIELD_NUMBER: builtins.int
    @property
    def collected_incentives(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    @property
    def forfeited_incentives(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        collected_incentives: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        forfeited_incentives: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["collected_incentives", b"collected_incentives", "forfeited_incentives", b"forfeited_incentives"]) -> None: ...

global___MsgCollectIncentivesResponse = MsgCollectIncentivesResponse

@typing.final
class MsgFungifyChargedPositions(google.protobuf.message.Message):
    """===================== MsgFungifyChargedPositions"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_IDS_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    sender: builtins.str
    @property
    def position_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        position_ids: collections.abc.Iterable[builtins.int] | None = ...,
        sender: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["position_ids", b"position_ids", "sender", b"sender"]) -> None: ...

global___MsgFungifyChargedPositions = MsgFungifyChargedPositions

@typing.final
class MsgFungifyChargedPositionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEW_POSITION_ID_FIELD_NUMBER: builtins.int
    new_position_id: builtins.int
    def __init__(
        self,
        *,
        new_position_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["new_position_id", b"new_position_id"]) -> None: ...

global___MsgFungifyChargedPositionsResponse = MsgFungifyChargedPositionsResponse

@typing.final
class MsgTransferPositions(google.protobuf.message.Message):
    """===================== MsgTransferPositions"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_IDS_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    NEW_OWNER_FIELD_NUMBER: builtins.int
    sender: builtins.str
    new_owner: builtins.str
    @property
    def position_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        position_ids: collections.abc.Iterable[builtins.int] | None = ...,
        sender: builtins.str = ...,
        new_owner: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["new_owner", b"new_owner", "position_ids", b"position_ids", "sender", b"sender"]) -> None: ...

global___MsgTransferPositions = MsgTransferPositions

@typing.final
class MsgTransferPositionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgTransferPositionsResponse = MsgTransferPositionsResponse
