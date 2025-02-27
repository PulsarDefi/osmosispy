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
import google.protobuf.timestamp_pb2
import stride.airdrop.airdrop_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class QueryAirdropRequest(google.protobuf.message.Message):
    """Airdrop"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___QueryAirdropRequest = QueryAirdropRequest

@typing.final
class QueryAirdropResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    REWARD_DENOM_FIELD_NUMBER: builtins.int
    DISTRIBUTION_START_DATE_FIELD_NUMBER: builtins.int
    DISTRIBUTION_END_DATE_FIELD_NUMBER: builtins.int
    CLAWBACK_DATE_FIELD_NUMBER: builtins.int
    CLAIM_TYPE_DEADLINE_DATE_FIELD_NUMBER: builtins.int
    EARLY_CLAIM_PENALTY_FIELD_NUMBER: builtins.int
    DISTRIBUTOR_ADDRESS_FIELD_NUMBER: builtins.int
    ALLOCATOR_ADDRESS_FIELD_NUMBER: builtins.int
    LINKER_ADDRESS_FIELD_NUMBER: builtins.int
    CURRENT_DATE_INDEX_FIELD_NUMBER: builtins.int
    AIRDROP_LENGTH_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Airdrop ID"""
    reward_denom: builtins.str
    """Denom used when distributing rewards"""
    early_claim_penalty: builtins.str
    """Penalty for claiming rewards early - e.g. 0.5 means claiming early will
    result in losing 50% of rewards
    """
    distributor_address: builtins.str
    """Account that holds the total reward balance and distributes to users"""
    allocator_address: builtins.str
    """Admin account with permissions to add or update allocations"""
    linker_address: builtins.str
    """Admin account with permissions to link addresseses"""
    current_date_index: builtins.int
    """The current date index into the airdrop array"""
    airdrop_length: builtins.int
    """The length of the airdrop (i.e. number of periods in the airdrop array)"""
    @property
    def distribution_start_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The first date that claiming begins and rewards are distributed"""

    @property
    def distribution_end_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The last date for rewards to be distributed. Immediately after this date
        the rewards can no longer be claimed, but rewards have not been clawed back
        yet
        """

    @property
    def clawback_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Date with which the rewards are clawed back (occurs after the distribution
        end date)
        """

    @property
    def claim_type_deadline_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Deadline for the user to make a decision on their claim type"""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        reward_denom: builtins.str = ...,
        distribution_start_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        distribution_end_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        clawback_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        claim_type_deadline_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        early_claim_penalty: builtins.str = ...,
        distributor_address: builtins.str = ...,
        allocator_address: builtins.str = ...,
        linker_address: builtins.str = ...,
        current_date_index: builtins.int = ...,
        airdrop_length: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["claim_type_deadline_date", b"claim_type_deadline_date", "clawback_date", b"clawback_date", "distribution_end_date", b"distribution_end_date", "distribution_start_date", b"distribution_start_date"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["airdrop_length", b"airdrop_length", "allocator_address", b"allocator_address", "claim_type_deadline_date", b"claim_type_deadline_date", "clawback_date", b"clawback_date", "current_date_index", b"current_date_index", "distribution_end_date", b"distribution_end_date", "distribution_start_date", b"distribution_start_date", "distributor_address", b"distributor_address", "early_claim_penalty", b"early_claim_penalty", "id", b"id", "linker_address", b"linker_address", "reward_denom", b"reward_denom"]) -> None: ...

global___QueryAirdropResponse = QueryAirdropResponse

@typing.final
class QueryAllAirdropsRequest(google.protobuf.message.Message):
    """Airdrops"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryAllAirdropsRequest = QueryAllAirdropsRequest

@typing.final
class QueryAllAirdropsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AIRDROPS_FIELD_NUMBER: builtins.int
    @property
    def airdrops(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.airdrop.airdrop_pb2.Airdrop]: ...
    def __init__(
        self,
        *,
        airdrops: collections.abc.Iterable[stride.airdrop.airdrop_pb2.Airdrop] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["airdrops", b"airdrops"]) -> None: ...

global___QueryAllAirdropsResponse = QueryAllAirdropsResponse

@typing.final
class QueryUserAllocationRequest(google.protobuf.message.Message):
    """UserAllocation"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AIRDROP_ID_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    airdrop_id: builtins.str
    address: builtins.str
    def __init__(
        self,
        *,
        airdrop_id: builtins.str = ...,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "airdrop_id", b"airdrop_id"]) -> None: ...

