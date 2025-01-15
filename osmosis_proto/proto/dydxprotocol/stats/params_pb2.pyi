"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Params(google.protobuf.message.Message):
    """Params defines the parameters for x/stats module."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WINDOW_DURATION_FIELD_NUMBER: builtins.int
    @property
    def window_duration(self) -> google.protobuf.duration_pb2.Duration:
        """The desired number of seconds in the look-back window."""

    def __init__(
        self,
        *,
        window_duration: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["window_duration", b"window_duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["window_duration", b"window_duration"]) -> None: ...

global___Params = Params
