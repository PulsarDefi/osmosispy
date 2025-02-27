"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import dydxprotocol.blocktime.params_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MsgUpdateDowntimeParams(google.protobuf.message.Message):
    """MsgUpdateDowntimeParams is the Msg/UpdateDowntimeParams request type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    authority: builtins.str
    @property
    def params(self) -> dydxprotocol.blocktime.params_pb2.DowntimeParams:
        """Defines the parameters to update. All parameters must be supplied."""

    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        params: dydxprotocol.blocktime.params_pb2.DowntimeParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authority", b"authority", "params", b"params"]) -> None: ...

global___MsgUpdateDowntimeParams = MsgUpdateDowntimeParams

@typing.final
class MsgUpdateDowntimeParamsResponse(google.protobuf.message.Message):
    """MsgUpdateDowntimeParamsResponse is the Msg/UpdateDowntimeParams response
    type.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgUpdateDowntimeParamsResponse = MsgUpdateDowntimeParamsResponse

@typing.final
class MsgUpdateSynchronyParams(google.protobuf.message.Message):
    """MsgUpdateSynchronyParams is the Msg/UpdateSynchronyParams request type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    authority: builtins.str
    @property
    def params(self) -> dydxprotocol.blocktime.params_pb2.SynchronyParams:
        """Defines the parameters to update. All parameters must be supplied."""

    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        params: dydxprotocol.blocktime.params_pb2.SynchronyParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authority", b"authority", "params", b"params"]) -> None: ...

global___MsgUpdateSynchronyParams = MsgUpdateSynchronyParams

@typing.final
class MsgUpdateSynchronyParamsResponse(google.protobuf.message.Message):
    """MsgUpdateSynchronyParamsResponse is the Msg/UpdateSynchronyParams response
    type.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgUpdateSynchronyParamsResponse = MsgUpdateSynchronyParamsResponse
