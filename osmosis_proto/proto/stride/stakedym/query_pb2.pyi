"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import cosmos.base.query.v1beta1.pagination_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import stride.stakedym.stakedym_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class QueryHostZoneRequest(google.protobuf.message.Message):
    """Host Zone"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryHostZoneRequest = QueryHostZoneRequest

@typing.final
class QueryHostZoneResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_ZONE_FIELD_NUMBER: builtins.int
    @property
    def host_zone(self) -> stride.stakedym.stakedym_pb2.HostZone: ...
    def __init__(
        self,
        *,
        host_zone: stride.stakedym.stakedym_pb2.HostZone | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["host_zone", b"host_zone"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["host_zone", b"host_zone"]) -> None: ...

global___QueryHostZoneResponse = QueryHostZoneResponse

@typing.final
class QueryDelegationRecordsRequest(google.protobuf.message.Message):
    """All Delegation Records"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INCLUDE_ARCHIVED_FIELD_NUMBER: builtins.int
    include_archived: builtins.bool
    def __init__(
        self,
        *,
        include_archived: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["include_archived", b"include_archived"]) -> None: ...

global___QueryDelegationRecordsRequest = QueryDelegationRecordsRequest

@typing.final
class QueryDelegationRecordsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELEGATION_RECORDS_FIELD_NUMBER: builtins.int
    @property
    def delegation_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.stakedym.stakedym_pb2.DelegationRecord]: ...
    def __init__(
        self,
        *,
        delegation_records: collections.abc.Iterable[stride.stakedym.stakedym_pb2.DelegationRecord] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["delegation_records", b"delegation_records"]) -> None: ...

global___QueryDelegationRecordsResponse = QueryDelegationRecordsResponse

@typing.final
class QueryUnbondingRecordsRequest(google.protobuf.message.Message):
    """All Unbonding Records"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INCLUDE_ARCHIVED_FIELD_NUMBER: builtins.int
    include_archived: builtins.bool
    def __init__(
        self,
        *,
        include_archived: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["include_archived", b"include_archived"]) -> None: ...

global___QueryUnbondingRecordsRequest = QueryUnbondingRecordsRequest

@typing.final
class QueryUnbondingRecordsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UNBONDING_RECORDS_FIELD_NUMBER: builtins.int
    @property
    def unbonding_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.stakedym.stakedym_pb2.UnbondingRecord]: ...
    def __init__(
        self,
        *,
        unbonding_records: collections.abc.Iterable[stride.stakedym.stakedym_pb2.UnbondingRecord] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["unbonding_records", b"unbonding_records"]) -> None: ...

global___QueryUnbondingRecordsResponse = QueryUnbondingRecordsResponse

@typing.final
class QueryRedemptionRecordRequest(google.protobuf.message.Message):
    """Single Redemption Record"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UNBONDING_RECORD_ID_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    unbonding_record_id: builtins.int
    address: builtins.str
    def __init__(
        self,
        *,
        unbonding_record_id: builtins.int = ...,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "unbonding_record_id", b"unbonding_record_id"]) -> None: ...

global___QueryRedemptionRecordRequest = QueryRedemptionRecordRequest

@typing.final
class QueryRedemptionRecordResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REDEMPTION_RECORD_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def redemption_record_response(self) -> global___RedemptionRecordResponse: ...
    def __init__(
        self,
        *,
        redemption_record_response: global___RedemptionRecordResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["redemption_record_response", b"redemption_record_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["redemption_record_response", b"redemption_record_response"]) -> None: ...

global___QueryRedemptionRecordResponse = QueryRedemptionRecordResponse

@typing.final
class QueryRedemptionRecordsRequest(google.protobuf.message.Message):
    """All Redemption Records"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    UNBONDING_RECORD_ID_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    address: builtins.str
    unbonding_record_id: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        address: builtins.str = ...,
        unbonding_record_id: builtins.int = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "pagination", b"pagination", "unbonding_record_id", b"unbonding_record_id"]) -> None: ...

global___QueryRedemptionRecordsRequest = QueryRedemptionRecordsRequest

@typing.final
class QueryRedemptionRecordsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REDEMPTION_RECORD_RESPONSES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def redemption_record_responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RedemptionRecordResponse]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        redemption_record_responses: collections.abc.Iterable[global___RedemptionRecordResponse] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination", "redemption_record_responses", b"redemption_record_responses"]) -> None: ...

global___QueryRedemptionRecordsResponse = QueryRedemptionRecordsResponse

@typing.final
class QuerySlashRecordsRequest(google.protobuf.message.Message):
    """All Slash Records"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QuerySlashRecordsRequest = QuerySlashRecordsRequest

@typing.final
class QuerySlashRecordsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLASH_RECORDS_FIELD_NUMBER: builtins.int
    @property
    def slash_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.stakedym.stakedym_pb2.SlashRecord]: ...
    def __init__(
        self,
        *,
        slash_records: collections.abc.Iterable[stride.stakedym.stakedym_pb2.SlashRecord] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["slash_records", b"slash_records"]) -> None: ...

global___QuerySlashRecordsResponse = QuerySlashRecordsResponse

@typing.final
class RedemptionRecordResponse(google.protobuf.message.Message):
    """Data structure for frontend to consume"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REDEMPTION_RECORD_FIELD_NUMBER: builtins.int
    UNBONDING_COMPLETION_TIME_SECONDS_FIELD_NUMBER: builtins.int
    unbonding_completion_time_seconds: builtins.int
    """The Unix timestamp (in seconds) at which the unbonding for the UR
    associated with this RR completes
    """
    @property
    def redemption_record(self) -> stride.stakedym.stakedym_pb2.RedemptionRecord:
        """Redemption record"""

    def __init__(
        self,
        *,
        redemption_record: stride.stakedym.stakedym_pb2.RedemptionRecord | None = ...,
        unbonding_completion_time_seconds: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["redemption_record", b"redemption_record"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["redemption_record", b"redemption_record", "unbonding_completion_time_seconds", b"unbonding_completion_time_seconds"]) -> None: ...

global___RedemptionRecordResponse = RedemptionRecordResponse
