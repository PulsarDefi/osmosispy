"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.message
import osmosis.downtime_detector.v1beta1.downtime_duration_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class RecoveredSinceDowntimeOfLengthRequest(google.protobuf.message.Message):
    """Query for has it been at least $RECOVERY_DURATION units of time,
    since the chain has been down for $DOWNTIME_DURATION.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOWNTIME_FIELD_NUMBER: builtins.int
    RECOVERY_FIELD_NUMBER: builtins.int
    downtime: osmosis.downtime_detector.v1beta1.downtime_duration_pb2.Downtime.ValueType
    @property
    def recovery(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        downtime: osmosis.downtime_detector.v1beta1.downtime_duration_pb2.Downtime.ValueType = ...,
        recovery: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["recovery", b"recovery"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["downtime", b"downtime", "recovery", b"recovery"]) -> None: ...

global___RecoveredSinceDowntimeOfLengthRequest = RecoveredSinceDowntimeOfLengthRequest

@typing_extensions.final
class RecoveredSinceDowntimeOfLengthResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESFULLY_RECOVERED_FIELD_NUMBER: builtins.int
    succesfully_recovered: builtins.bool
    def __init__(
        self,
        *,
        succesfully_recovered: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["succesfully_recovered", b"succesfully_recovered"]) -> None: ...

global___RecoveredSinceDowntimeOfLengthResponse = RecoveredSinceDowntimeOfLengthResponse
