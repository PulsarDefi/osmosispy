"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import stride.autopilot.params_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the claim module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> stride.autopilot.params_pb2.Params:
        """params defines all the parameters of the module."""

    def __init__(
        self,
        *,
        params: stride.autopilot.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params"]) -> None: ...

global___GenesisState = GenesisState
