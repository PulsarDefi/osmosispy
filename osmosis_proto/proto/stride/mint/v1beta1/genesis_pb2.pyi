"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import stride.mint.v1beta1.mint_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the mint module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MINTER_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    REDUCTION_STARTED_EPOCH_FIELD_NUMBER: builtins.int
    reduction_started_epoch: builtins.int
    """current reduction period start epoch"""
    @property
    def minter(self) -> stride.mint.v1beta1.mint_pb2.Minter:
        """minter is a space for holding current rewards information."""

    @property
    def params(self) -> stride.mint.v1beta1.mint_pb2.Params:
        """params defines all the paramaters of the module."""

    def __init__(
        self,
        *,
        minter: stride.mint.v1beta1.mint_pb2.Minter | None = ...,
        params: stride.mint.v1beta1.mint_pb2.Params | None = ...,
        reduction_started_epoch: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["minter", b"minter", "params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["minter", b"minter", "params", b"params", "reduction_started_epoch", b"reduction_started_epoch"]) -> None: ...

global___GenesisState = GenesisState
