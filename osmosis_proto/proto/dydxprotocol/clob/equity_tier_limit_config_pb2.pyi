"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class EquityTierLimitConfiguration(google.protobuf.message.Message):
    """Defines the set of equity tiers to limit how many open orders
    a subaccount is allowed to have.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHORT_TERM_ORDER_EQUITY_TIERS_FIELD_NUMBER: builtins.int
    STATEFUL_ORDER_EQUITY_TIERS_FIELD_NUMBER: builtins.int
    @property
    def short_term_order_equity_tiers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EquityTierLimit]:
        """How many short term stateful orders are allowed per equity tier.
        Specifying 0 values disables this limit.
        """

    @property
    def stateful_order_equity_tiers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EquityTierLimit]:
        """How many open stateful orders are allowed per equity tier.
        Specifying 0 values disables this limit.
        """

    def __init__(
        self,
        *,
        short_term_order_equity_tiers: collections.abc.Iterable[global___EquityTierLimit] | None = ...,
        stateful_order_equity_tiers: collections.abc.Iterable[global___EquityTierLimit] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["short_term_order_equity_tiers", b"short_term_order_equity_tiers", "stateful_order_equity_tiers", b"stateful_order_equity_tiers"]) -> None: ...

global___EquityTierLimitConfiguration = EquityTierLimitConfiguration

@typing.final
class EquityTierLimit(google.protobuf.message.Message):
    """Defines an equity tier limit."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USD_TNC_REQUIRED_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    usd_tnc_required: builtins.bytes
    """The total net collateral in USDC quote quantums of equity required."""
    limit: builtins.int
    """What the limit is for `usd_tnc_required`."""
    def __init__(
        self,
        *,
        usd_tnc_required: builtins.bytes = ...,
        limit: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["limit", b"limit", "usd_tnc_required", b"usd_tnc_required"]) -> None: ...

global___EquityTierLimit = EquityTierLimit
