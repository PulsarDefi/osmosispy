"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import dydxprotocol.feetiers.params_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MsgUpdatePerpetualFeeParams(google.protobuf.message.Message):
    """MsgUpdatePerpetualFeeParams is the Msg/UpdatePerpetualFeeParams request type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    authority: builtins.str
    @property
    def params(self) -> dydxprotocol.feetiers.params_pb2.PerpetualFeeParams:
        """Defines the parameters to update. All parameters must be supplied."""

    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        params: dydxprotocol.feetiers.params_pb2.PerpetualFeeParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authority", b"authority", "params", b"params"]) -> None: ...

global___MsgUpdatePerpetualFeeParams = MsgUpdatePerpetualFeeParams

@typing.final
class MsgUpdatePerpetualFeeParamsResponse(google.protobuf.message.Message):
    """MsgUpdatePerpetualFeeParamsResponse is the Msg/UpdatePerpetualFeeParams
    response type.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgUpdatePerpetualFeeParamsResponse = MsgUpdatePerpetualFeeParamsResponse
