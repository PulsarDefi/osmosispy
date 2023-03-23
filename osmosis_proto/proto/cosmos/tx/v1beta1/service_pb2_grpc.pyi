"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import cosmos.tx.v1beta1.service_pb2
import grpc

class ServiceStub:
    """Service defines a gRPC service for interacting with transactions."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Simulate: grpc.UnaryUnaryMultiCallable[
        cosmos.tx.v1beta1.service_pb2.SimulateRequest,
        cosmos.tx.v1beta1.service_pb2.SimulateResponse,
    ]
    """Simulate simulates executing a transaction for estimating gas usage."""
    GetTx: grpc.UnaryUnaryMultiCallable[
        cosmos.tx.v1beta1.service_pb2.GetTxRequest,
        cosmos.tx.v1beta1.service_pb2.GetTxResponse,
    ]
    """GetTx fetches a tx by hash."""
    BroadcastTx: grpc.UnaryUnaryMultiCallable[
        cosmos.tx.v1beta1.service_pb2.BroadcastTxRequest,
        cosmos.tx.v1beta1.service_pb2.BroadcastTxResponse,
    ]
    """BroadcastTx broadcast transaction."""
    GetTxsEvent: grpc.UnaryUnaryMultiCallable[
        cosmos.tx.v1beta1.service_pb2.GetTxsEventRequest,
        cosmos.tx.v1beta1.service_pb2.GetTxsEventResponse,
    ]
    """GetTxsEvent fetches txs by event."""

class ServiceServicer(metaclass=abc.ABCMeta):
    """Service defines a gRPC service for interacting with transactions."""

    @abc.abstractmethod
    def Simulate(
        self,
        request: cosmos.tx.v1beta1.service_pb2.SimulateRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.tx.v1beta1.service_pb2.SimulateResponse:
        """Simulate simulates executing a transaction for estimating gas usage."""
    @abc.abstractmethod
    def GetTx(
        self,
        request: cosmos.tx.v1beta1.service_pb2.GetTxRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.tx.v1beta1.service_pb2.GetTxResponse:
        """GetTx fetches a tx by hash."""
    @abc.abstractmethod
    def BroadcastTx(
        self,
        request: cosmos.tx.v1beta1.service_pb2.BroadcastTxRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.tx.v1beta1.service_pb2.BroadcastTxResponse:
        """BroadcastTx broadcast transaction."""
    @abc.abstractmethod
    def GetTxsEvent(
        self,
        request: cosmos.tx.v1beta1.service_pb2.GetTxsEventRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.tx.v1beta1.service_pb2.GetTxsEventResponse:
        """GetTxsEvent fetches txs by event."""

def add_ServiceServicer_to_server(servicer: ServiceServicer, server: grpc.Server) -> None: ...
