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
class MsgUpdateParams(google.protobuf.message.Message):
    """MsgUpdateParams is the Msg/UpdateParams request type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    authority: builtins.str
    @property
    def params(self) -> dydxprotocol.stats.params_pb2.Params:
        """The parameters to update. Each field must be set."""

    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        params: dydxprotocol.stats.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authority", b"authority", "params", b"params"]) -> None: ...

global___MsgUpdateParams = MsgUpdateParams

@typing.final
class MsgUpdateParamsResponse(google.protobuf.message.Message):
    """MsgUpdateParamsResponse is the Msg/UpdateParams response type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgUpdateParamsResponse = MsgUpdateParamsResponse
