# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/vault/params.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from dydxprotocol.vault import vault_pb2 as dydxprotocol_dot_vault_dot_vault__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1f\x64ydxprotocol/vault/params.proto\x12\x12\x64ydxprotocol.vault\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x64ydxprotocol/vault/vault.proto\x1a\x14gogoproto/gogo.proto"\xa0\x02\n\rQuotingParams\x12\x0e\n\x06layers\x18\x01 \x01(\r\x12\x16\n\x0espread_min_ppm\x18\x02 \x01(\r\x12\x19\n\x11spread_buffer_ppm\x18\x03 \x01(\r\x12\x17\n\x0fskew_factor_ppm\x18\x04 \x01(\r\x12\x1a\n\x12order_size_pct_ppm\x18\x05 \x01(\r\x12 \n\x18order_expiration_seconds\x18\x06 \x01(\r\x12u\n#activation_threshold_quote_quantums\x18\x07 \x01(\x0c\x42H\xc8\xde\x1f\x00\xda\xde\x1f@github.com/dydxprotocol/v4-chain/protocol/dtypes.SerializableInt"y\n\x0bVaultParams\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.dydxprotocol.vault.VaultStatus\x12\x39\n\x0equoting_params\x18\x02 \x01(\x0b\x32!.dydxprotocol.vault.QuotingParams"z\n\x0eOperatorParams\x12*\n\x08operator\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12<\n\x08metadata\x18\x02 \x01(\x0b\x32$.dydxprotocol.vault.OperatorMetadataB\x04\xc8\xde\x1f\x00"5\n\x10OperatorMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t"\x99\x02\n\x06Params\x12\x0e\n\x06layers\x18\x01 \x01(\r\x12\x16\n\x0espread_min_ppm\x18\x02 \x01(\r\x12\x19\n\x11spread_buffer_ppm\x18\x03 \x01(\r\x12\x17\n\x0fskew_factor_ppm\x18\x04 \x01(\r\x12\x1a\n\x12order_size_pct_ppm\x18\x05 \x01(\r\x12 \n\x18order_expiration_seconds\x18\x06 \x01(\r\x12u\n#activation_threshold_quote_quantums\x18\x07 \x01(\x0c\x42H\xc8\xde\x1f\x00\xda\xde\x1f@github.com/dydxprotocol/v4-chain/protocol/dtypes.SerializableIntB9Z7github.com/dydxprotocol/v4-chain/protocol/x/vault/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.vault.params_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z7github.com/dydxprotocol/v4-chain/protocol/x/vault/types"
    _globals["_QUOTINGPARAMS"].fields_by_name["activation_threshold_quote_quantums"]._loaded_options = None
    _globals["_QUOTINGPARAMS"].fields_by_name[
        "activation_threshold_quote_quantums"
    ]._serialized_options = (
        b"\310\336\037\000\332\336\037@github.com/dydxprotocol/v4-chain/protocol/dtypes.SerializableInt"
    )
    _globals["_OPERATORPARAMS"].fields_by_name["operator"]._loaded_options = None
    _globals["_OPERATORPARAMS"].fields_by_name["operator"]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_OPERATORPARAMS"].fields_by_name["metadata"]._loaded_options = None
    _globals["_OPERATORPARAMS"].fields_by_name["metadata"]._serialized_options = b"\310\336\037\000"
    _globals["_PARAMS"].fields_by_name["activation_threshold_quote_quantums"]._loaded_options = None
    _globals["_PARAMS"].fields_by_name[
        "activation_threshold_quote_quantums"
    ]._serialized_options = (
        b"\310\336\037\000\332\336\037@github.com/dydxprotocol/v4-chain/protocol/dtypes.SerializableInt"
    )
    _globals["_QUOTINGPARAMS"]._serialized_start = 137
    _globals["_QUOTINGPARAMS"]._serialized_end = 425
    _globals["_VAULTPARAMS"]._serialized_start = 427
    _globals["_VAULTPARAMS"]._serialized_end = 548
    _globals["_OPERATORPARAMS"]._serialized_start = 550
    _globals["_OPERATORPARAMS"]._serialized_end = 672
    _globals["_OPERATORMETADATA"]._serialized_start = 674
    _globals["_OPERATORMETADATA"]._serialized_end = 727
    _globals["_PARAMS"]._serialized_start = 730
    _globals["_PARAMS"]._serialized_end = 1011
# @@protoc_insertion_point(module_scope)
