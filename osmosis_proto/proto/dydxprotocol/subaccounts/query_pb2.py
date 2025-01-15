# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/subaccounts/query.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'dydxprotocol/subaccounts/query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from dydxprotocol.subaccounts import subaccount_pb2 as dydxprotocol_dot_subaccounts_dot_subaccount__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$dydxprotocol/subaccounts/query.proto\x12\x18\x64ydxprotocol.subaccounts\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a)dydxprotocol/subaccounts/subaccount.proto\"T\n\x19QueryGetSubaccountRequest\x12\'\n\x05owner\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0e\n\x06number\x18\x02 \x01(\r\"Y\n\x17QuerySubaccountResponse\x12>\n\nsubaccount\x18\x01 \x01(\x0b\x32$.dydxprotocol.subaccounts.SubaccountB\x04\xc8\xde\x1f\x00\"W\n\x19QueryAllSubaccountRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x99\x01\n\x1aQuerySubaccountAllResponse\x12>\n\nsubaccount\x18\x01 \x03(\x0b\x32$.dydxprotocol.subaccounts.SubaccountB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"H\n0QueryGetWithdrawalAndTransfersBlockedInfoRequest\x12\x14\n\x0cperpetual_id\x18\x01 \x01(\r\"\xbc\x01\n1QueryGetWithdrawalAndTransfersBlockedInfoResponse\x12-\n%negative_tnc_subaccount_seen_at_block\x18\x01 \x01(\r\x12\"\n\x1a\x63hain_outage_seen_at_block\x18\x02 \x01(\r\x12\x34\n,withdrawals_and_transfers_unblocked_at_block\x18\x03 \x01(\r\"9\n!QueryCollateralPoolAddressRequest\x12\x14\n\x0cperpetual_id\x18\x01 \x01(\r\"_\n\"QueryCollateralPoolAddressResponse\x12\x39\n\x17\x63ollateral_pool_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString2\xe2\x06\n\x05Query\x12\xb3\x01\n\nSubaccount\x12\x33.dydxprotocol.subaccounts.QueryGetSubaccountRequest\x1a\x31.dydxprotocol.subaccounts.QuerySubaccountResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/dydxprotocol/subaccounts/subaccount/{owner}/{number}\x12\xa8\x01\n\rSubaccountAll\x12\x33.dydxprotocol.subaccounts.QueryAllSubaccountRequest\x1a\x34.dydxprotocol.subaccounts.QuerySubaccountAllResponse\",\x82\xd3\xe4\x93\x02&\x12$/dydxprotocol/subaccounts/subaccount\x12\x98\x02\n$GetWithdrawalAndTransfersBlockedInfo\x12J.dydxprotocol.subaccounts.QueryGetWithdrawalAndTransfersBlockedInfoRequest\x1aK.dydxprotocol.subaccounts.QueryGetWithdrawalAndTransfersBlockedInfoResponse\"W\x82\xd3\xe4\x93\x02Q\x12O/dydxprotocol/subaccounts/withdrawals_and_transfers_blocked_info/{perpetual_id}\x12\xdc\x01\n\x15\x43ollateralPoolAddress\x12;.dydxprotocol.subaccounts.QueryCollateralPoolAddressRequest\x1a<.dydxprotocol.subaccounts.QueryCollateralPoolAddressResponse\"H\x82\xd3\xe4\x93\x02\x42\x12@/dydxprotocol/subaccounts/collateral_pool_address/{perpetual_id}B?Z=github.com/dydxprotocol/v4-chain/protocol/x/subaccounts/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.subaccounts.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/dydxprotocol/v4-chain/protocol/x/subaccounts/types'
  _globals['_QUERYGETSUBACCOUNTREQUEST'].fields_by_name['owner']._loaded_options = None
  _globals['_QUERYGETSUBACCOUNTREQUEST'].fields_by_name['owner']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYSUBACCOUNTRESPONSE'].fields_by_name['subaccount']._loaded_options = None
  _globals['_QUERYSUBACCOUNTRESPONSE'].fields_by_name['subaccount']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYSUBACCOUNTALLRESPONSE'].fields_by_name['subaccount']._loaded_options = None
  _globals['_QUERYSUBACCOUNTALLRESPONSE'].fields_by_name['subaccount']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCOLLATERALPOOLADDRESSRESPONSE'].fields_by_name['collateral_pool_address']._loaded_options = None
  _globals['_QUERYCOLLATERALPOOLADDRESSRESPONSE'].fields_by_name['collateral_pool_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERY'].methods_by_name['Subaccount']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Subaccount']._serialized_options = b'\202\323\344\223\0027\0225/dydxprotocol/subaccounts/subaccount/{owner}/{number}'
  _globals['_QUERY'].methods_by_name['SubaccountAll']._loaded_options = None
  _globals['_QUERY'].methods_by_name['SubaccountAll']._serialized_options = b'\202\323\344\223\002&\022$/dydxprotocol/subaccounts/subaccount'
  _globals['_QUERY'].methods_by_name['GetWithdrawalAndTransfersBlockedInfo']._loaded_options = None
  _globals['_QUERY'].methods_by_name['GetWithdrawalAndTransfersBlockedInfo']._serialized_options = b'\202\323\344\223\002Q\022O/dydxprotocol/subaccounts/withdrawals_and_transfers_blocked_info/{perpetual_id}'
  _globals['_QUERY'].methods_by_name['CollateralPoolAddress']._loaded_options = None
  _globals['_QUERY'].methods_by_name['CollateralPoolAddress']._serialized_options = b'\202\323\344\223\002B\022@/dydxprotocol/subaccounts/collateral_pool_address/{perpetual_id}'
  _globals['_QUERYGETSUBACCOUNTREQUEST']._serialized_start=232
  _globals['_QUERYGETSUBACCOUNTREQUEST']._serialized_end=316
  _globals['_QUERYSUBACCOUNTRESPONSE']._serialized_start=318
  _globals['_QUERYSUBACCOUNTRESPONSE']._serialized_end=407
  _globals['_QUERYALLSUBACCOUNTREQUEST']._serialized_start=409
  _globals['_QUERYALLSUBACCOUNTREQUEST']._serialized_end=496
  _globals['_QUERYSUBACCOUNTALLRESPONSE']._serialized_start=499
  _globals['_QUERYSUBACCOUNTALLRESPONSE']._serialized_end=652
  _globals['_QUERYGETWITHDRAWALANDTRANSFERSBLOCKEDINFOREQUEST']._serialized_start=654
  _globals['_QUERYGETWITHDRAWALANDTRANSFERSBLOCKEDINFOREQUEST']._serialized_end=726
  _globals['_QUERYGETWITHDRAWALANDTRANSFERSBLOCKEDINFORESPONSE']._serialized_start=729
  _globals['_QUERYGETWITHDRAWALANDTRANSFERSBLOCKEDINFORESPONSE']._serialized_end=917
  _globals['_QUERYCOLLATERALPOOLADDRESSREQUEST']._serialized_start=919
  _globals['_QUERYCOLLATERALPOOLADDRESSREQUEST']._serialized_end=976
  _globals['_QUERYCOLLATERALPOOLADDRESSRESPONSE']._serialized_start=978
  _globals['_QUERYCOLLATERALPOOLADDRESSRESPONSE']._serialized_end=1073
  _globals['_QUERY']._serialized_start=1076
  _globals['_QUERY']._serialized_end=1942
# @@protoc_insertion_point(module_scope)
