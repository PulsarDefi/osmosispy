"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import dydxprotocol.ratelimit.limit_params_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the ratelimit module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIMIT_PARAMS_LIST_FIELD_NUMBER: builtins.int
    @property
    def limit_params_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.ratelimit.limit_params_pb2.LimitParams]:
        """limit_params_list defines the list of `LimitParams` at genesis."""

    def __init__(
        self,
        *,
        limit_params_list: collections.abc.Iterable[dydxprotocol.ratelimit.limit_params_pb2.LimitParams] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["limit_params_list", b"limit_params_list"]) -> None: ...

global___GenesisState = GenesisState
