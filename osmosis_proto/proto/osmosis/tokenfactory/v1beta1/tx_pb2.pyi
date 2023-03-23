"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.bank.v1beta1.bank_pb2
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MsgCreateDenom(google.protobuf.message.Message):
    """MsgCreateDenom defines the message structure for the CreateDenom gRPC service
    method. It allows an account to create a new denom. It requires a sender
    address and a sub denomination. The (sender_address, sub_denomination) tuple
    must be unique and cannot be re-used.

    The resulting denom created is defined as
    <factory/{creatorAddress}/{subdenom}>. The resulting denom's admin is
    originally set to be the creator, but this can be changed later. The token
    denom does not indicate the current admin.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    SUBDENOM_FIELD_NUMBER: builtins.int
    sender: builtins.str
    subdenom: builtins.str
    """subdenom can be up to 44 "alphanumeric" characters long."""
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        subdenom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sender", b"sender", "subdenom", b"subdenom"]) -> None: ...

global___MsgCreateDenom = MsgCreateDenom

@typing_extensions.final
class MsgCreateDenomResponse(google.protobuf.message.Message):
    """MsgCreateDenomResponse is the return value of MsgCreateDenom
    It returns the full string of the newly created denom
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEW_TOKEN_DENOM_FIELD_NUMBER: builtins.int
    new_token_denom: builtins.str
    def __init__(
        self,
        *,
        new_token_denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["new_token_denom", b"new_token_denom"]) -> None: ...

global___MsgCreateDenomResponse = MsgCreateDenomResponse

@typing_extensions.final
class MsgMint(google.protobuf.message.Message):
    """MsgMint is the sdk.Msg type for allowing an admin account to mint
    more of a token.  For now, we only support minting to the sender account
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    sender: builtins.str
    @property
    def amount(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        amount: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["amount", b"amount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount", "sender", b"sender"]) -> None: ...

global___MsgMint = MsgMint

@typing_extensions.final
class MsgMintResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgMintResponse = MsgMintResponse

@typing_extensions.final
class MsgBurn(google.protobuf.message.Message):
    """MsgBurn is the sdk.Msg type for allowing an admin account to burn
    a token.  For now, we only support burning from the sender account.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    sender: builtins.str
    @property
    def amount(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        amount: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["amount", b"amount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount", "sender", b"sender"]) -> None: ...

global___MsgBurn = MsgBurn

@typing_extensions.final
class MsgBurnResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgBurnResponse = MsgBurnResponse

@typing_extensions.final
class MsgChangeAdmin(google.protobuf.message.Message):
    """MsgChangeAdmin is the sdk.Msg type for allowing an admin account to reassign
    adminship of a denom to a new account
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    DENOM_FIELD_NUMBER: builtins.int
    NEW_ADMIN_FIELD_NUMBER: builtins.int
    sender: builtins.str
    denom: builtins.str
    new_admin: builtins.str
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        denom: builtins.str = ...,
        new_admin: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom", "new_admin", b"new_admin", "sender", b"sender"]) -> None: ...

global___MsgChangeAdmin = MsgChangeAdmin

@typing_extensions.final
class MsgChangeAdminResponse(google.protobuf.message.Message):
    """MsgChangeAdminResponse defines the response structure for an executed
    MsgChangeAdmin message.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgChangeAdminResponse = MsgChangeAdminResponse

@typing_extensions.final
class MsgSetDenomMetadata(google.protobuf.message.Message):
    """message MsgForceTransferResponse {}

    MsgSetDenomMetadata is the sdk.Msg type for allowing an admin account to set
    the denom's bank metadata
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    sender: builtins.str
    @property
    def metadata(self) -> cosmos.bank.v1beta1.bank_pb2.Metadata: ...
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        metadata: cosmos.bank.v1beta1.bank_pb2.Metadata | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "sender", b"sender"]) -> None: ...

global___MsgSetDenomMetadata = MsgSetDenomMetadata

@typing_extensions.final
class MsgSetDenomMetadataResponse(google.protobuf.message.Message):
    """MsgSetDenomMetadataResponse defines the response structure for an executed
    MsgSetDenomMetadata message.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgSetDenomMetadataResponse = MsgSetDenomMetadataResponse
