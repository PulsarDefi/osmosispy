"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import osmosis.lockup.lock_pb2
import osmosis.lockup.params_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ModuleBalanceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ModuleBalanceRequest = ModuleBalanceRequest

@typing_extensions.final
class ModuleBalanceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COINS_FIELD_NUMBER: builtins.int
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["coins", b"coins"]) -> None: ...

global___ModuleBalanceResponse = ModuleBalanceResponse

@typing_extensions.final
class ModuleLockedAmountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ModuleLockedAmountRequest = ModuleLockedAmountRequest

@typing_extensions.final
class ModuleLockedAmountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COINS_FIELD_NUMBER: builtins.int
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["coins", b"coins"]) -> None: ...

global___ModuleLockedAmountResponse = ModuleLockedAmountResponse

@typing_extensions.final
class AccountUnlockableCoinsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    owner: builtins.str
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["owner", b"owner"]) -> None: ...

global___AccountUnlockableCoinsRequest = AccountUnlockableCoinsRequest

@typing_extensions.final
class AccountUnlockableCoinsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COINS_FIELD_NUMBER: builtins.int
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["coins", b"coins"]) -> None: ...

global___AccountUnlockableCoinsResponse = AccountUnlockableCoinsResponse

@typing_extensions.final
class AccountUnlockingCoinsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    owner: builtins.str
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["owner", b"owner"]) -> None: ...

global___AccountUnlockingCoinsRequest = AccountUnlockingCoinsRequest

@typing_extensions.final
class AccountUnlockingCoinsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COINS_FIELD_NUMBER: builtins.int
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["coins", b"coins"]) -> None: ...

global___AccountUnlockingCoinsResponse = AccountUnlockingCoinsResponse

@typing_extensions.final
class AccountLockedCoinsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    owner: builtins.str
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["owner", b"owner"]) -> None: ...

global___AccountLockedCoinsRequest = AccountLockedCoinsRequest

@typing_extensions.final
class AccountLockedCoinsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COINS_FIELD_NUMBER: builtins.int
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["coins", b"coins"]) -> None: ...

global___AccountLockedCoinsResponse = AccountLockedCoinsResponse

@typing_extensions.final
class AccountLockedPastTimeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    owner: builtins.str
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["owner", b"owner", "timestamp", b"timestamp"]) -> None: ...

global___AccountLockedPastTimeRequest = AccountLockedPastTimeRequest

@typing_extensions.final
class AccountLockedPastTimeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCKS_FIELD_NUMBER: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.PeriodLock]: ...
    def __init__(
        self,
        *,
        locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.PeriodLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locks", b"locks"]) -> None: ...

global___AccountLockedPastTimeResponse = AccountLockedPastTimeResponse

@typing_extensions.final
class AccountLockedPastTimeNotUnlockingOnlyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    owner: builtins.str
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["owner", b"owner", "timestamp", b"timestamp"]) -> None: ...

global___AccountLockedPastTimeNotUnlockingOnlyRequest = AccountLockedPastTimeNotUnlockingOnlyRequest

@typing_extensions.final
class AccountLockedPastTimeNotUnlockingOnlyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCKS_FIELD_NUMBER: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.PeriodLock]: ...
    def __init__(
        self,
        *,
        locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.PeriodLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locks", b"locks"]) -> None: ...

global___AccountLockedPastTimeNotUnlockingOnlyResponse = AccountLockedPastTimeNotUnlockingOnlyResponse

@typing_extensions.final
class AccountUnlockedBeforeTimeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    owner: builtins.str
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["owner", b"owner", "timestamp", b"timestamp"]) -> None: ...

global___AccountUnlockedBeforeTimeRequest = AccountUnlockedBeforeTimeRequest

