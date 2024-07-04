import os
import subprocess
import sys


def validate_proto_file(file_path):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)


# Define the directories of the SDK repositories
GENERATED_DIR = "./../tmp"
ROOT_PROTO_DIR = "./../repos_protobufs"
COSMOS_PROTO_DIR = os.path.join(ROOT_PROTO_DIR, "cosmos")
IBC_PROTO_DIR = os.path.join(ROOT_PROTO_DIR, "ibc")
COSMWASM_PROTO_DIR = os.path.join(ROOT_PROTO_DIR, "cosmwasm")
TENDERMINT_PROTO_DIR = os.path.join(ROOT_PROTO_DIR, "tendermint")
OSMOSIS_PROTO_DIR = os.path.join(ROOT_PROTO_DIR, "osmosis")
GOGO_PROTO_DIR = os.path.join(ROOT_PROTO_DIR, "gogoproto")

# Choose the files you want to convert
PROTO_FILES = [
    os.path.join(OSMOSIS_PROTO_DIR, "concentratedliquidity/v1beta1/genesis.proto"),
    os.path.join(OSMOSIS_PROTO_DIR, "concentratedliquidity/v1beta1/gov.proto"),
    os.path.join(OSMOSIS_PROTO_DIR, "concentratedliquidity/v1beta1/incentive_record.proto"),
    os.path.join(OSMOSIS_PROTO_DIR, "concentratedliquidity/v1beta1/pool.proto"),
    os.path.join(OSMOSIS_PROTO_DIR, "concentratedliquidity/v1beta1/position.proto"),
    os.path.join(OSMOSIS_PROTO_DIR, "concentratedliquidity/v1beta1/query.proto"),
    os.path.join(OSMOSIS_PROTO_DIR, "concentratedliquidity/v1beta1/tick_info.proto"),
    os.path.join(OSMOSIS_PROTO_DIR, "concentratedliquidity/v1beta1/tx.proto"),
]


os.makedirs(GENERATED_DIR, exist_ok=True)

for proto_file in PROTO_FILES:
    validate_proto_file(proto_file)

for proto_file in PROTO_FILES:
    protoc_command = [
        "protoc",
        f"--proto_path={ROOT_PROTO_DIR}",
        f"--python_out={GENERATED_DIR}",
        f"--mypy_out=.",
        proto_file,
    ]
    try:
        subprocess.run(protoc_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during protobuf compilation: {e}")
        sys.exit(1)

print(f"Protobuf files have been compiled to Python and output to {GENERATED_DIR}")
