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
import stride.records.params_pb2
import stride.records.records_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class QueryParamsRequest(google.protobuf.message.Message):
    """QueryParamsRequest is request type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryParamsRequest = QueryParamsRequest

@typing.final
class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is response type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> stride.records.params_pb2.Params:
        """params holds all the parameters of this module."""

    def __init__(
        self,
        *,
        params: stride.records.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

@typing.final
class QueryGetDepositRecordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.int
    def __init__(
        self,
        *,
        id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___QueryGetDepositRecordRequest = QueryGetDepositRecordRequest

@typing.final
class QueryGetDepositRecordResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEPOSIT_RECORD_FIELD_NUMBER: builtins.int
    @property
    def deposit_record(self) -> stride.records.records_pb2.DepositRecord: ...
    def __init__(
        self,
        *,
        deposit_record: stride.records.records_pb2.DepositRecord | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["deposit_record", b"deposit_record"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["deposit_record", b"deposit_record"]) -> None: ...

global___QueryGetDepositRecordResponse = QueryGetDepositRecordResponse

@typing.final
class QueryAllDepositRecordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination"]) -> None: ...

global___QueryAllDepositRecordRequest = QueryAllDepositRecordRequest

@typing.final
class QueryAllDepositRecordResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEPOSIT_RECORD_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def deposit_record(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.records.records_pb2.DepositRecord]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        deposit_record: collections.abc.Iterable[stride.records.records_pb2.DepositRecord] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["deposit_record", b"deposit_record", "pagination", b"pagination"]) -> None: ...

global___QueryAllDepositRecordResponse = QueryAllDepositRecordResponse

@typing.final
class QueryDepositRecordByHostRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_ZONE_ID_FIELD_NUMBER: builtins.int
    host_zone_id: builtins.str
    def __init__(
        self,
        *,
        host_zone_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host_zone_id", b"host_zone_id"]) -> None: ...

global___QueryDepositRecordByHostRequest = QueryDepositRecordByHostRequest

@typing.final
class QueryDepositRecordByHostResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEPOSIT_RECORD_FIELD_NUMBER: builtins.int
    @property
    def deposit_record(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.records.records_pb2.DepositRecord]: ...
    def __init__(
        self,
        *,
        deposit_record: collections.abc.Iterable[stride.records.records_pb2.DepositRecord] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["deposit_record", b"deposit_record"]) -> None: ...

global___QueryDepositRecordByHostResponse = QueryDepositRecordByHostResponse

@typing.final
class QueryGetUserRedemptionRecordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___QueryGetUserRedemptionRecordRequest = QueryGetUserRedemptionRecordRequest

@typing.final
class QueryGetUserRedemptionRecordResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_REDEMPTION_RECORD_FIELD_NUMBER: builtins.int
    @property
    def user_redemption_record(self) -> stride.records.records_pb2.UserRedemptionRecord: ...
    def __init__(
        self,
        *,
        user_redemption_record: stride.records.records_pb2.UserRedemptionRecord | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["user_redemption_record", b"user_redemption_record"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["user_redemption_record", b"user_redemption_record"]) -> None: ...

global___QueryGetUserRedemptionRecordResponse = QueryGetUserRedemptionRecordResponse

@typing.final
class QueryAllUserRedemptionRecordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination"]) -> None: ...

global___QueryAllUserRedemptionRecordRequest = QueryAllUserRedemptionRecordRequest

@typing.final
class QueryAllUserRedemptionRecordResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_REDEMPTION_RECORD_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def user_redemption_record(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.records.records_pb2.UserRedemptionRecord]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        user_redemption_record: collections.abc.Iterable[stride.records.records_pb2.UserRedemptionRecord] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination", "user_redemption_record", b"user_redemption_record"]) -> None: ...

global___QueryAllUserRedemptionRecordResponse = QueryAllUserRedemptionRecordResponse

@typing.final
class QueryAllUserRedemptionRecordForUserRequest(google.protobuf.message.Message):
    """Query UserRedemptionRecords by chainId / userId pair"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHAIN_ID_FIELD_NUMBER: builtins.int
    DAY_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    chain_id: builtins.str
    day: builtins.int
    address: builtins.str
    limit: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        chain_id: builtins.str = ...,
        day: builtins.int = ...,
        address: builtins.str = ...,
        limit: builtins.int = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "chain_id", b"chain_id", "day", b"day", "limit", b"limit", "pagination", b"pagination"]) -> None: ...

