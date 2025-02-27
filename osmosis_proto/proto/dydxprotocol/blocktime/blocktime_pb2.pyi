"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BlockInfo(google.protobuf.message.Message):
    """BlockInfo stores information about a block"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    height: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["height", b"height", "timestamp", b"timestamp"]) -> None: ...

global___BlockInfo = BlockInfo

@typing.final
class AllDowntimeInfo(google.protobuf.message.Message):
    """AllDowntimeInfo stores information for all downtime durations."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class DowntimeInfo(google.protobuf.message.Message):
        """Stores information about downtime. block_info corresponds to the most
        recent block at which a downtime occurred.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        DURATION_FIELD_NUMBER: builtins.int
        BLOCK_INFO_FIELD_NUMBER: builtins.int
        @property
        def duration(self) -> google.protobuf.duration_pb2.Duration: ...
        @property
        def block_info(self) -> global___BlockInfo: ...
        def __init__(
            self,
            *,
            duration: google.protobuf.duration_pb2.Duration | None = ...,
            block_info: global___BlockInfo | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["block_info", b"block_info", "duration", b"duration"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["block_info", b"block_info", "duration", b"duration"]) -> None: ...

    INFOS_FIELD_NUMBER: builtins.int
    @property
    def infos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AllDowntimeInfo.DowntimeInfo]:
        """The downtime information for each tracked duration. Sorted by duration,
        ascending. (i.e. the same order as they appear in DowntimeParams).
        """

    def __init__(
        self,
        *,
        infos: collections.abc.Iterable[global___AllDowntimeInfo.DowntimeInfo] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["infos", b"infos"]) -> None: ...

global___AllDowntimeInfo = AllDowntimeInfo