@typing_extensions.final
class AccountUnlockedBeforeTimeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCKS_FIELD_NUMBER: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.PeriodLock]: ...
    def __init__(
        self,
        *,
        locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.PeriodLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locks", b"locks"]) -> None: ...

global___AccountUnlockedBeforeTimeResponse = AccountUnlockedBeforeTimeResponse

@typing_extensions.final
class AccountLockedPastTimeDenomRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    DENOM_FIELD_NUMBER: builtins.int
    owner: builtins.str
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    denom: builtins.str
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        denom: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom", "owner", b"owner", "timestamp", b"timestamp"]) -> None: ...

global___AccountLockedPastTimeDenomRequest = AccountLockedPastTimeDenomRequest

@typing_extensions.final
class AccountLockedPastTimeDenomResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCKS_FIELD_NUMBER: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.PeriodLock]: ...
    def __init__(
        self,
        *,
        locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.PeriodLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locks", b"locks"]) -> None: ...

global___AccountLockedPastTimeDenomResponse = AccountLockedPastTimeDenomResponse

@typing_extensions.final
class LockedDenomRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DENOM_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    denom: builtins.str
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        denom: builtins.str = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom", "duration", b"duration"]) -> None: ...

global___LockedDenomRequest = LockedDenomRequest

@typing_extensions.final
class LockedDenomResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AMOUNT_FIELD_NUMBER: builtins.int
    amount: builtins.str
    def __init__(
        self,
        *,
        amount: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount"]) -> None: ...

global___LockedDenomResponse = LockedDenomResponse

@typing_extensions.final
class LockedRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCK_ID_FIELD_NUMBER: builtins.int
    lock_id: builtins.int
    def __init__(
        self,
        *,
        lock_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["lock_id", b"lock_id"]) -> None: ...

global___LockedRequest = LockedRequest

@typing_extensions.final
class LockedResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCK_FIELD_NUMBER: builtins.int
    @property
    def lock(self) -> osmosis.lockup.lock_pb2.PeriodLock: ...
    def __init__(
        self,
        *,
        lock: osmosis.lockup.lock_pb2.PeriodLock | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["lock", b"lock"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["lock", b"lock"]) -> None: ...

global___LockedResponse = LockedResponse

@typing_extensions.final
class SyntheticLockupsByLockupIDRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCK_ID_FIELD_NUMBER: builtins.int
    lock_id: builtins.int
    def __init__(
        self,
        *,
        lock_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["lock_id", b"lock_id"]) -> None: ...

global___SyntheticLockupsByLockupIDRequest = SyntheticLockupsByLockupIDRequest

@typing_extensions.final
class SyntheticLockupsByLockupIDResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SYNTHETIC_LOCKS_FIELD_NUMBER: builtins.int
    @property
    def synthetic_locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.SyntheticLock]: ...
    def __init__(
        self,
        *,
        synthetic_locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.SyntheticLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["synthetic_locks", b"synthetic_locks"]) -> None: ...

global___SyntheticLockupsByLockupIDResponse = SyntheticLockupsByLockupIDResponse

@typing_extensions.final
class AccountLockedLongerDurationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    owner: builtins.str
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration", b"duration", "owner", b"owner"]) -> None: ...

global___AccountLockedLongerDurationRequest = AccountLockedLongerDurationRequest

@typing_extensions.final
class AccountLockedLongerDurationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCKS_FIELD_NUMBER: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.PeriodLock]: ...
    def __init__(
        self,
        *,
        locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.PeriodLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locks", b"locks"]) -> None: ...

global___AccountLockedLongerDurationResponse = AccountLockedLongerDurationResponse

@typing_extensions.final
class AccountLockedDurationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    owner: builtins.str
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration", b"duration", "owner", b"owner"]) -> None: ...

global___AccountLockedDurationRequest = AccountLockedDurationRequest

@typing_extensions.final
class AccountLockedDurationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCKS_FIELD_NUMBER: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.PeriodLock]: ...
    def __init__(
        self,
        *,
        locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.PeriodLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locks", b"locks"]) -> None: ...

global___AccountLockedDurationResponse = AccountLockedDurationResponse

@typing_extensions.final
class AccountLockedLongerDurationNotUnlockingOnlyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    owner: builtins.str
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration", b"duration", "owner", b"owner"]) -> None: ...

global___AccountLockedLongerDurationNotUnlockingOnlyRequest = AccountLockedLongerDurationNotUnlockingOnlyRequest

@typing_extensions.final
class AccountLockedLongerDurationNotUnlockingOnlyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCKS_FIELD_NUMBER: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.PeriodLock]: ...
    def __init__(
        self,
        *,
        locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.PeriodLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locks", b"locks"]) -> None: ...

global___AccountLockedLongerDurationNotUnlockingOnlyResponse = AccountLockedLongerDurationNotUnlockingOnlyResponse

@typing_extensions.final
class AccountLockedLongerDurationDenomRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    DENOM_FIELD_NUMBER: builtins.int
    owner: builtins.str
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration: ...
    denom: builtins.str
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
        denom: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom", "duration", b"duration", "owner", b"owner"]) -> None: ...

global___AccountLockedLongerDurationDenomRequest = AccountLockedLongerDurationDenomRequest

@typing_extensions.final
class AccountLockedLongerDurationDenomResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCKS_FIELD_NUMBER: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.PeriodLock]: ...
    def __init__(
        self,
        *,
        locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.PeriodLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locks", b"locks"]) -> None: ...

global___AccountLockedLongerDurationDenomResponse = AccountLockedLongerDurationDenomResponse

@typing_extensions.final
class QueryParamsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryParamsRequest = QueryParamsRequest

@typing_extensions.final
class QueryParamsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> osmosis.lockup.params_pb2.Params: ...
    def __init__(
        self,
        *,
        params: osmosis.lockup.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params", b"params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse
