# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: stride/airdrop/airdrop.proto
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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cstride/airdrop/airdrop.proto\x12\x0estride.airdrop\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\'\n\x06Params\x12\x1d\n\x15period_length_seconds\x18\x01 \x01(\x03"\xe5\x01\n\x0eUserAllocation\x12\x12\n\nairdrop_id\x18\x01 \x01(\t\x12)\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12.\n\x07\x63laimed\x18\x03 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\x12\x30\n\tforfeited\x18\x04 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\x12\x32\n\x0b\x61llocations\x18\x05 \x03(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int"\x8c\x04\n\x07\x41irdrop\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0creward_denom\x18\x02 \x01(\t\x12\x41\n\x17\x64istribution_start_date\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12?\n\x15\x64istribution_end_date\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12\x37\n\rclawback_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12\x42\n\x18\x63laim_type_deadline_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12@\n\x13\x65\x61rly_claim_penalty\x18\x07 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x35\n\x13\x64istributor_address\x18\x08 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x33\n\x11\x61llocator_address\x18\t \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x30\n\x0elinker_address\x18\n \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString*3\n\tClaimType\x12\x0f\n\x0b\x43LAIM_DAILY\x10\x00\x12\x0f\n\x0b\x43LAIM_EARLY\x10\x01\x1a\x04\x88\xa3\x1e\x00\x42\x33Z1github.com/Stride-Labs/stride/v24/x/airdrop/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "stride.airdrop.airdrop_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"Z1github.com/Stride-Labs/stride/v24/x/airdrop/types"
    )
    _globals["_CLAIMTYPE"]._loaded_options = None
    _globals["_CLAIMTYPE"]._serialized_options = b"\210\243\036\000"
    _globals["_USERALLOCATION"].fields_by_name["address"]._loaded_options = None
    _globals["_USERALLOCATION"].fields_by_name[
        "address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_USERALLOCATION"].fields_by_name["claimed"]._loaded_options = None
    _globals["_USERALLOCATION"].fields_by_name[
        "claimed"
    ]._serialized_options = b"\310\336\037\000\332\336\037\025cosmossdk.io/math.Int"
    _globals["_USERALLOCATION"].fields_by_name["forfeited"]._loaded_options = None
    _globals["_USERALLOCATION"].fields_by_name[
        "forfeited"
    ]._serialized_options = b"\310\336\037\000\332\336\037\025cosmossdk.io/math.Int"
    _globals["_USERALLOCATION"].fields_by_name["allocations"]._loaded_options = None
    _globals["_USERALLOCATION"].fields_by_name[
        "allocations"
    ]._serialized_options = b"\310\336\037\000\332\336\037\025cosmossdk.io/math.Int"
    _globals["_AIRDROP"].fields_by_name[
        "distribution_start_date"
    ]._loaded_options = None
    _globals["_AIRDROP"].fields_by_name[
        "distribution_start_date"
    ]._serialized_options = b"\220\337\037\001"
    _globals["_AIRDROP"].fields_by_name["distribution_end_date"]._loaded_options = None
    _globals["_AIRDROP"].fields_by_name[
        "distribution_end_date"
    ]._serialized_options = b"\220\337\037\001"
    _globals["_AIRDROP"].fields_by_name["clawback_date"]._loaded_options = None
    _globals["_AIRDROP"].fields_by_name[
        "clawback_date"
    ]._serialized_options = b"\220\337\037\001"
    _globals["_AIRDROP"].fields_by_name[
        "claim_type_deadline_date"
    ]._loaded_options = None
    _globals["_AIRDROP"].fields_by_name[
        "claim_type_deadline_date"
    ]._serialized_options = b"\220\337\037\001"
    _globals["_AIRDROP"].fields_by_name["early_claim_penalty"]._loaded_options = None
    _globals["_AIRDROP"].fields_by_name[
        "early_claim_penalty"
    ]._serialized_options = (
        b"\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec"
    )
    _globals["_AIRDROP"].fields_by_name["distributor_address"]._loaded_options = None
    _globals["_AIRDROP"].fields_by_name[
        "distributor_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_AIRDROP"].fields_by_name["allocator_address"]._loaded_options = None
    _globals["_AIRDROP"].fields_by_name[
        "allocator_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_AIRDROP"].fields_by_name["linker_address"]._loaded_options = None
    _globals["_AIRDROP"].fields_by_name[
        "linker_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_CLAIMTYPE"]._serialized_start = 930
    _globals["_CLAIMTYPE"]._serialized_end = 981
    _globals["_PARAMS"]._serialized_start = 130
    _globals["_PARAMS"]._serialized_end = 169
    _globals["_USERALLOCATION"]._serialized_start = 172
    _globals["_USERALLOCATION"]._serialized_end = 401
    _globals["_AIRDROP"]._serialized_start = 404
    _globals["_AIRDROP"]._serialized_end = 928
# @@protoc_insertion_point(module_scope)
