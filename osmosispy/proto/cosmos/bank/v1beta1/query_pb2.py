# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google_apis.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/bank/v1beta1/query.proto\x12\x13\x63osmos.bank.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\"?\n\x13QueryBalanceRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"B\n\x14QueryBalanceResponse\x12*\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.Coin\"p\n\x17QueryAllBalancesRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb6\x01\n\x18QueryAllBalancesResponse\x12]\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"_\n\x17QueryTotalSupplyRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb4\x01\n\x18QueryTotalSupplyResponse\x12[\n\x06supply\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"%\n\x14QuerySupplyOfRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"H\n\x15QuerySupplyOfResponse\x12/\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"l\n$QueryTotalSupplyWithoutOffsetRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xc1\x01\n%QueryTotalSupplyWithoutOffsetResponse\x12[\n\x06supply\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"2\n!QuerySupplyOfWithoutOffsetRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"U\n\"QuerySupplyOfWithoutOffsetResponse\x12/\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x14\n\x12QueryParamsRequest\"H\n\x13QueryParamsResponse\x12\x31\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.bank.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\"X\n\x1aQueryDenomsMetadataRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x92\x01\n\x1bQueryDenomsMetadataResponse\x12\x36\n\tmetadatas\x18\x01 \x03(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"*\n\x19QueryDenomMetadataRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"S\n\x1aQueryDenomMetadataResponse\x12\x35\n\x08metadata\x18\x01 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00\"&\n\x15QueryBaseDenomRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\",\n\x16QueryBaseDenomResponse\x12\x12\n\nbase_denom\x18\x01 \x01(\t2\xd2\x0c\n\x05Query\x12\x98\x01\n\x07\x42\x61lance\x12(.cosmos.bank.v1beta1.QueryBalanceRequest\x1a).cosmos.bank.v1beta1.QueryBalanceResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/cosmos/bank/v1beta1/balances/{address}/by_denom\x12\x9b\x01\n\x0b\x41llBalances\x12,.cosmos.bank.v1beta1.QueryAllBalancesRequest\x1a-.cosmos.bank.v1beta1.QueryAllBalancesResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/bank/v1beta1/balances/{address}\x12\x8f\x01\n\x0bTotalSupply\x12,.cosmos.bank.v1beta1.QueryTotalSupplyRequest\x1a-.cosmos.bank.v1beta1.QueryTotalSupplyResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/supply\x12\x8e\x01\n\x08SupplyOf\x12).cosmos.bank.v1beta1.QuerySupplyOfRequest\x1a*.cosmos.bank.v1beta1.QuerySupplyOfResponse\"+\x82\xd3\xe4\x93\x02%\x12#/cosmos/bank/v1beta1/supply/{denom}\x12\xc5\x01\n\x18TotalSupplyWithoutOffset\x12\x39.cosmos.bank.v1beta1.QueryTotalSupplyWithoutOffsetRequest\x1a:.cosmos.bank.v1beta1.QueryTotalSupplyWithoutOffsetResponse\"2\x82\xd3\xe4\x93\x02,\x12*/cosmos/bank/v1beta1/supply_without_offset\x12\xc4\x01\n\x15SupplyOfWithoutOffset\x12\x36.cosmos.bank.v1beta1.QuerySupplyOfWithoutOffsetRequest\x1a\x37.cosmos.bank.v1beta1.QuerySupplyOfWithoutOffsetResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/cosmos/bank/v1beta1/supply_without_offset/{denom}\x12\x80\x01\n\x06Params\x12\'.cosmos.bank.v1beta1.QueryParamsRequest\x1a(.cosmos.bank.v1beta1.QueryParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/params\x12\xa6\x01\n\rDenomMetadata\x12..cosmos.bank.v1beta1.QueryDenomMetadataRequest\x1a/.cosmos.bank.v1beta1.QueryDenomMetadataResponse\"4\x82\xd3\xe4\x93\x02.\x12,/cosmos/bank/v1beta1/denoms_metadata/{denom}\x12\xa1\x01\n\x0e\x44\x65nomsMetadata\x12/.cosmos.bank.v1beta1.QueryDenomsMetadataRequest\x1a\x30.cosmos.bank.v1beta1.QueryDenomsMetadataResponse\",\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/denoms_metadata\x12\x8d\x01\n\tBaseDenom\x12*.cosmos.bank.v1beta1.QueryBaseDenomRequest\x1a+.cosmos.bank.v1beta1.QueryBaseDenomResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/cosmos/bank/v1beta1/base_denomB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
  _QUERYBALANCEREQUEST._options = None
  _QUERYBALANCEREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYALLBALANCESREQUEST._options = None
  _QUERYALLBALANCESREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYALLBALANCESRESPONSE.fields_by_name['balances']._options = None
  _QUERYALLBALANCESRESPONSE.fields_by_name['balances']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYTOTALSUPPLYREQUEST._options = None
  _QUERYTOTALSUPPLYREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply']._options = None
  _QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYSUPPLYOFRESPONSE.fields_by_name['amount']._options = None
  _QUERYSUPPLYOFRESPONSE.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _QUERYTOTALSUPPLYWITHOUTOFFSETREQUEST._options = None
  _QUERYTOTALSUPPLYWITHOUTOFFSETREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYTOTALSUPPLYWITHOUTOFFSETRESPONSE.fields_by_name['supply']._options = None
  _QUERYTOTALSUPPLYWITHOUTOFFSETRESPONSE.fields_by_name['supply']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYSUPPLYOFWITHOUTOFFSETRESPONSE.fields_by_name['amount']._options = None
  _QUERYSUPPLYOFWITHOUTOFFSETRESPONSE.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas']._options = None
  _QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas']._serialized_options = b'\310\336\037\000'
  _QUERYDENOMMETADATARESPONSE.fields_by_name['metadata']._options = None
  _QUERYDENOMMETADATARESPONSE.fields_by_name['metadata']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Balance']._options = None
  _QUERY.methods_by_name['Balance']._serialized_options = b'\202\323\344\223\0022\0220/cosmos/bank/v1beta1/balances/{address}/by_denom'
  _QUERY.methods_by_name['AllBalances']._options = None
  _QUERY.methods_by_name['AllBalances']._serialized_options = b'\202\323\344\223\002)\022\'/cosmos/bank/v1beta1/balances/{address}'
  _QUERY.methods_by_name['TotalSupply']._options = None
  _QUERY.methods_by_name['TotalSupply']._serialized_options = b'\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/supply'
  _QUERY.methods_by_name['SupplyOf']._options = None
  _QUERY.methods_by_name['SupplyOf']._serialized_options = b'\202\323\344\223\002%\022#/cosmos/bank/v1beta1/supply/{denom}'
  _QUERY.methods_by_name['TotalSupplyWithoutOffset']._options = None
  _QUERY.methods_by_name['TotalSupplyWithoutOffset']._serialized_options = b'\202\323\344\223\002,\022*/cosmos/bank/v1beta1/supply_without_offset'
  _QUERY.methods_by_name['SupplyOfWithoutOffset']._options = None
  _QUERY.methods_by_name['SupplyOfWithoutOffset']._serialized_options = b'\202\323\344\223\0024\0222/cosmos/bank/v1beta1/supply_without_offset/{denom}'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/params'
  _QUERY.methods_by_name['DenomMetadata']._options = None
  _QUERY.methods_by_name['DenomMetadata']._serialized_options = b'\202\323\344\223\002.\022,/cosmos/bank/v1beta1/denoms_metadata/{denom}'
  _QUERY.methods_by_name['DenomsMetadata']._options = None
  _QUERY.methods_by_name['DenomsMetadata']._serialized_options = b'\202\323\344\223\002&\022$/cosmos/bank/v1beta1/denoms_metadata'
  _QUERY.methods_by_name['BaseDenom']._options = None
  _QUERY.methods_by_name['BaseDenom']._serialized_options = b'\202\323\344\223\002!\022\037/cosmos/bank/v1beta1/base_denom'
  _QUERYBALANCEREQUEST._serialized_start=216
  _QUERYBALANCEREQUEST._serialized_end=279
  _QUERYBALANCERESPONSE._serialized_start=281
  _QUERYBALANCERESPONSE._serialized_end=347
  _QUERYALLBALANCESREQUEST._serialized_start=349
  _QUERYALLBALANCESREQUEST._serialized_end=461
  _QUERYALLBALANCESRESPONSE._serialized_start=464
  _QUERYALLBALANCESRESPONSE._serialized_end=646
  _QUERYTOTALSUPPLYREQUEST._serialized_start=648
  _QUERYTOTALSUPPLYREQUEST._serialized_end=743
  _QUERYTOTALSUPPLYRESPONSE._serialized_start=746
  _QUERYTOTALSUPPLYRESPONSE._serialized_end=926
  _QUERYSUPPLYOFREQUEST._serialized_start=928
  _QUERYSUPPLYOFREQUEST._serialized_end=965
  _QUERYSUPPLYOFRESPONSE._serialized_start=967
  _QUERYSUPPLYOFRESPONSE._serialized_end=1039
  _QUERYTOTALSUPPLYWITHOUTOFFSETREQUEST._serialized_start=1041
  _QUERYTOTALSUPPLYWITHOUTOFFSETREQUEST._serialized_end=1149
  _QUERYTOTALSUPPLYWITHOUTOFFSETRESPONSE._serialized_start=1152
  _QUERYTOTALSUPPLYWITHOUTOFFSETRESPONSE._serialized_end=1345
  _QUERYSUPPLYOFWITHOUTOFFSETREQUEST._serialized_start=1347
  _QUERYSUPPLYOFWITHOUTOFFSETREQUEST._serialized_end=1397
  _QUERYSUPPLYOFWITHOUTOFFSETRESPONSE._serialized_start=1399
  _QUERYSUPPLYOFWITHOUTOFFSETRESPONSE._serialized_end=1484
  _QUERYPARAMSREQUEST._serialized_start=1486
  _QUERYPARAMSREQUEST._serialized_end=1506
  _QUERYPARAMSRESPONSE._serialized_start=1508
  _QUERYPARAMSRESPONSE._serialized_end=1580
  _QUERYDENOMSMETADATAREQUEST._serialized_start=1582
  _QUERYDENOMSMETADATAREQUEST._serialized_end=1670
  _QUERYDENOMSMETADATARESPONSE._serialized_start=1673
  _QUERYDENOMSMETADATARESPONSE._serialized_end=1819
  _QUERYDENOMMETADATAREQUEST._serialized_start=1821
  _QUERYDENOMMETADATAREQUEST._serialized_end=1863
  _QUERYDENOMMETADATARESPONSE._serialized_start=1865
  _QUERYDENOMMETADATARESPONSE._serialized_end=1948
  _QUERYBASEDENOMREQUEST._serialized_start=1950
  _QUERYBASEDENOMREQUEST._serialized_end=1988
  _QUERYBASEDENOMRESPONSE._serialized_start=1990
  _QUERYBASEDENOMRESPONSE._serialized_end=2034
  _QUERY._serialized_start=2037
  _QUERY._serialized_end=3655
# @@protoc_insertion_point(module_scope)
