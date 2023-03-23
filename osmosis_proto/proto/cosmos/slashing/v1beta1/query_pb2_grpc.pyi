"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import cosmos.slashing.v1beta1.query_pb2
import grpc

class QueryStub:
    """Query provides defines the gRPC querier service"""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Params: grpc.UnaryUnaryMultiCallable[
        cosmos.slashing.v1beta1.query_pb2.QueryParamsRequest,
        cosmos.slashing.v1beta1.query_pb2.QueryParamsResponse,
    ]
    """Params queries the parameters of slashing module"""
    SigningInfo: grpc.UnaryUnaryMultiCallable[
        cosmos.slashing.v1beta1.query_pb2.QuerySigningInfoRequest,
        cosmos.slashing.v1beta1.query_pb2.QuerySigningInfoResponse,
    ]
    """SigningInfo queries the signing info of given cons address"""
    SigningInfos: grpc.UnaryUnaryMultiCallable[
        cosmos.slashing.v1beta1.query_pb2.QuerySigningInfosRequest,
        cosmos.slashing.v1beta1.query_pb2.QuerySigningInfosResponse,
    ]
    """SigningInfos queries signing info of all validators"""

class QueryServicer(metaclass=abc.ABCMeta):
    """Query provides defines the gRPC querier service"""

    @abc.abstractmethod
    def Params(
        self,
        request: cosmos.slashing.v1beta1.query_pb2.QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.slashing.v1beta1.query_pb2.QueryParamsResponse:
        """Params queries the parameters of slashing module"""
    @abc.abstractmethod
    def SigningInfo(
        self,
        request: cosmos.slashing.v1beta1.query_pb2.QuerySigningInfoRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.slashing.v1beta1.query_pb2.QuerySigningInfoResponse:
        """SigningInfo queries the signing info of given cons address"""
    @abc.abstractmethod
    def SigningInfos(
        self,
        request: cosmos.slashing.v1beta1.query_pb2.QuerySigningInfosRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.slashing.v1beta1.query_pb2.QuerySigningInfosResponse:
        """SigningInfos queries signing info of all validators"""

def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
