"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import stride.stakeibc.epoch_tracker_pb2
import stride.stakeibc.host_zone_pb2
import stride.stakeibc.params_pb2
import stride.stakeibc.trade_route_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the stakeibc module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    PORT_ID_FIELD_NUMBER: builtins.int
    HOST_ZONE_LIST_FIELD_NUMBER: builtins.int
    EPOCH_TRACKER_LIST_FIELD_NUMBER: builtins.int
    TRADE_ROUTES_FIELD_NUMBER: builtins.int
    port_id: builtins.str
    @property
    def params(self) -> stride.stakeibc.params_pb2.Params: ...
    @property
    def host_zone_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.stakeibc.host_zone_pb2.HostZone]: ...
    @property
    def epoch_tracker_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.stakeibc.epoch_tracker_pb2.EpochTracker]: ...
    @property
    def trade_routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[stride.stakeibc.trade_route_pb2.TradeRoute]: ...
    def __init__(
        self,
        *,
        params: stride.stakeibc.params_pb2.Params | None = ...,
        port_id: builtins.str = ...,
        host_zone_list: collections.abc.Iterable[stride.stakeibc.host_zone_pb2.HostZone] | None = ...,
        epoch_tracker_list: collections.abc.Iterable[stride.stakeibc.epoch_tracker_pb2.EpochTracker] | None = ...,
        trade_routes: collections.abc.Iterable[stride.stakeibc.trade_route_pb2.TradeRoute] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["epoch_tracker_list", b"epoch_tracker_list", "host_zone_list", b"host_zone_list", "params", b"params", "port_id", b"port_id", "trade_routes", b"trade_routes"]) -> None: ...

global___GenesisState = GenesisState
