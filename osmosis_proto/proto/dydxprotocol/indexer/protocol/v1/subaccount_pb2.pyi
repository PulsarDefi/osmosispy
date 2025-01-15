"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class IndexerSubaccountId(google.protobuf.message.Message):
    """Initial copy of protos from dYdX chain application state protos for the
    subaccount module for use to send Indexer specific messages. Do not make any
    breaking changes to these protos, a new version should be created if a
    breaking change is needed.

    IndexerSubaccountId defines a unique identifier for a Subaccount.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_FIELD_NUMBER: builtins.int
    NUMBER_FIELD_NUMBER: builtins.int
    owner: builtins.str
    """The address of the wallet that owns this subaccount."""
    number: builtins.int
    """< 128 Since 128 should be enough to start and it fits within
    1 Byte (1 Bit needed to indicate that the first byte is the last).
    """
    def __init__(
        self,
        *,
        owner: builtins.str = ...,
        number: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["number", b"number", "owner", b"owner"]) -> None: ...

global___IndexerSubaccountId = IndexerSubaccountId

@typing.final
class IndexerPerpetualPosition(google.protobuf.message.Message):
    """IndexerPerpetualPosition are an account’s positions of a `Perpetual`.
    Therefore they hold any information needed to trade perpetuals.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PERPETUAL_ID_FIELD_NUMBER: builtins.int
    QUANTUMS_FIELD_NUMBER: builtins.int
    FUNDING_INDEX_FIELD_NUMBER: builtins.int
    FUNDING_PAYMENT_FIELD_NUMBER: builtins.int
    perpetual_id: builtins.int
    """The `Id` of the `Perpetual`."""
    quantums: builtins.bytes
    """The size of the position in base quantums."""
    funding_index: builtins.bytes
    """The funding_index of the `Perpetual` the last time this position was
    settled.
    """
    funding_payment: builtins.bytes
    """Amount of funding payment (in quote quantums).
    Note: 1. this field is not cumulative.
    2. a positive value means funding payment was paid out and
    a negative value means funding payment was received.
    """
    def __init__(
        self,
        *,
        perpetual_id: builtins.int = ...,
        quantums: builtins.bytes = ...,
        funding_index: builtins.bytes = ...,
        funding_payment: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["funding_index", b"funding_index", "funding_payment", b"funding_payment", "perpetual_id", b"perpetual_id", "quantums", b"quantums"]) -> None: ...

global___IndexerPerpetualPosition = IndexerPerpetualPosition

@typing.final
class IndexerAssetPosition(google.protobuf.message.Message):
    """IndexerAssetPosition define an account’s positions of an `Asset`.
    Therefore they hold any information needed to trade on Spot and Margin.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSET_ID_FIELD_NUMBER: builtins.int
    QUANTUMS_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    asset_id: builtins.int
    """The `Id` of the `Asset`."""
    quantums: builtins.bytes
    """The absolute size of the position in base quantums."""
    index: builtins.int
    """The `Index` (either `LongIndex` or `ShortIndex`) of the `Asset` the last
    time this position was settled
    TODO(DEC-582): pending margin trading being added.
    """
    def __init__(
        self,
        *,
        asset_id: builtins.int = ...,
        quantums: builtins.bytes = ...,
        index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["asset_id", b"asset_id", "index", b"index", "quantums", b"quantums"]) -> None: ...

global___IndexerAssetPosition = IndexerAssetPosition
