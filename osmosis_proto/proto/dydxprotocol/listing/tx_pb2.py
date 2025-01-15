# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/listing/tx.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from dydxprotocol.subaccounts import subaccount_pb2 as dydxprotocol_dot_subaccounts_dot_subaccount__pb2
from dydxprotocol.listing import params_pb2 as dydxprotocol_dot_listing_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1d\x64ydxprotocol/listing/tx.proto\x12\x14\x64ydxprotocol.listing\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x14gogoproto/gogo.proto\x1a)dydxprotocol/subaccounts/subaccount.proto\x1a!dydxprotocol/listing/params.proto"q\n\x14MsgSetMarketsHardCap\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x1c\n\x14hard_cap_for_markets\x18\x02 \x01(\r:\x0e\x82\xe7\xb0*\tauthority"\x1e\n\x1cMsgSetMarketsHardCapResponse"\x82\x01\n\x1dMsgCreateMarketPermissionless\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12=\n\rsubaccount_id\x18\x02 \x01(\x0b\x32&.dydxprotocol.subaccounts.SubaccountId:\x12\x82\xe7\xb0*\rsubaccount_id"\'\n%MsgCreateMarketPermissionlessResponse"\xa5\x01\n\x1fMsgSetListingVaultDepositParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x45\n\x06params\x18\x02 \x01(\x0b\x32/.dydxprotocol.listing.ListingVaultDepositParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority")\n\'MsgSetListingVaultDepositParamsResponse"w\n"MsgUpgradeIsolatedPerpetualToCross\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x14\n\x0cperpetual_id\x18\x02 \x01(\r:\x0e\x82\xe7\xb0*\tauthority",\n*MsgUpgradeIsolatedPerpetualToCrossResponse2\xc2\x04\n\x03Msg\x12s\n\x11SetMarketsHardCap\x12*.dydxprotocol.listing.MsgSetMarketsHardCap\x1a\x32.dydxprotocol.listing.MsgSetMarketsHardCapResponse\x12\x8e\x01\n\x1a\x43reateMarketPermissionless\x12\x33.dydxprotocol.listing.MsgCreateMarketPermissionless\x1a;.dydxprotocol.listing.MsgCreateMarketPermissionlessResponse\x12\x94\x01\n\x1cSetListingVaultDepositParams\x12\x35.dydxprotocol.listing.MsgSetListingVaultDepositParams\x1a=.dydxprotocol.listing.MsgSetListingVaultDepositParamsResponse\x12\x9d\x01\n\x1fUpgradeIsolatedPerpetualToCross\x12\x38.dydxprotocol.listing.MsgUpgradeIsolatedPerpetualToCross\x1a@.dydxprotocol.listing.MsgUpgradeIsolatedPerpetualToCrossResponseB;Z9github.com/dydxprotocol/v4-chain/protocol/x/listing/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.listing.tx_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z9github.com/dydxprotocol/v4-chain/protocol/x/listing/types"
    _globals["_MSGSETMARKETSHARDCAP"].fields_by_name["authority"]._loaded_options = None
    _globals["_MSGSETMARKETSHARDCAP"].fields_by_name[
        "authority"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGSETMARKETSHARDCAP"]._loaded_options = None
    _globals["_MSGSETMARKETSHARDCAP"]._serialized_options = b"\202\347\260*\tauthority"
    _globals["_MSGCREATEMARKETPERMISSIONLESS"]._loaded_options = None
    _globals["_MSGCREATEMARKETPERMISSIONLESS"]._serialized_options = b"\202\347\260*\rsubaccount_id"
    _globals["_MSGSETLISTINGVAULTDEPOSITPARAMS"].fields_by_name["authority"]._loaded_options = None
    _globals["_MSGSETLISTINGVAULTDEPOSITPARAMS"].fields_by_name[
        "authority"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGSETLISTINGVAULTDEPOSITPARAMS"].fields_by_name["params"]._loaded_options = None
    _globals["_MSGSETLISTINGVAULTDEPOSITPARAMS"].fields_by_name["params"]._serialized_options = b"\310\336\037\000"
    _globals["_MSGSETLISTINGVAULTDEPOSITPARAMS"]._loaded_options = None
    _globals["_MSGSETLISTINGVAULTDEPOSITPARAMS"]._serialized_options = b"\202\347\260*\tauthority"
    _globals["_MSGUPGRADEISOLATEDPERPETUALTOCROSS"].fields_by_name["authority"]._loaded_options = None
    _globals["_MSGUPGRADEISOLATEDPERPETUALTOCROSS"].fields_by_name[
        "authority"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPGRADEISOLATEDPERPETUALTOCROSS"]._loaded_options = None
    _globals["_MSGUPGRADEISOLATEDPERPETUALTOCROSS"]._serialized_options = b"\202\347\260*\tauthority"
    _globals["_MSGSETMARKETSHARDCAP"]._serialized_start = 207
    _globals["_MSGSETMARKETSHARDCAP"]._serialized_end = 320
    _globals["_MSGSETMARKETSHARDCAPRESPONSE"]._serialized_start = 322
    _globals["_MSGSETMARKETSHARDCAPRESPONSE"]._serialized_end = 352
    _globals["_MSGCREATEMARKETPERMISSIONLESS"]._serialized_start = 355
    _globals["_MSGCREATEMARKETPERMISSIONLESS"]._serialized_end = 485
    _globals["_MSGCREATEMARKETPERMISSIONLESSRESPONSE"]._serialized_start = 487
    _globals["_MSGCREATEMARKETPERMISSIONLESSRESPONSE"]._serialized_end = 526
    _globals["_MSGSETLISTINGVAULTDEPOSITPARAMS"]._serialized_start = 529
    _globals["_MSGSETLISTINGVAULTDEPOSITPARAMS"]._serialized_end = 694
    _globals["_MSGSETLISTINGVAULTDEPOSITPARAMSRESPONSE"]._serialized_start = 696
    _globals["_MSGSETLISTINGVAULTDEPOSITPARAMSRESPONSE"]._serialized_end = 737
    _globals["_MSGUPGRADEISOLATEDPERPETUALTOCROSS"]._serialized_start = 739
    _globals["_MSGUPGRADEISOLATEDPERPETUALTOCROSS"]._serialized_end = 858
    _globals["_MSGUPGRADEISOLATEDPERPETUALTOCROSSRESPONSE"]._serialized_start = 860
    _globals["_MSGUPGRADEISOLATEDPERPETUALTOCROSSRESPONSE"]._serialized_end = 904
    _globals["_MSG"]._serialized_start = 907
    _globals["_MSG"]._serialized_end = 1485
# @@protoc_insertion_point(module_scope)
