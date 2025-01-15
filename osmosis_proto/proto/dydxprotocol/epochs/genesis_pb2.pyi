"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import dydxprotocol.epochs.epoch_info_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the epochs module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPOCH_INFO_LIST_FIELD_NUMBER: builtins.int
    @property
    def epoch_info_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dydxprotocol.epochs.epoch_info_pb2.EpochInfo]:
        """this line is used by starport scaffolding # genesis/proto/state"""

    def __init__(
        self,
        *,
        epoch_info_list: collections.abc.Iterable[dydxprotocol.epochs.epoch_info_pb2.EpochInfo] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["epoch_info_list", b"epoch_info_list"]) -> None: ...

global___GenesisState = GenesisState
