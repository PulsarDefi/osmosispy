"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class PerpetualClobMetadata(google.protobuf.message.Message):
    """PerpetualClobMetadata contains metadata for a `ClobPair`
    representing a Perpetual product.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PERPETUAL_ID_FIELD_NUMBER: builtins.int
    perpetual_id: builtins.int
    """Id of the Perpetual the CLOB allows trading of."""
    def __init__(
        self,
        *,
        perpetual_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["perpetual_id", b"perpetual_id"]) -> None: ...

global___PerpetualClobMetadata = PerpetualClobMetadata

@typing.final
class SpotClobMetadata(google.protobuf.message.Message):
    """PerpetualClobMetadata contains metadata for a `ClobPair`
    representing a Spot product.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_ASSET_ID_FIELD_NUMBER: builtins.int
    QUOTE_ASSET_ID_FIELD_NUMBER: builtins.int
    base_asset_id: builtins.int
    """Id of the base Asset in the trading pair."""
    quote_asset_id: builtins.int
    """Id of the quote Asset in the trading pair."""
    def __init__(
        self,
        *,
        base_asset_id: builtins.int = ...,
        quote_asset_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["base_asset_id", b"base_asset_id", "quote_asset_id", b"quote_asset_id"]) -> None: ...

global___SpotClobMetadata = SpotClobMetadata

@typing.final
class ClobPair(google.protobuf.message.Message):
    """ClobPair represents a single CLOB pair for a given product
    in state.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ClobPair._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: ClobPair._Status.ValueType  # 0
        """Default value. This value is invalid and unused."""
        STATUS_ACTIVE: ClobPair._Status.ValueType  # 1
        """STATUS_ACTIVE represents an active clob pair."""
        STATUS_PAUSED: ClobPair._Status.ValueType  # 2
        """STATUS_PAUSED behavior is unfinalized.
        TODO(DEC-600): update this documentation.
        """
        STATUS_CANCEL_ONLY: ClobPair._Status.ValueType  # 3
        """STATUS_CANCEL_ONLY behavior is unfinalized.
        TODO(DEC-600): update this documentation.
        """
        STATUS_POST_ONLY: ClobPair._Status.ValueType  # 4
        """STATUS_POST_ONLY behavior is unfinalized.
        TODO(DEC-600): update this documentation.
        """
        STATUS_INITIALIZING: ClobPair._Status.ValueType  # 5
        """STATUS_INITIALIZING represents a newly-added clob pair.
        Clob pairs in this state only accept orders which are
        both short-term and post-only.
        """
        STATUS_FINAL_SETTLEMENT: ClobPair._Status.ValueType  # 6
        """STATUS_FINAL_SETTLEMENT represents a clob pair which is deactivated
        and trading has ceased. All open positions will be closed by the
        protocol. Open stateful orders will be cancelled. Open short-term
        orders will be left to expire.
        """

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        """Status of the CLOB."""

    STATUS_UNSPECIFIED: ClobPair.Status.ValueType  # 0
    """Default value. This value is invalid and unused."""
    STATUS_ACTIVE: ClobPair.Status.ValueType  # 1
    """STATUS_ACTIVE represents an active clob pair."""
    STATUS_PAUSED: ClobPair.Status.ValueType  # 2
    """STATUS_PAUSED behavior is unfinalized.
    TODO(DEC-600): update this documentation.
    """
    STATUS_CANCEL_ONLY: ClobPair.Status.ValueType  # 3
    """STATUS_CANCEL_ONLY behavior is unfinalized.
    TODO(DEC-600): update this documentation.
    """
    STATUS_POST_ONLY: ClobPair.Status.ValueType  # 4
    """STATUS_POST_ONLY behavior is unfinalized.
    TODO(DEC-600): update this documentation.
    """
    STATUS_INITIALIZING: ClobPair.Status.ValueType  # 5
    """STATUS_INITIALIZING represents a newly-added clob pair.
    Clob pairs in this state only accept orders which are
    both short-term and post-only.
    """
    STATUS_FINAL_SETTLEMENT: ClobPair.Status.ValueType  # 6
    """STATUS_FINAL_SETTLEMENT represents a clob pair which is deactivated
    and trading has ceased. All open positions will be closed by the
    protocol. Open stateful orders will be cancelled. Open short-term
    orders will be left to expire.
    """

    ID_FIELD_NUMBER: builtins.int
    PERPETUAL_CLOB_METADATA_FIELD_NUMBER: builtins.int
    SPOT_CLOB_METADATA_FIELD_NUMBER: builtins.int
    STEP_BASE_QUANTUMS_FIELD_NUMBER: builtins.int
    SUBTICKS_PER_TICK_FIELD_NUMBER: builtins.int
    QUANTUM_CONVERSION_EXPONENT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    id: builtins.int
    """ID of the orderbook that stores all resting liquidity for this CLOB."""
    step_base_quantums: builtins.int
    """Minimum increment in the size of orders on the CLOB, in base quantums."""
    subticks_per_tick: builtins.int
    """Defines the tick size of the orderbook by defining how many subticks
    are in one tick. That is, the subticks of any valid order must be a
    multiple of this value. Generally this value should start `>= 100`to
    allow room for decreasing it.
    """
    quantum_conversion_exponent: builtins.int
    """`10^Exponent` gives the number of QuoteQuantums traded per BaseQuantum
    per Subtick.
    """
    status: global___ClobPair.Status.ValueType
    @property
    def perpetual_clob_metadata(self) -> global___PerpetualClobMetadata: ...
    @property
    def spot_clob_metadata(self) -> global___SpotClobMetadata: ...
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        perpetual_clob_metadata: global___PerpetualClobMetadata | None = ...,
        spot_clob_metadata: global___SpotClobMetadata | None = ...,
        step_base_quantums: builtins.int = ...,
        subticks_per_tick: builtins.int = ...,
        quantum_conversion_exponent: builtins.int = ...,
        status: global___ClobPair.Status.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "perpetual_clob_metadata", b"perpetual_clob_metadata", "spot_clob_metadata", b"spot_clob_metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "metadata", b"metadata", "perpetual_clob_metadata", b"perpetual_clob_metadata", "quantum_conversion_exponent", b"quantum_conversion_exponent", "spot_clob_metadata", b"spot_clob_metadata", "status", b"status", "step_base_quantums", b"step_base_quantums", "subticks_per_tick", b"subticks_per_tick"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["metadata", b"metadata"]) -> typing.Literal["perpetual_clob_metadata", "spot_clob_metadata"] | None: ...

global___ClobPair = ClobPair
