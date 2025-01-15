"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import dydxprotocol.subaccounts.subaccount_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the subaccounts module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def subaccounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.subaccounts.subaccount_pb2.Subaccount]: ...
    def __init__(
        self,
        *,
        subaccounts: collections.abc.Iterable[dydxprotocol.subaccounts.subaccount_pb2.Subaccount] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subaccounts", b"subaccounts"]) -> None: ...

global___GenesisState = GenesisState
