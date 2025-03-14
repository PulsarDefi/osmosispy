"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import dydxprotocol.clob.matches_pb2
import dydxprotocol.clob.order_pb2
import dydxprotocol.clob.order_removals_pb2
import dydxprotocol.clob.tx_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Operation(google.protobuf.message.Message):
    """Operation represents an operation in the proposed operations. Operation is
    used internally within the memclob only.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MATCH_FIELD_NUMBER: builtins.int
    SHORT_TERM_ORDER_PLACEMENT_FIELD_NUMBER: builtins.int
    SHORT_TERM_ORDER_CANCELLATION_FIELD_NUMBER: builtins.int
    PREEXISTING_STATEFUL_ORDER_FIELD_NUMBER: builtins.int
    @property
    def match(self) -> dydxprotocol.clob.matches_pb2.ClobMatch: ...
    @property
    def short_term_order_placement(self) -> dydxprotocol.clob.tx_pb2.MsgPlaceOrder: ...
    @property
    def short_term_order_cancellation(self) -> dydxprotocol.clob.tx_pb2.MsgCancelOrder: ...
    @property
    def preexisting_stateful_order(self) -> dydxprotocol.clob.order_pb2.OrderId: ...
    def __init__(
        self,
        *,
        match: dydxprotocol.clob.matches_pb2.ClobMatch | None = ...,
        short_term_order_placement: dydxprotocol.clob.tx_pb2.MsgPlaceOrder | None = ...,
        short_term_order_cancellation: dydxprotocol.clob.tx_pb2.MsgCancelOrder | None = ...,
        preexisting_stateful_order: dydxprotocol.clob.order_pb2.OrderId | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["match", b"match", "operation", b"operation", "preexisting_stateful_order", b"preexisting_stateful_order", "short_term_order_cancellation", b"short_term_order_cancellation", "short_term_order_placement", b"short_term_order_placement"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["match", b"match", "operation", b"operation", "preexisting_stateful_order", b"preexisting_stateful_order", "short_term_order_cancellation", b"short_term_order_cancellation", "short_term_order_placement", b"short_term_order_placement"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["operation", b"operation"]) -> typing.Literal["match", "short_term_order_placement", "short_term_order_cancellation", "preexisting_stateful_order"] | None: ...

global___Operation = Operation

@typing.final
class InternalOperation(google.protobuf.message.Message):
    """InternalOperation represents an internal operation in the operations to
    propose. InternalOperation is used internally within the memclob only.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MATCH_FIELD_NUMBER: builtins.int
    SHORT_TERM_ORDER_PLACEMENT_FIELD_NUMBER: builtins.int
    PREEXISTING_STATEFUL_ORDER_FIELD_NUMBER: builtins.int
    ORDER_REMOVAL_FIELD_NUMBER: builtins.int
    @property
    def match(self) -> dydxprotocol.clob.matches_pb2.ClobMatch: ...
    @property
    def short_term_order_placement(self) -> dydxprotocol.clob.tx_pb2.MsgPlaceOrder: ...
    @property
    def preexisting_stateful_order(self) -> dydxprotocol.clob.order_pb2.OrderId: ...
    @property
    def order_removal(self) -> dydxprotocol.clob.order_removals_pb2.OrderRemoval: ...
    def __init__(
        self,
        *,
        match: dydxprotocol.clob.matches_pb2.ClobMatch | None = ...,
        short_term_order_placement: dydxprotocol.clob.tx_pb2.MsgPlaceOrder | None = ...,
        preexisting_stateful_order: dydxprotocol.clob.order_pb2.OrderId | None = ...,
        order_removal: dydxprotocol.clob.order_removals_pb2.OrderRemoval | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["match", b"match", "operation", b"operation", "order_removal", b"order_removal", "preexisting_stateful_order", b"preexisting_stateful_order", "short_term_order_placement", b"short_term_order_placement"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["match", b"match", "operation", b"operation", "order_removal", b"order_removal", "preexisting_stateful_order", b"preexisting_stateful_order", "short_term_order_placement", b"short_term_order_placement"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["operation", b"operation"]) -> typing.Literal["match", "short_term_order_placement", "preexisting_stateful_order", "order_removal"] | None: ...

global___InternalOperation = InternalOperation
