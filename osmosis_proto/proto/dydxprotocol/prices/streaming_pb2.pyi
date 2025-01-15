"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import dydxprotocol.prices.market_price_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class StreamPriceUpdate(google.protobuf.message.Message):
    """StreamPriceUpdate provides information on a price update."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MARKET_ID_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    SNAPSHOT_FIELD_NUMBER: builtins.int
    market_id: builtins.int
    """The `Id` of the `Market`."""
    snapshot: builtins.bool
    """Snapshot indicates if the response is from a snapshot of the price."""
    @property
    def price(self) -> dydxprotocol.prices.market_price_pb2.MarketPrice:
        """The updated price."""

    def __init__(
        self,
        *,
        market_id: builtins.int = ...,
        price: dydxprotocol.prices.market_price_pb2.MarketPrice | None = ...,
        snapshot: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["price", b"price"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["market_id", b"market_id", "price", b"price", "snapshot", b"snapshot"]) -> None: ...

global___StreamPriceUpdate = StreamPriceUpdate
