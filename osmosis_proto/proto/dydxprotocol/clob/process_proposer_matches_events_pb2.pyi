"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import dydxprotocol.clob.order_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ProcessProposerMatchesEvents(google.protobuf.message.Message):
    """ProcessProposerMatchesEvents is used for communicating which events occurred
    in the last block that require updating the state of the memclob in the
    Commit blocker. It contains information about the following state updates:
    - Long term order IDs that were placed in the last block.
    - Stateful order IDs that were expired in the last block.
    - Order IDs that were filled in the last block.
    - Stateful cancellations order IDs that were placed in the last block.
    - Stateful order IDs forcefully removed in the last block.
    - Conditional order IDs triggered in the last block.
    - Conditional order IDs placed, but not triggered in the last block.
    - The height of the block in which the events occurred.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLACED_LONG_TERM_ORDER_IDS_FIELD_NUMBER: builtins.int
    EXPIRED_STATEFUL_ORDER_IDS_FIELD_NUMBER: builtins.int
    ORDER_IDS_FILLED_IN_LAST_BLOCK_FIELD_NUMBER: builtins.int
    PLACED_STATEFUL_CANCELLATION_ORDER_IDS_FIELD_NUMBER: builtins.int
    REMOVED_STATEFUL_ORDER_IDS_FIELD_NUMBER: builtins.int
    CONDITIONAL_ORDER_IDS_TRIGGERED_IN_LAST_BLOCK_FIELD_NUMBER: builtins.int
    PLACED_CONDITIONAL_ORDER_IDS_FIELD_NUMBER: builtins.int
    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    block_height: builtins.int
    @property
    def placed_long_term_order_ids(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.clob.order_pb2.OrderId]: ...
    @property
    def expired_stateful_order_ids(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.clob.order_pb2.OrderId]: ...
    @property
    def order_ids_filled_in_last_block(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.clob.order_pb2.OrderId]: ...
    @property
    def placed_stateful_cancellation_order_ids(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.clob.order_pb2.OrderId]: ...
    @property
    def removed_stateful_order_ids(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.clob.order_pb2.OrderId]: ...
    @property
    def conditional_order_ids_triggered_in_last_block(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.clob.order_pb2.OrderId]: ...
    @property
    def placed_conditional_order_ids(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.clob.order_pb2.OrderId]: ...
    def __init__(
        self,
        *,
        placed_long_term_order_ids: collections.abc.Iterable[dydxprotocol.clob.order_pb2.OrderId] | None = ...,
        expired_stateful_order_ids: collections.abc.Iterable[dydxprotocol.clob.order_pb2.OrderId] | None = ...,
        order_ids_filled_in_last_block: collections.abc.Iterable[dydxprotocol.clob.order_pb2.OrderId] | None = ...,
        placed_stateful_cancellation_order_ids: collections.abc.Iterable[dydxprotocol.clob.order_pb2.OrderId] | None = ...,
        removed_stateful_order_ids: collections.abc.Iterable[dydxprotocol.clob.order_pb2.OrderId] | None = ...,
        conditional_order_ids_triggered_in_last_block: collections.abc.Iterable[dydxprotocol.clob.order_pb2.OrderId] | None = ...,
        placed_conditional_order_ids: collections.abc.Iterable[dydxprotocol.clob.order_pb2.OrderId] | None = ...,
        block_height: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["block_height", b"block_height", "conditional_order_ids_triggered_in_last_block", b"conditional_order_ids_triggered_in_last_block", "expired_stateful_order_ids", b"expired_stateful_order_ids", "order_ids_filled_in_last_block", b"order_ids_filled_in_last_block", "placed_conditional_order_ids", b"placed_conditional_order_ids", "placed_long_term_order_ids", b"placed_long_term_order_ids", "placed_stateful_cancellation_order_ids", b"placed_stateful_cancellation_order_ids", "removed_stateful_order_ids", b"removed_stateful_order_ids"]) -> None: ...

global___ProcessProposerMatchesEvents = ProcessProposerMatchesEvents
