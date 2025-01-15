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
class LiquidationsConfig(google.protobuf.message.Message):
    """LiquidationsConfig stores all configurable fields related to liquidations."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_LIQUIDATION_FEE_PPM_FIELD_NUMBER: builtins.int
    POSITION_BLOCK_LIMITS_FIELD_NUMBER: builtins.int
    SUBACCOUNT_BLOCK_LIMITS_FIELD_NUMBER: builtins.int
    FILLABLE_PRICE_CONFIG_FIELD_NUMBER: builtins.int
    max_liquidation_fee_ppm: builtins.int
    """The maximum liquidation fee (in parts-per-million). This fee goes
    100% to the insurance fund.
    """
    @property
    def position_block_limits(self) -> global___PositionBlockLimits:
        """Limits around how much of a single position can be liquidated
        within a single block.
        """

    @property
    def subaccount_block_limits(self) -> global___SubaccountBlockLimits:
        """Limits around how many quote quantums from a single subaccount can
        be liquidated within a single block.
        """

    @property
    def fillable_price_config(self) -> global___FillablePriceConfig:
        """Config about how the fillable-price spread from the oracle price
        increases based on the adjusted bankruptcy rating of the subaccount.
        """

    def __init__(
        self,
        *,
        max_liquidation_fee_ppm: builtins.int = ...,
        position_block_limits: global___PositionBlockLimits | None = ...,
        subaccount_block_limits: global___SubaccountBlockLimits | None = ...,
        fillable_price_config: global___FillablePriceConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["fillable_price_config", b"fillable_price_config", "position_block_limits", b"position_block_limits", "subaccount_block_limits", b"subaccount_block_limits"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["fillable_price_config", b"fillable_price_config", "max_liquidation_fee_ppm", b"max_liquidation_fee_ppm", "position_block_limits", b"position_block_limits", "subaccount_block_limits", b"subaccount_block_limits"]) -> None: ...

global___LiquidationsConfig = LiquidationsConfig

@typing.final
class PositionBlockLimits(google.protobuf.message.Message):
    """PositionBlockLimits stores all configurable fields related to limits
    around how much of a single position can be liquidated within a single block.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MIN_POSITION_NOTIONAL_LIQUIDATED_FIELD_NUMBER: builtins.int
    MAX_POSITION_PORTION_LIQUIDATED_PPM_FIELD_NUMBER: builtins.int
    min_position_notional_liquidated: builtins.int
    """The minimum amount of quantums to liquidate for each message (in
    quote quantums).
    Overridden by the maximum size of the position.
    """
    max_position_portion_liquidated_ppm: builtins.int
    """The maximum portion of the position liquidated (in parts-per-
    million). Overridden by min_position_notional_liquidated.
    """
    def __init__(
        self,
        *,
        min_position_notional_liquidated: builtins.int = ...,
        max_position_portion_liquidated_ppm: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["max_position_portion_liquidated_ppm", b"max_position_portion_liquidated_ppm", "min_position_notional_liquidated", b"min_position_notional_liquidated"]) -> None: ...

global___PositionBlockLimits = PositionBlockLimits

@typing.final
class SubaccountBlockLimits(google.protobuf.message.Message):
    """SubaccountBlockLimits stores all configurable fields related to limits
    around how many quote quantums from a single subaccount can
    be liquidated within a single block.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_NOTIONAL_LIQUIDATED_FIELD_NUMBER: builtins.int
    MAX_QUANTUMS_INSURANCE_LOST_FIELD_NUMBER: builtins.int
    max_notional_liquidated: builtins.int
    """The maximum notional amount that a single subaccount can have
    liquidated (in quote quantums) per block.
    """
    max_quantums_insurance_lost: builtins.int
    """The maximum insurance-fund payout amount for a given subaccount
    per block. I.e. how much it can cover for that subaccount.
    """
    def __init__(
        self,
        *,
        max_notional_liquidated: builtins.int = ...,
        max_quantums_insurance_lost: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["max_notional_liquidated", b"max_notional_liquidated", "max_quantums_insurance_lost", b"max_quantums_insurance_lost"]) -> None: ...

global___SubaccountBlockLimits = SubaccountBlockLimits

@typing.final
class FillablePriceConfig(google.protobuf.message.Message):
    """FillablePriceConfig stores all configurable fields related to calculating
    the fillable price for liquidating a position.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BANKRUPTCY_ADJUSTMENT_PPM_FIELD_NUMBER: builtins.int
    SPREAD_TO_MAINTENANCE_MARGIN_RATIO_PPM_FIELD_NUMBER: builtins.int
    bankruptcy_adjustment_ppm: builtins.int
    """The rate at which the Adjusted Bankruptcy Rating increases."""
    spread_to_maintenance_margin_ratio_ppm: builtins.int
    """The maximum value that the liquidation spread can take, as
    a ratio against the position's maintenance margin.
    """
    def __init__(
        self,
        *,
        bankruptcy_adjustment_ppm: builtins.int = ...,
        spread_to_maintenance_margin_ratio_ppm: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["bankruptcy_adjustment_ppm", b"bankruptcy_adjustment_ppm", "spread_to_maintenance_margin_ratio_ppm", b"spread_to_maintenance_margin_ratio_ppm"]) -> None: ...

global___FillablePriceConfig = FillablePriceConfig
