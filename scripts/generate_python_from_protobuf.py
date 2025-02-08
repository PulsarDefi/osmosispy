import os
import sys
import subprocess


def validate_proto_file(file_path):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)


def get_proto_files_from_directories(directories):
    proto_files = []
    for directory in directories:
        if not os.path.isdir(directory):
            print(f"Directory not found: {directory}")
            sys.exit(1)
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".proto"):
                    proto_files.append(os.path.normpath(os.path.join(root, file)))
    return proto_files


# Define the directories of the SDK repositories
GENERATED_DIR = os.path.abspath("./../tmp")
ROOT_PROTO_DIR = os.path.abspath("./../repos_protobufs")
OSMOSIS_PROTO_DIR = os.path.join(ROOT_PROTO_DIR, "osmosis")
STRIDE_PROTO_DIR = os.path.join(ROOT_PROTO_DIR, "stride")
DYDX_PROTO_DIR = os.path.join(ROOT_PROTO_DIR, "dydxprotocol")
# Define the directories of the protobuf files
PROTO_DIRECTORIES = [DYDX_PROTO_DIR]

os.makedirs(GENERATED_DIR, exist_ok=True)
proto_files = get_proto_files_from_directories(PROTO_DIRECTORIES)

for proto_file in proto_files:
    validate_proto_file(proto_file)

for proto_file in proto_files:
    protoc_command = [
        "protoc",
        f"--proto_path={os.path.normpath(ROOT_PROTO_DIR)}",
        f"--python_out={os.path.normpath(GENERATED_DIR)}",
        f"--mypy_out={os.path.normpath(GENERATED_DIR)}",
        os.path.normpath(proto_file),
    ]

    try:
        if os.name == "nt":  # Windows
            subprocess.run(protoc_command, check=True, shell=True)
        else:  # macOS/Linux
            subprocess.run(protoc_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during protobuf compilation: {e}")
        sys.exit(1)

print(f"Protobuf files have been compiled to Python and output to {GENERATED_DIR}")
