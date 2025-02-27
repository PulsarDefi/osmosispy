"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BlockRateLimitConfiguration(google.protobuf.message.Message):
    """Defines the block rate limits for CLOB specific operations."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_SHORT_TERM_ORDERS_PER_N_BLOCKS_FIELD_NUMBER: builtins.int
    MAX_STATEFUL_ORDERS_PER_N_BLOCKS_FIELD_NUMBER: builtins.int
    MAX_SHORT_TERM_ORDER_CANCELLATIONS_PER_N_BLOCKS_FIELD_NUMBER: builtins.int
    MAX_SHORT_TERM_ORDERS_AND_CANCELS_PER_N_BLOCKS_FIELD_NUMBER: builtins.int
    @property
    def max_short_term_orders_per_n_blocks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MaxPerNBlocksRateLimit]:
        """How many short term order attempts (successful and failed) are allowed for
        an account per N blocks. Note that the rate limits are applied
        in an AND fashion such that an order placement must pass all rate limit
        configurations.

        Specifying 0 values disables this rate limit.
        Deprecated in favor of `max_short_term_orders_and_cancels_per_n_blocks`
        for v5.x onwards.
        """

    @property
    def max_stateful_orders_per_n_blocks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MaxPerNBlocksRateLimit]:
        """How many stateful order attempts (successful and failed) are allowed for
        an account per N blocks. Note that the rate limits are applied
        in an AND fashion such that an order placement must pass all rate limit
        configurations.

        Specifying 0 values disables this rate limit.
        """

    @property
    def max_short_term_order_cancellations_per_n_blocks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MaxPerNBlocksRateLimit]:
        """How many short term order cancellation attempts (successful and failed) are
        allowed for an account per N blocks. Note that the rate limits are
        applied in an AND fashion such that an order cancellation must pass all
        rate limit configurations.

        Specifying 0 values disables this rate limit.
        Deprecated in favor of `max_short_term_orders_and_cancels_per_n_blocks`
        for v5.x onwards.
        """

    @property
    def max_short_term_orders_and_cancels_per_n_blocks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MaxPerNBlocksRateLimit]:
        """How many short term order place and cancel attempts (successful and failed)
        are allowed for an account per N blocks. Note that the rate limits are
        applied in an AND fashion such that an order placement must pass all rate
        limit configurations.

        Specifying 0 values disables this rate limit.
        """

    def __init__(
        self,
        *,
        max_short_term_orders_per_n_blocks: collections.abc.Iterable[global___MaxPerNBlocksRateLimit] | None = ...,
        max_stateful_orders_per_n_blocks: collections.abc.Iterable[global___MaxPerNBlocksRateLimit] | None = ...,
        max_short_term_order_cancellations_per_n_blocks: collections.abc.Iterable[global___MaxPerNBlocksRateLimit] | None = ...,
        max_short_term_orders_and_cancels_per_n_blocks: collections.abc.Iterable[global___MaxPerNBlocksRateLimit] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["max_short_term_order_cancellations_per_n_blocks", b"max_short_term_order_cancellations_per_n_blocks", "max_short_term_orders_and_cancels_per_n_blocks", b"max_short_term_orders_and_cancels_per_n_blocks", "max_short_term_orders_per_n_blocks", b"max_short_term_orders_per_n_blocks", "max_stateful_orders_per_n_blocks", b"max_stateful_orders_per_n_blocks"]) -> None: ...

global___BlockRateLimitConfiguration = BlockRateLimitConfiguration

@typing.final
class MaxPerNBlocksRateLimit(google.protobuf.message.Message):
    """Defines a rate limit over a specific number of blocks."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NUM_BLOCKS_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    num_blocks: builtins.int
    """How many blocks the rate limit is over.
    Specifying 0 is invalid.
    """
    limit: builtins.int
    """What the limit is for `num_blocks`.
    Specifying 0 is invalid.
    """
    def __init__(
        self,
        *,
        num_blocks: builtins.int = ...,
        limit: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["limit", b"limit", "num_blocks", b"num_blocks"]) -> None: ...

global___MaxPerNBlocksRateLimit = MaxPerNBlocksRateLimit
