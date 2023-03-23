"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class QuerySpotPriceRequest(google.protobuf.message.Message):
    """QuerySpotPriceRequest defines the gRPC request structure for a SpotPrice
    query.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    BASE_ASSET_DENOM_FIELD_NUMBER: builtins.int
    QUOTE_ASSET_DENOM_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    base_asset_denom: builtins.str
    quote_asset_denom: builtins.str
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        base_asset_denom: builtins.str = ...,
        quote_asset_denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_asset_denom", b"base_asset_denom", "pool_id", b"pool_id", "quote_asset_denom", b"quote_asset_denom"]) -> None: ...

global___QuerySpotPriceRequest = QuerySpotPriceRequest

@typing_extensions.final
class QuerySpotPriceResponse(google.protobuf.message.Message):
    """QuerySpotPriceResponse defines the gRPC response structure for a SpotPrice
    query.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPOT_PRICE_FIELD_NUMBER: builtins.int
    spot_price: builtins.str
    """String of the Dec. Ex) 10.203uatom"""
    def __init__(
        self,
        *,
        spot_price: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["spot_price", b"spot_price"]) -> None: ...

global___QuerySpotPriceResponse = QuerySpotPriceResponse
