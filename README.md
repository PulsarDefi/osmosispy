# Convert ProtoBuf Files to Python

## Requirements
   - protobuf-compiler installed on the computer
      
      For example in MacOs:
      ```sh
      brew install protobuf
      ```
   - mypy-protobuf library installed on python
      ```sh
      pip install mypy-protobuf
      ```

## Step by step

1. **Some Background**:

   - The Osmosis SDK uses protobuf files to communicate with the osmosis chain, similar to the Cosmos SDK.

   - The protobuf files of the most important SDKs on Cosmos are located in the `repos_protobufs` folder.
   
   - The Python files converted from `repos_protobufs` are located in the `osmosis_proto` folder.

2. In the `scripts/generate_python_from_protobuf.py` file, you can convert the proto files to Python files.

3. **Specifying Proto File Paths:** 
   
   You can specify which proto files to convert in two ways:
   - **Convert an Entire Directory**: Add the path of the directory containing the proto files to the `PROTO_DIRECTORIES` list in the script.

   - **Convert Specific Files**: Add individual file paths to the `proto_files` list in the script, for this remove the function `get_proto_files_from_directories(PROTO_DIRECTORIES)` that is being called.


4. Run the script with the command `python generate_python_from_protobuf.py` in the directory of the script:
   ```sh
   python generate_python_from_protobuf.py
   ```

   - If the script runs successfully, the Python files will be generated in the `tmp` folder. 

   - Copy the files to their destination in the `osmosis_proto` folder. 
   
   - Try to maintain the same folder structure as the `repos_protobufs` folder, like how the protobuf files are organized. 
   
   - Read the section "Warning" below for more information.

5. **Handling Errors**:

   If the script retrieves a "File not found" error, there is probably a missing dependency. This means some protobuf files of some SDK are not present in the `repos_protobufs` folder.
     1. The error will provide the name of the missing dependency.

     2. Copy the dependency name, search for it on GitHub.

     3. Add the new proto files to the `repos_protobufs` folder.

## Warning

The version of the Protobuf compiler used in the files that are converted to `.py` contains an issue. The Protobuf compiler imports a non-existent library:

```python
from google.protobuf import runtime_version as _runtime_version
```

Additionally, the following code (an example) is included:

```python
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'osmosis/concentratedliquidity/v1beta1/query.proto'
)
```

This code needs to be manually removed from each generated `.py` file. While this is somewhat tedious, after making these changes, the compilation of the repository will work correctly.

