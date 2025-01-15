"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import dydxprotocol.affiliates.affiliates_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class AffiliateInfoRequest(google.protobuf.message.Message):
    """AffiliateInfoRequest is the request type for the Query/AffiliateInfo RPC
    method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address"]) -> None: ...

global___AffiliateInfoRequest = AffiliateInfoRequest

@typing.final
class AffiliateInfoResponse(google.protobuf.message.Message):
    """AffiliateInfoResponse is the response type for the Query/AffiliateInfo RPC
    method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IS_WHITELISTED_FIELD_NUMBER: builtins.int
    TIER_FIELD_NUMBER: builtins.int
    FEE_SHARE_PPM_FIELD_NUMBER: builtins.int
    REFERRED_VOLUME_FIELD_NUMBER: builtins.int
    STAKED_AMOUNT_FIELD_NUMBER: builtins.int
    is_whitelisted: builtins.bool
    """Whether the address is a whitelisted affiliate (VIP)."""
    tier: builtins.int
    """If `is_whiteslisted == false`, the affiliate's tier qualified through
    regular affiliate program.
    """
    fee_share_ppm: builtins.int
    """The affiliate's taker fee share in parts-per-million (for both VIP and
    regular affiliate).
    """
    referred_volume: builtins.bytes
    """The affiliate's all-time referred volume in quote quantums."""
    staked_amount: builtins.bytes
    """The affiliate's currently staked native tokens (in whole coins)."""
    def __init__(
        self,
        *,
        is_whitelisted: builtins.bool = ...,
        tier: builtins.int = ...,
        fee_share_ppm: builtins.int = ...,
        referred_volume: builtins.bytes = ...,
        staked_amount: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["fee_share_ppm", b"fee_share_ppm", "is_whitelisted", b"is_whitelisted", "referred_volume", b"referred_volume", "staked_amount", b"staked_amount", "tier", b"tier"]) -> None: ...

global___AffiliateInfoResponse = AffiliateInfoResponse

@typing.final
class ReferredByRequest(google.protobuf.message.Message):
    """ReferredByRequest is the request type for the Query/ReferredBy RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    """The address to query."""
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address"]) -> None: ...

global___ReferredByRequest = ReferredByRequest

@typing.final
class ReferredByResponse(google.protobuf.message.Message):
    """ReferredByResponse is the response type for the Query/ReferredBy RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AFFILIATE_ADDRESS_FIELD_NUMBER: builtins.int
    affiliate_address: builtins.str
    """The affiliate's address that referred the queried address."""
    def __init__(
        self,
        *,
        affiliate_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["affiliate_address", b"affiliate_address"]) -> None: ...

global___ReferredByResponse = ReferredByResponse

@typing.final
class AllAffiliateTiersRequest(google.protobuf.message.Message):
    """AllAffiliateTiersRequest is the request type for the Query/AllAffiliateTiers
    RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AllAffiliateTiersRequest = AllAffiliateTiersRequest

@typing.final
class AllAffiliateTiersResponse(google.protobuf.message.Message):
    """AllAffiliateTiersResponse is the response type for the
    Query/AllAffiliateTiers RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIERS_FIELD_NUMBER: builtins.int
    @property
    def tiers(self) -> dydxprotocol.affiliates.affiliates_pb2.AffiliateTiers:
        """All affiliate tiers information."""

    def __init__(
        self,
        *,
        tiers: dydxprotocol.affiliates.affiliates_pb2.AffiliateTiers | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["tiers", b"tiers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["tiers", b"tiers"]) -> None: ...

global___AllAffiliateTiersResponse = AllAffiliateTiersResponse

@typing.final
class AffiliateWhitelistRequest(google.protobuf.message.Message):
    """AffiliateWhitelistRequest is the request type for the
    Query/AffiliateWhitelist RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AffiliateWhitelistRequest = AffiliateWhitelistRequest

@typing.final
class AffiliateWhitelistResponse(google.protobuf.message.Message):
    """AffiliateWhitelistResponse is the response type for the
    Query/AffiliateWhitelist RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WHITELIST_FIELD_NUMBER: builtins.int
    @property
    def whitelist(self) -> dydxprotocol.affiliates.affiliates_pb2.AffiliateWhitelist: ...
    def __init__(
        self,
        *,
        whitelist: dydxprotocol.affiliates.affiliates_pb2.AffiliateWhitelist | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["whitelist", b"whitelist"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["whitelist", b"whitelist"]) -> None: ...

global___AffiliateWhitelistResponse = AffiliateWhitelistResponse
