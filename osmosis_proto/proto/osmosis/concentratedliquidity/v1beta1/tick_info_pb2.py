# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: osmosis/concentratedliquidity/v1beta1/tick_info.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n5osmosis/concentratedliquidity/v1beta1/tick_info.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xbd\x03\n\x08TickInfo\x12V\n\x0fliquidity_gross\x18\x01 \x01(\tB=\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xf2\xde\x1f\x16yaml:\"liquidity_gross\"\x12R\n\rliquidity_net\x18\x02 \x01(\tB;\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xf2\xde\x1f\x14yaml:\"liquidity_net\"\x12\x94\x01\n9spread_reward_growth_opposite_direction_of_last_traversal\x18\x03 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\x12n\n\x0fuptime_trackers\x18\x04 \x01(\x0b\x32\x35.osmosis.concentratedliquidity.v1beta1.UptimeTrackersB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:\"uptime_trackers\"\"i\n\x0eUptimeTrackers\x12W\n\x04list\x18\x01 \x03(\x0b\x32\x34.osmosis.concentratedliquidity.v1beta1.UptimeTrackerB\x13\xc8\xde\x1f\x00\xf2\xde\x1f\x0byaml:\"list\"\"\x81\x01\n\rUptimeTracker\x12p\n\x15uptime_growth_outside\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoinsBDZBgithub.com/osmosis-labs/osmosis/v25/x/concentrated-liquidity/modelb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentratedliquidity.v1beta1.tick_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v25/x/concentrated-liquidity/model'
    _globals['_TICKINFO'].fields_by_name['liquidity_gross']._loaded_options = None
    _globals['_TICKINFO'].fields_by_name[
        'liquidity_gross'
    ]._serialized_options = (
        b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\362\336\037\026yaml:\"liquidity_gross\"'
    )
    _globals['_TICKINFO'].fields_by_name['liquidity_net']._loaded_options = None
    _globals['_TICKINFO'].fields_by_name[
        'liquidity_net'
    ]._serialized_options = (
        b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\362\336\037\024yaml:\"liquidity_net\"'
    )
    _globals['_TICKINFO'].fields_by_name[
        'spread_reward_growth_opposite_direction_of_last_traversal'
    ]._loaded_options = None
    _globals['_TICKINFO'].fields_by_name[
        'spread_reward_growth_opposite_direction_of_last_traversal'
    ]._serialized_options = b'\310\336\037\000\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _globals['_TICKINFO'].fields_by_name['uptime_trackers']._loaded_options = None
    _globals['_TICKINFO'].fields_by_name[
        'uptime_trackers'
    ]._serialized_options = b'\310\336\037\000\362\336\037\026yaml:\"uptime_trackers\"'
    _globals['_UPTIMETRACKERS'].fields_by_name['list']._loaded_options = None
    _globals['_UPTIMETRACKERS'].fields_by_name[
        'list'
    ]._serialized_options = b'\310\336\037\000\362\336\037\013yaml:\"list\"'
    _globals['_UPTIMETRACKER'].fields_by_name['uptime_growth_outside']._loaded_options = None
    _globals['_UPTIMETRACKER'].fields_by_name[
        'uptime_growth_outside'
    ]._serialized_options = b'\310\336\037\000\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _globals['_TICKINFO']._serialized_start = 151
    _globals['_TICKINFO']._serialized_end = 596
    _globals['_UPTIMETRACKERS']._serialized_start = 598
    _globals['_UPTIMETRACKERS']._serialized_end = 703
    _globals['_UPTIMETRACKER']._serialized_start = 706
    _globals['_UPTIMETRACKER']._serialized_end = 835
# @@protoc_insertion_point(module_scope)
