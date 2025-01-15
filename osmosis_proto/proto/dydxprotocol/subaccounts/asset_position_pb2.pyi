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
class AssetPosition(google.protobuf.message.Message):
    """AssetPositions define an account’s positions of an `Asset`.
    Therefore they hold any information needed to trade on Spot and Margin.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSET_ID_FIELD_NUMBER: builtins.int
    QUANTUMS_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    asset_id: builtins.int
    """The `Id` of the `Asset`."""
    quantums: builtins.bytes
    """The absolute size of the position in base quantums."""
    index: builtins.int
    """The `Index` (either `LongIndex` or `ShortIndex`) of the `Asset` the last
    time this position was settled
    TODO(DEC-582): pending margin trading being added.
    """
    def __init__(
        self,
        *,
        asset_id: builtins.int = ...,
        quantums: builtins.bytes = ...,
        index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["asset_id", b"asset_id", "index", b"index", "quantums", b"quantums"]) -> None: ...

global___AssetPosition = AssetPosition
