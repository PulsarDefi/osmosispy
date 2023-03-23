"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.abci.v1beta1.abci_pb2
import cosmos.base.query.v1beta1.pagination_pb2
import cosmos.tx.v1beta1.tx_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _OrderBy:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _OrderByEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OrderBy.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ORDER_BY_UNSPECIFIED: _OrderBy.ValueType  # 0
    """ORDER_BY_UNSPECIFIED specifies an unknown sorting order. OrderBy defaults to ASC in this case."""
    ORDER_BY_ASC: _OrderBy.ValueType  # 1
    """ORDER_BY_ASC defines ascending order"""
    ORDER_BY_DESC: _OrderBy.ValueType  # 2
    """ORDER_BY_DESC defines descending order"""

class OrderBy(_OrderBy, metaclass=_OrderByEnumTypeWrapper):
    """OrderBy defines the sorting order"""

ORDER_BY_UNSPECIFIED: OrderBy.ValueType  # 0
"""ORDER_BY_UNSPECIFIED specifies an unknown sorting order. OrderBy defaults to ASC in this case."""
ORDER_BY_ASC: OrderBy.ValueType  # 1
"""ORDER_BY_ASC defines ascending order"""
ORDER_BY_DESC: OrderBy.ValueType  # 2
"""ORDER_BY_DESC defines descending order"""
global___OrderBy = OrderBy

class _BroadcastMode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _BroadcastModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BroadcastMode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    BROADCAST_MODE_UNSPECIFIED: _BroadcastMode.ValueType  # 0
    """zero-value for mode ordering"""
    BROADCAST_MODE_BLOCK: _BroadcastMode.ValueType  # 1
    """BROADCAST_MODE_BLOCK defines a tx broadcasting mode where the client waits for
    the tx to be committed in a block.
    """
    BROADCAST_MODE_SYNC: _BroadcastMode.ValueType  # 2
    """BROADCAST_MODE_SYNC defines a tx broadcasting mode where the client waits for
    a CheckTx execution response only.
    """
    BROADCAST_MODE_ASYNC: _BroadcastMode.ValueType  # 3
    """BROADCAST_MODE_ASYNC defines a tx broadcasting mode where the client returns
    immediately.
    """

class BroadcastMode(_BroadcastMode, metaclass=_BroadcastModeEnumTypeWrapper):
    """BroadcastMode specifies the broadcast mode for the TxService.Broadcast RPC method."""

BROADCAST_MODE_UNSPECIFIED: BroadcastMode.ValueType  # 0
"""zero-value for mode ordering"""
BROADCAST_MODE_BLOCK: BroadcastMode.ValueType  # 1
"""BROADCAST_MODE_BLOCK defines a tx broadcasting mode where the client waits for
the tx to be committed in a block.
"""
BROADCAST_MODE_SYNC: BroadcastMode.ValueType  # 2
"""BROADCAST_MODE_SYNC defines a tx broadcasting mode where the client waits for
a CheckTx execution response only.
"""
BROADCAST_MODE_ASYNC: BroadcastMode.ValueType  # 3
"""BROADCAST_MODE_ASYNC defines a tx broadcasting mode where the client returns
immediately.
"""
global___BroadcastMode = BroadcastMode

@typing_extensions.final
class GetTxsEventRequest(google.protobuf.message.Message):
    """GetTxsEventRequest is the request type for the Service.TxsByEvents
    RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EVENTS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    @property
    def events(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """events is the list of transaction event type."""
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an pagination for the request."""
    order_by: global___OrderBy.ValueType
    def __init__(
        self,
        *,
        events: collections.abc.Iterable[builtins.str] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
        order_by: global___OrderBy.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["events", b"events", "order_by", b"order_by", "pagination", b"pagination"]) -> None: ...

global___GetTxsEventRequest = GetTxsEventRequest

