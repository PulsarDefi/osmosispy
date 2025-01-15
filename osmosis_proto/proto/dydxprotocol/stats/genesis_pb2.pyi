"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import dydxprotocol.stats.params_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the stats module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> dydxprotocol.stats.params_pb2.Params:
        """The parameters of the module."""

    def __init__(
        self,
        *,
        params: dydxprotocol.stats.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params"]) -> None: ...

global___GenesisState = GenesisState
