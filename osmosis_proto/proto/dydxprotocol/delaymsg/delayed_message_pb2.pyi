"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DelayedMessage(google.protobuf.message.Message):
    """DelayedMessage is a message that is delayed until a certain block height."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    MSG_FIELD_NUMBER: builtins.int
    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    id: builtins.int
    """The ID of the delayed message."""
    block_height: builtins.int
    """The block height at which the message should be executed."""
    @property
    def msg(self) -> google.protobuf.any_pb2.Any:
        """The message to be executed."""

    def __init__(
        self,
        *,
        id: builtins.int = ...,
        msg: google.protobuf.any_pb2.Any | None = ...,
        block_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["msg", b"msg"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["block_height", b"block_height", "id", b"id", "msg", b"msg"]) -> None: ...

global___DelayedMessage = DelayedMessage