@typing_extensions.final
class GetTxsEventResponse(google.protobuf.message.Message):
    """GetTxsEventResponse is the response type for the Service.TxsByEvents
    RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TXS_FIELD_NUMBER: builtins.int
    TX_RESPONSES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def txs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.tx.v1beta1.tx_pb2.Tx]:
        """txs is the list of queried transactions."""
    @property
    def tx_responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.abci.v1beta1.abci_pb2.TxResponse]:
        """tx_responses is the list of queried TxResponses."""
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines an pagination for the response."""
    def __init__(
        self,
        *,
        txs: collections.abc.Iterable[cosmos.tx.v1beta1.tx_pb2.Tx] | None = ...,
        tx_responses: collections.abc.Iterable[cosmos.base.abci.v1beta1.abci_pb2.TxResponse] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination", "tx_responses", b"tx_responses", "txs", b"txs"]) -> None: ...

global___GetTxsEventResponse = GetTxsEventResponse

@typing_extensions.final
class BroadcastTxRequest(google.protobuf.message.Message):
    """BroadcastTxRequest is the request type for the Service.BroadcastTxRequest
    RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_BYTES_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    tx_bytes: builtins.bytes
    """tx_bytes is the raw transaction."""
    mode: global___BroadcastMode.ValueType
    def __init__(
        self,
        *,
        tx_bytes: builtins.bytes = ...,
        mode: global___BroadcastMode.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["mode", b"mode", "tx_bytes", b"tx_bytes"]) -> None: ...

global___BroadcastTxRequest = BroadcastTxRequest

@typing_extensions.final
class BroadcastTxResponse(google.protobuf.message.Message):
    """BroadcastTxResponse is the response type for the
    Service.BroadcastTx method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def tx_response(self) -> cosmos.base.abci.v1beta1.abci_pb2.TxResponse:
        """tx_response is the queried TxResponses."""
    def __init__(
        self,
        *,
        tx_response: cosmos.base.abci.v1beta1.abci_pb2.TxResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tx_response", b"tx_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tx_response", b"tx_response"]) -> None: ...

global___BroadcastTxResponse = BroadcastTxResponse

@typing_extensions.final
class SimulateRequest(google.protobuf.message.Message):
    """SimulateRequest is the request type for the Service.Simulate
    RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_FIELD_NUMBER: builtins.int
    TX_BYTES_FIELD_NUMBER: builtins.int
    @property
    def tx(self) -> cosmos.tx.v1beta1.tx_pb2.Tx:
        """tx is the transaction to simulate.
        Deprecated. Send raw tx bytes instead.
        """
    tx_bytes: builtins.bytes
    """tx_bytes is the raw transaction.

    Since: cosmos-sdk 0.43
    """
    def __init__(
        self,
        *,
        tx: cosmos.tx.v1beta1.tx_pb2.Tx | None = ...,
        tx_bytes: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tx", b"tx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tx", b"tx", "tx_bytes", b"tx_bytes"]) -> None: ...

global___SimulateRequest = SimulateRequest

@typing_extensions.final
class SimulateResponse(google.protobuf.message.Message):
    """SimulateResponse is the response type for the
    Service.SimulateRPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GAS_INFO_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def gas_info(self) -> cosmos.base.abci.v1beta1.abci_pb2.GasInfo:
        """gas_info is the information about gas used in the simulation."""
    @property
    def result(self) -> cosmos.base.abci.v1beta1.abci_pb2.Result:
        """result is the result of the simulation."""
    def __init__(
        self,
        *,
        gas_info: cosmos.base.abci.v1beta1.abci_pb2.GasInfo | None = ...,
        result: cosmos.base.abci.v1beta1.abci_pb2.Result | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gas_info", b"gas_info", "result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gas_info", b"gas_info", "result", b"result"]) -> None: ...

global___SimulateResponse = SimulateResponse

@typing_extensions.final
class GetTxRequest(google.protobuf.message.Message):
    """GetTxRequest is the request type for the Service.GetTx
    RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HASH_FIELD_NUMBER: builtins.int
    hash: builtins.str
    """hash is the tx hash to query, encoded as a hex string."""
    def __init__(
        self,
        *,
        hash: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hash", b"hash"]) -> None: ...

global___GetTxRequest = GetTxRequest

@typing_extensions.final
class GetTxResponse(google.protobuf.message.Message):
    """GetTxResponse is the response type for the Service.GetTx method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_FIELD_NUMBER: builtins.int
    TX_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def tx(self) -> cosmos.tx.v1beta1.tx_pb2.Tx:
        """tx is the queried transaction."""
    @property
    def tx_response(self) -> cosmos.base.abci.v1beta1.abci_pb2.TxResponse:
        """tx_response is the queried TxResponses."""
    def __init__(
        self,
        *,
        tx: cosmos.tx.v1beta1.tx_pb2.Tx | None = ...,
        tx_response: cosmos.base.abci.v1beta1.abci_pb2.TxResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tx", b"tx", "tx_response", b"tx_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tx", b"tx", "tx_response", b"tx_response"]) -> None: ...

global___GetTxResponse = GetTxResponse