global___QueryAllUserRedemptionRecordForUserRequest = QueryAllUserRedemptionRecordForUserRequest

@typing.final
class QueryAllUserRedemptionRecordForUserResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_REDEMPTION_RECORD_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def user_redemption_record(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.records.records_pb2.UserRedemptionRecord]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        user_redemption_record: collections.abc.Iterable[stride.records.records_pb2.UserRedemptionRecord] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination", "user_redemption_record", b"user_redemption_record"]) -> None: ...

global___QueryAllUserRedemptionRecordForUserResponse = QueryAllUserRedemptionRecordForUserResponse

@typing.final
class QueryGetEpochUnbondingRecordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPOCH_NUMBER_FIELD_NUMBER: builtins.int
    epoch_number: builtins.int
    def __init__(
        self,
        *,
        epoch_number: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["epoch_number", b"epoch_number"]) -> None: ...

global___QueryGetEpochUnbondingRecordRequest = QueryGetEpochUnbondingRecordRequest

@typing.final
class QueryGetEpochUnbondingRecordResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPOCH_UNBONDING_RECORD_FIELD_NUMBER: builtins.int
    @property
    def epoch_unbonding_record(self) -> stride.records.records_pb2.EpochUnbondingRecord: ...
    def __init__(
        self,
        *,
        epoch_unbonding_record: stride.records.records_pb2.EpochUnbondingRecord | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["epoch_unbonding_record", b"epoch_unbonding_record"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["epoch_unbonding_record", b"epoch_unbonding_record"]) -> None: ...

global___QueryGetEpochUnbondingRecordResponse = QueryGetEpochUnbondingRecordResponse

@typing.final
class QueryAllEpochUnbondingRecordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination"]) -> None: ...

global___QueryAllEpochUnbondingRecordRequest = QueryAllEpochUnbondingRecordRequest

@typing.final
class QueryAllEpochUnbondingRecordResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPOCH_UNBONDING_RECORD_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def epoch_unbonding_record(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.records.records_pb2.EpochUnbondingRecord]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        epoch_unbonding_record: collections.abc.Iterable[stride.records.records_pb2.EpochUnbondingRecord] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["epoch_unbonding_record", b"epoch_unbonding_record", "pagination", b"pagination"]) -> None: ...

global___QueryAllEpochUnbondingRecordResponse = QueryAllEpochUnbondingRecordResponse

@typing.final
class QueryLSMDepositRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHAIN_ID_FIELD_NUMBER: builtins.int
    DENOM_FIELD_NUMBER: builtins.int
    chain_id: builtins.str
    denom: builtins.str
    def __init__(
        self,
        *,
        chain_id: builtins.str = ...,
        denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["chain_id", b"chain_id", "denom", b"denom"]) -> None: ...

global___QueryLSMDepositRequest = QueryLSMDepositRequest

@typing.final
class QueryLSMDepositResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEPOSIT_FIELD_NUMBER: builtins.int
    @property
    def deposit(self) -> stride.records.records_pb2.LSMTokenDeposit: ...
    def __init__(
        self,
        *,
        deposit: stride.records.records_pb2.LSMTokenDeposit | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["deposit", b"deposit"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["deposit", b"deposit"]) -> None: ...

global___QueryLSMDepositResponse = QueryLSMDepositResponse

@typing.final
class QueryLSMDepositsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHAIN_ID_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    chain_id: builtins.str
    validator_address: builtins.str
    status: builtins.str
    def __init__(
        self,
        *,
        chain_id: builtins.str = ...,
        validator_address: builtins.str = ...,
        status: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["chain_id", b"chain_id", "status", b"status", "validator_address", b"validator_address"]) -> None: ...

global___QueryLSMDepositsRequest = QueryLSMDepositsRequest

@typing.final
class QueryLSMDepositsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEPOSITS_FIELD_NUMBER: builtins.int
    @property
    def deposits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.records.records_pb2.LSMTokenDeposit]: ...
    def __init__(
        self,
        *,
        deposits: collections.abc.Iterable[stride.records.records_pb2.LSMTokenDeposit] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["deposits", b"deposits"]) -> None: ...

global___QueryLSMDepositsResponse = QueryLSMDepositsResponse
