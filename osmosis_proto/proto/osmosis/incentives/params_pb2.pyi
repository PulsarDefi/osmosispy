"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Params(google.protobuf.message.Message):
    """Params holds parameters for the incentives module"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISTR_EPOCH_IDENTIFIER_FIELD_NUMBER: builtins.int
    distr_epoch_identifier: builtins.str
    """distr_epoch_identifier is what epoch type distribution will be triggered by
    (day, week, etc.)
    """
    def __init__(
        self,
        *,
        distr_epoch_identifier: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["distr_epoch_identifier", b"distr_epoch_identifier"]) -> None: ...

global___Params = Params
