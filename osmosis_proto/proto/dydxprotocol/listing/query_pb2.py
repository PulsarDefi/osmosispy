# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/listing/query.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from dydxprotocol.listing import params_pb2 as dydxprotocol_dot_listing_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n dydxprotocol/listing/query.proto\x12\x14\x64ydxprotocol.listing\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a!dydxprotocol/listing/params.proto"\x15\n\x13QueryMarketsHardCap"/\n\x1bQueryMarketsHardCapResponse\x12\x10\n\x08hard_cap\x18\x01 \x01(\r" \n\x1eQueryListingVaultDepositParams"o\n&QueryListingVaultDepositParamsResponse\x12\x45\n\x06params\x18\x01 \x01(\x0b\x32/.dydxprotocol.listing.ListingVaultDepositParamsB\x04\xc8\xde\x1f\x00\x32\xee\x02\n\x05Query\x12\x9e\x01\n\x0eMarketsHardCap\x12).dydxprotocol.listing.QueryMarketsHardCap\x1a\x31.dydxprotocol.listing.QueryMarketsHardCapResponse".\x82\xd3\xe4\x93\x02(\x12&/dydxprotocol/listing/markets_hard_cap\x12\xc3\x01\n\x19ListingVaultDepositParams\x12\x34.dydxprotocol.listing.QueryListingVaultDepositParams\x1a<.dydxprotocol.listing.QueryListingVaultDepositParamsResponse"2\x82\xd3\xe4\x93\x02,\x12*/dydxprotocol/listing/vault_deposit_paramsB;Z9github.com/dydxprotocol/v4-chain/protocol/x/listing/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.listing.query_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z9github.com/dydxprotocol/v4-chain/protocol/x/listing/types"
    _globals["_QUERYLISTINGVAULTDEPOSITPARAMSRESPONSE"].fields_by_name["params"]._loaded_options = None
    _globals["_QUERYLISTINGVAULTDEPOSITPARAMSRESPONSE"].fields_by_name[
        "params"
    ]._serialized_options = b"\310\336\037\000"
    _globals["_QUERY"].methods_by_name["MarketsHardCap"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "MarketsHardCap"
    ]._serialized_options = b"\202\323\344\223\002(\022&/dydxprotocol/listing/markets_hard_cap"
    _globals["_QUERY"].methods_by_name["ListingVaultDepositParams"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "ListingVaultDepositParams"
    ]._serialized_options = b"\202\323\344\223\002,\022*/dydxprotocol/listing/vault_deposit_params"
    _globals["_QUERYMARKETSHARDCAP"]._serialized_start = 145
    _globals["_QUERYMARKETSHARDCAP"]._serialized_end = 166
    _globals["_QUERYMARKETSHARDCAPRESPONSE"]._serialized_start = 168
    _globals["_QUERYMARKETSHARDCAPRESPONSE"]._serialized_end = 215
    _globals["_QUERYLISTINGVAULTDEPOSITPARAMS"]._serialized_start = 217
    _globals["_QUERYLISTINGVAULTDEPOSITPARAMS"]._serialized_end = 249
    _globals["_QUERYLISTINGVAULTDEPOSITPARAMSRESPONSE"]._serialized_start = 251
    _globals["_QUERYLISTINGVAULTDEPOSITPARAMSRESPONSE"]._serialized_end = 362
    _globals["_QUERY"]._serialized_start = 365
    _globals["_QUERY"]._serialized_end = 731
# @@protoc_insertion_point(module_scope)
