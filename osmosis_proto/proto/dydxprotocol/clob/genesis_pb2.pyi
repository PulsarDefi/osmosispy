"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import dydxprotocol.clob.block_rate_limit_config_pb2
import dydxprotocol.clob.clob_pair_pb2
import dydxprotocol.clob.equity_tier_limit_config_pb2
import dydxprotocol.clob.liquidations_config_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the clob module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLOB_PAIRS_FIELD_NUMBER: builtins.int
    LIQUIDATIONS_CONFIG_FIELD_NUMBER: builtins.int
    BLOCK_RATE_LIMIT_CONFIG_FIELD_NUMBER: builtins.int
    EQUITY_TIER_LIMIT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def clob_pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.clob.clob_pair_pb2.ClobPair]: ...
    @property
    def liquidations_config(self) -> dydxprotocol.clob.liquidations_config_pb2.LiquidationsConfig: ...
    @property
    def block_rate_limit_config(self) -> dydxprotocol.clob.block_rate_limit_config_pb2.BlockRateLimitConfiguration: ...
    @property
    def equity_tier_limit_config(self) -> dydxprotocol.clob.equity_tier_limit_config_pb2.EquityTierLimitConfiguration: ...
    def __init__(
        self,
        *,
        clob_pairs: collections.abc.Iterable[dydxprotocol.clob.clob_pair_pb2.ClobPair] | None = ...,
        liquidations_config: dydxprotocol.clob.liquidations_config_pb2.LiquidationsConfig | None = ...,
        block_rate_limit_config: dydxprotocol.clob.block_rate_limit_config_pb2.BlockRateLimitConfiguration | None = ...,
        equity_tier_limit_config: dydxprotocol.clob.equity_tier_limit_config_pb2.EquityTierLimitConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["block_rate_limit_config", b"block_rate_limit_config", "equity_tier_limit_config", b"equity_tier_limit_config", "liquidations_config", b"liquidations_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["block_rate_limit_config", b"block_rate_limit_config", "clob_pairs", b"clob_pairs", "equity_tier_limit_config", b"equity_tier_limit_config", "liquidations_config", b"liquidations_config"]) -> None: ...

global___GenesisState = GenesisState
