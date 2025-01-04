"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _TimeoutPolicy:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TimeoutPolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TimeoutPolicy.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    REJECT_QUERY_RESPONSE: _TimeoutPolicy.ValueType  # 0
    RETRY_QUERY_REQUEST: _TimeoutPolicy.ValueType  # 1
    EXECUTE_QUERY_CALLBACK: _TimeoutPolicy.ValueType  # 2

class TimeoutPolicy(_TimeoutPolicy, metaclass=_TimeoutPolicyEnumTypeWrapper): ...

REJECT_QUERY_RESPONSE: TimeoutPolicy.ValueType  # 0
RETRY_QUERY_REQUEST: TimeoutPolicy.ValueType  # 1
EXECUTE_QUERY_CALLBACK: TimeoutPolicy.ValueType  # 2
global___TimeoutPolicy = TimeoutPolicy

@typing.final
class Query(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    CONNECTION_ID_FIELD_NUMBER: builtins.int
    CHAIN_ID_FIELD_NUMBER: builtins.int
    QUERY_TYPE_FIELD_NUMBER: builtins.int
    REQUEST_DATA_FIELD_NUMBER: builtins.int
    CALLBACK_MODULE_FIELD_NUMBER: builtins.int
    CALLBACK_ID_FIELD_NUMBER: builtins.int
    CALLBACK_DATA_FIELD_NUMBER: builtins.int
    TIMEOUT_POLICY_FIELD_NUMBER: builtins.int
    TIMEOUT_DURATION_FIELD_NUMBER: builtins.int
    TIMEOUT_TIMESTAMP_FIELD_NUMBER: builtins.int
    REQUEST_SENT_FIELD_NUMBER: builtins.int
    SUBMISSION_HEIGHT_FIELD_NUMBER: builtins.int
    id: builtins.str
    connection_id: builtins.str
    chain_id: builtins.str
    query_type: builtins.str
    request_data: builtins.bytes
    callback_module: builtins.str
    callback_id: builtins.str
    callback_data: builtins.bytes
    timeout_policy: global___TimeoutPolicy.ValueType
    timeout_timestamp: builtins.int
    request_sent: builtins.bool
    submission_height: builtins.int
    @property
    def timeout_duration(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        connection_id: builtins.str = ...,
        chain_id: builtins.str = ...,
        query_type: builtins.str = ...,
        request_data: builtins.bytes = ...,
        callback_module: builtins.str = ...,
        callback_id: builtins.str = ...,
        callback_data: builtins.bytes = ...,
        timeout_policy: global___TimeoutPolicy.ValueType = ...,
        timeout_duration: google.protobuf.duration_pb2.Duration | None = ...,
        timeout_timestamp: builtins.int = ...,
        request_sent: builtins.bool = ...,
        submission_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["timeout_duration", b"timeout_duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["callback_data", b"callback_data", "callback_id", b"callback_id", "callback_module", b"callback_module", "chain_id", b"chain_id", "connection_id", b"connection_id", "id", b"id", "query_type", b"query_type", "request_data", b"request_data", "request_sent", b"request_sent", "submission_height", b"submission_height", "timeout_duration", b"timeout_duration", "timeout_policy", b"timeout_policy", "timeout_timestamp", b"timeout_timestamp"]) -> None: ...

global___Query = Query

@typing.final
class DataPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    REMOTE_HEIGHT_FIELD_NUMBER: builtins.int
    LOCAL_HEIGHT_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    id: builtins.str
    remote_height: builtins.str
    local_height: builtins.str
    value: builtins.bytes
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        remote_height: builtins.str = ...,
        local_height: builtins.str = ...,
        value: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "local_height", b"local_height", "remote_height", b"remote_height", "value", b"value"]) -> None: ...

global___DataPoint = DataPoint

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the epochs module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUERIES_FIELD_NUMBER: builtins.int
    @property
    def queries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Query]: ...
    def __init__(
        self,
        *,
        queries: collections.abc.Iterable[global___Query] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["queries", b"queries"]) -> None: ...

global___GenesisState = GenesisState
