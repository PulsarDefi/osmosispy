"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import dydxprotocol.delaymsg.delayed_message_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class QueryNextDelayedMessageIdRequest(google.protobuf.message.Message):
    """QueryNextDelayedMessageIdRequest is the request type for the
    NextDelayedMessageId RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryNextDelayedMessageIdRequest = QueryNextDelayedMessageIdRequest

@typing.final
class QueryNextDelayedMessageIdResponse(google.protobuf.message.Message):
    """QueryNextDelayedMessageIdResponse is the response type for the
    NextDelayedMessageId RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEXT_DELAYED_MESSAGE_ID_FIELD_NUMBER: builtins.int
    next_delayed_message_id: builtins.int
    def __init__(
        self,
        *,
        next_delayed_message_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_delayed_message_id", b"next_delayed_message_id"]) -> None: ...

global___QueryNextDelayedMessageIdResponse = QueryNextDelayedMessageIdResponse

@typing.final
class QueryMessageRequest(google.protobuf.message.Message):
    """QueryMessageRequest is the request type for the Message RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.int
    def __init__(
        self,
        *,
        id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___QueryMessageRequest = QueryMessageRequest

@typing.final
class QueryMessageResponse(google.protobuf.message.Message):
    """QueryGetMessageResponse is the response type for the Message RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGE_FIELD_NUMBER: builtins.int
    @property
    def message(self) -> dydxprotocol.delaymsg.delayed_message_pb2.DelayedMessage: ...
    def __init__(
        self,
        *,
        message: dydxprotocol.delaymsg.delayed_message_pb2.DelayedMessage | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["message", b"message"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["message", b"message"]) -> None: ...

global___QueryMessageResponse = QueryMessageResponse

@typing.final
class QueryBlockMessageIdsRequest(google.protobuf.message.Message):
    """QueryBlockMessageIdsRequest is the request type for the BlockMessageIds
    RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    block_height: builtins.int
    def __init__(
        self,
        *,
        block_height: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["block_height", b"block_height"]) -> None: ...

global___QueryBlockMessageIdsRequest = QueryBlockMessageIdsRequest

@typing.final
class QueryBlockMessageIdsResponse(google.protobuf.message.Message):
    """QueryGetBlockMessageIdsResponse is the response type for the BlockMessageIds
    RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGE_IDS_FIELD_NUMBER: builtins.int
    @property
    def message_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        message_ids: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["message_ids", b"message_ids"]) -> None: ...

global___QueryBlockMessageIdsResponse = QueryBlockMessageIdsResponse
