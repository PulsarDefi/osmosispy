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
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the delaymsg module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELAYED_MESSAGES_FIELD_NUMBER: builtins.int
    NEXT_DELAYED_MESSAGE_ID_FIELD_NUMBER: builtins.int
    next_delayed_message_id: builtins.int
    """next_delayed_message_id is the id to be assigned to next delayed message."""
    @property
    def delayed_messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.delaymsg.delayed_message_pb2.DelayedMessage]:
        """delayed_messages is a list of delayed messages."""

    def __init__(
        self,
        *,
        delayed_messages: collections.abc.Iterable[dydxprotocol.delaymsg.delayed_message_pb2.DelayedMessage] | None = ...,
        next_delayed_message_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["delayed_messages", b"delayed_messages", "next_delayed_message_id", b"next_delayed_message_id"]) -> None: ...

global___GenesisState = GenesisState
