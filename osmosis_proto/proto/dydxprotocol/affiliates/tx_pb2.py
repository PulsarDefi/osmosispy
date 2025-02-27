# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/affiliates/tx.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from dydxprotocol.affiliates import affiliates_pb2 as dydxprotocol_dot_affiliates_dot_affiliates__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n dydxprotocol/affiliates/tx.proto\x12\x17\x64ydxprotocol.affiliates\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a(dydxprotocol/affiliates/affiliates.proto\x1a\x17\x63osmos/msg/v1/msg.proto"\x84\x01\n\x14MsgRegisterAffiliate\x12)\n\x07referee\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12+\n\taffiliate\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x14\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x07referee"\x1e\n\x1cMsgRegisterAffiliateResponse"\x94\x01\n\x17MsgUpdateAffiliateTiers\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12<\n\x05tiers\x18\x02 \x01(\x0b\x32\'.dydxprotocol.affiliates.AffiliateTiersB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority"!\n\x1fMsgUpdateAffiliateTiersResponse"\xa0\x01\n\x1bMsgUpdateAffiliateWhitelist\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x44\n\twhitelist\x18\x02 \x01(\x0b\x32+.dydxprotocol.affiliates.AffiliateWhitelistB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority"%\n#MsgUpdateAffiliateWhitelistResponse2\x96\x03\n\x03Msg\x12y\n\x11RegisterAffiliate\x12-.dydxprotocol.affiliates.MsgRegisterAffiliate\x1a\x35.dydxprotocol.affiliates.MsgRegisterAffiliateResponse\x12\x82\x01\n\x14UpdateAffiliateTiers\x12\x30.dydxprotocol.affiliates.MsgUpdateAffiliateTiers\x1a\x38.dydxprotocol.affiliates.MsgUpdateAffiliateTiersResponse\x12\x8e\x01\n\x18UpdateAffiliateWhitelist\x12\x34.dydxprotocol.affiliates.MsgUpdateAffiliateWhitelist\x1a<.dydxprotocol.affiliates.MsgUpdateAffiliateWhitelistResponseB>Z<github.com/dydxprotocol/v4-chain/protocol/x/affiliates/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.affiliates.tx_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z<github.com/dydxprotocol/v4-chain/protocol/x/affiliates/types"
    _globals["_MSGREGISTERAFFILIATE"].fields_by_name["referee"]._loaded_options = None
    _globals["_MSGREGISTERAFFILIATE"].fields_by_name[
        "referee"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGREGISTERAFFILIATE"].fields_by_name["affiliate"]._loaded_options = None
    _globals["_MSGREGISTERAFFILIATE"].fields_by_name[
        "affiliate"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGREGISTERAFFILIATE"]._loaded_options = None
    _globals["_MSGREGISTERAFFILIATE"]._serialized_options = b"\210\240\037\000\350\240\037\000\202\347\260*\007referee"
    _globals["_MSGUPDATEAFFILIATETIERS"].fields_by_name["authority"]._loaded_options = None
    _globals["_MSGUPDATEAFFILIATETIERS"].fields_by_name[
        "authority"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEAFFILIATETIERS"].fields_by_name["tiers"]._loaded_options = None
    _globals["_MSGUPDATEAFFILIATETIERS"].fields_by_name["tiers"]._serialized_options = b"\310\336\037\000"
    _globals["_MSGUPDATEAFFILIATETIERS"]._loaded_options = None
    _globals["_MSGUPDATEAFFILIATETIERS"]._serialized_options = b"\202\347\260*\tauthority"
    _globals["_MSGUPDATEAFFILIATEWHITELIST"].fields_by_name["authority"]._loaded_options = None
    _globals["_MSGUPDATEAFFILIATEWHITELIST"].fields_by_name[
        "authority"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEAFFILIATEWHITELIST"].fields_by_name["whitelist"]._loaded_options = None
    _globals["_MSGUPDATEAFFILIATEWHITELIST"].fields_by_name["whitelist"]._serialized_options = b"\310\336\037\000"
    _globals["_MSGUPDATEAFFILIATEWHITELIST"]._loaded_options = None
    _globals["_MSGUPDATEAFFILIATEWHITELIST"]._serialized_options = b"\202\347\260*\tauthority"
    _globals["_MSGREGISTERAFFILIATE"]._serialized_start = 178
    _globals["_MSGREGISTERAFFILIATE"]._serialized_end = 310
    _globals["_MSGREGISTERAFFILIATERESPONSE"]._serialized_start = 312
    _globals["_MSGREGISTERAFFILIATERESPONSE"]._serialized_end = 342
    _globals["_MSGUPDATEAFFILIATETIERS"]._serialized_start = 345
    _globals["_MSGUPDATEAFFILIATETIERS"]._serialized_end = 493
    _globals["_MSGUPDATEAFFILIATETIERSRESPONSE"]._serialized_start = 495
    _globals["_MSGUPDATEAFFILIATETIERSRESPONSE"]._serialized_end = 528
    _globals["_MSGUPDATEAFFILIATEWHITELIST"]._serialized_start = 531
    _globals["_MSGUPDATEAFFILIATEWHITELIST"]._serialized_end = 691
    _globals["_MSGUPDATEAFFILIATEWHITELISTRESPONSE"]._serialized_start = 693
    _globals["_MSGUPDATEAFFILIATEWHITELISTRESPONSE"]._serialized_end = 730
    _globals["_MSG"]._serialized_start = 733
    _globals["_MSG"]._serialized_end = 1139
# @@protoc_insertion_point(module_scope)
