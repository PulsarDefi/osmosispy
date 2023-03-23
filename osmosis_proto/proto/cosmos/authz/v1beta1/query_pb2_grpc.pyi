"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.43"""
import abc
import cosmos.authz.v1beta1.query_pb2
import grpc

class QueryStub:
    """Query defines the gRPC querier service."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Grants: grpc.UnaryUnaryMultiCallable[
        cosmos.authz.v1beta1.query_pb2.QueryGrantsRequest,
        cosmos.authz.v1beta1.query_pb2.QueryGrantsResponse,
    ]
    """Returns list of `Authorization`, granted to the grantee by the granter."""

class QueryServicer(metaclass=abc.ABCMeta):
    """Query defines the gRPC querier service."""

    @abc.abstractmethod
    def Grants(
        self,
        request: cosmos.authz.v1beta1.query_pb2.QueryGrantsRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.authz.v1beta1.query_pb2.QueryGrantsResponse:
        """Returns list of `Authorization`, granted to the grantee by the granter."""

def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
