# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dydxprotocol/vault/vault.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1e\x64ydxprotocol/vault/vault.proto\x12\x12\x64ydxprotocol.vault"F\n\x07VaultId\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.dydxprotocol.vault.VaultType\x12\x0e\n\x06number\x18\x02 \x01(\r*<\n\tVaultType\x12\x1a\n\x16VAULT_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fVAULT_TYPE_CLOB\x10\x01*\x9b\x01\n\x0bVaultStatus\x12\x1c\n\x18VAULT_STATUS_UNSPECIFIED\x10\x00\x12\x1c\n\x18VAULT_STATUS_DEACTIVATED\x10\x01\x12\x19\n\x15VAULT_STATUS_STAND_BY\x10\x02\x12\x18\n\x14VAULT_STATUS_QUOTING\x10\x03\x12\x1b\n\x17VAULT_STATUS_CLOSE_ONLY\x10\x04\x42\x39Z7github.com/dydxprotocol/v4-chain/protocol/x/vault/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dydxprotocol.vault.vault_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z7github.com/dydxprotocol/v4-chain/protocol/x/vault/types"
    _globals["_VAULTTYPE"]._serialized_start = 126
    _globals["_VAULTTYPE"]._serialized_end = 186
    _globals["_VAULTSTATUS"]._serialized_start = 189
    _globals["_VAULTSTATUS"]._serialized_end = 344
    _globals["_VAULTID"]._serialized_start = 54
    _globals["_VAULTID"]._serialized_end = 124
# @@protoc_insertion_point(module_scope)
