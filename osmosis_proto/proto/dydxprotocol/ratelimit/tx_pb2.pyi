"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import dydxprotocol.ratelimit.limit_params_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MsgSetLimitParams(google.protobuf.message.Message):
    """MsgSetLimitParams is the Msg/SetLimitParams request type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    LIMIT_PARAMS_FIELD_NUMBER: builtins.int
    authority: builtins.str
    @property
    def limit_params(self) -> dydxprotocol.ratelimit.limit_params_pb2.LimitParams:
        """Defines the parameters to set. All parameters must be supplied."""

    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        limit_params: dydxprotocol.ratelimit.limit_params_pb2.LimitParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["limit_params", b"limit_params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authority", b"authority", "limit_params", b"limit_params"]) -> None: ...

global___MsgSetLimitParams = MsgSetLimitParams

@typing.final
class MsgSetLimitParamsResponse(google.protobuf.message.Message):
    """MsgSetLimitParamsResponse is the Msg/SetLimitParams response type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgSetLimitParamsResponse = MsgSetLimitParamsResponse