global___QueryUserAllocationRequest = QueryUserAllocationRequest

@typing.final
class QueryUserAllocationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ALLOCATION_FIELD_NUMBER: builtins.int
    @property
    def user_allocation(self) -> stride.airdrop.airdrop_pb2.UserAllocation: ...
    def __init__(
        self,
        *,
        user_allocation: stride.airdrop.airdrop_pb2.UserAllocation | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["user_allocation", b"user_allocation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["user_allocation", b"user_allocation"]) -> None: ...

global___QueryUserAllocationResponse = QueryUserAllocationResponse

@typing.final
class QueryUserAllocationsRequest(google.protobuf.message.Message):
    """UserAllocations"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address"]) -> None: ...

global___QueryUserAllocationsRequest = QueryUserAllocationsRequest

@typing.final
class QueryUserAllocationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ALLOCATIONS_FIELD_NUMBER: builtins.int
    @property
    def user_allocations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.airdrop.airdrop_pb2.UserAllocation]: ...
    def __init__(
        self,
        *,
        user_allocations: collections.abc.Iterable[stride.airdrop.airdrop_pb2.UserAllocation] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["user_allocations", b"user_allocations"]) -> None: ...

global___QueryUserAllocationsResponse = QueryUserAllocationsResponse

@typing.final
class QueryAllAllocationsRequest(google.protobuf.message.Message):
    """AllAllocations"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AIRDROP_ID_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    airdrop_id: builtins.str
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        airdrop_id: builtins.str = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["airdrop_id", b"airdrop_id", "pagination", b"pagination"]) -> None: ...

global___QueryAllAllocationsRequest = QueryAllAllocationsRequest

@typing.final
class QueryAllAllocationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALLOCATIONS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def allocations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.airdrop.airdrop_pb2.UserAllocation]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        allocations: collections.abc.Iterable[stride.airdrop.airdrop_pb2.UserAllocation] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["allocations", b"allocations", "pagination", b"pagination"]) -> None: ...

global___QueryAllAllocationsResponse = QueryAllAllocationsResponse

@typing.final
class QueryUserSummaryRequest(google.protobuf.message.Message):
    """UserSummary"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AIRDROP_ID_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    airdrop_id: builtins.str
    address: builtins.str
    def __init__(
        self,
        *,
        airdrop_id: builtins.str = ...,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "airdrop_id", b"airdrop_id"]) -> None: ...

global___QueryUserSummaryRequest = QueryUserSummaryRequest

@typing.final
class QueryUserSummaryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLAIM_TYPE_FIELD_NUMBER: builtins.int
    CLAIMED_FIELD_NUMBER: builtins.int
    FORFEITED_FIELD_NUMBER: builtins.int
    REMAINING_FIELD_NUMBER: builtins.int
    CLAIMABLE_FIELD_NUMBER: builtins.int
    claim_type: builtins.str
    """The claim type (claim daily or claim early)"""
    claimed: builtins.str
    """The total rewards claimed so far"""
    forfeited: builtins.str
    """The total rewards forfeited (in the case of claiming early)"""
    remaining: builtins.str
    """The total rewards remaining"""
    claimable: builtins.str
    """The total rewards that can be claimed right now"""
    def __init__(
        self,
        *,
        claim_type: builtins.str = ...,
        claimed: builtins.str = ...,
        forfeited: builtins.str = ...,
        remaining: builtins.str = ...,
        claimable: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["claim_type", b"claim_type", "claimable", b"claimable", "claimed", b"claimed", "forfeited", b"forfeited", "remaining", b"remaining"]) -> None: ...

global___QueryUserSummaryResponse = QueryUserSummaryResponse
