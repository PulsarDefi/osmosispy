"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BridgeEventInfo(google.protobuf.message.Message):
    """BridgeEventInfo stores information about the most recently processed bridge
    event.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEXT_ID_FIELD_NUMBER: builtins.int
    ETH_BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    next_id: builtins.int
    """The next event id (the last processed id plus one) of the logs from the
    Ethereum contract.
    """
    eth_block_height: builtins.int
    """The Ethereum block height of the most recently processed bridge event."""
    def __init__(
        self,
        *,
        next_id: builtins.int = ...,
        eth_block_height: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["eth_block_height", b"eth_block_height", "next_id", b"next_id"]) -> None: ...

global___BridgeEventInfo = BridgeEventInfo
