"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import dydxprotocol.vest.vest_entry_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the vest module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VEST_ENTRIES_FIELD_NUMBER: builtins.int
    @property
    def vest_entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.vest.vest_entry_pb2.VestEntry]:
        """The vest entries at genesis."""

    def __init__(
        self,
        *,
        vest_entries: collections.abc.Iterable[dydxprotocol.vest.vest_entry_pb2.VestEntry] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["vest_entries", b"vest_entries"]) -> None: ...

global___GenesisState = GenesisState
