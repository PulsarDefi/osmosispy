# Osmosis python SDK

<!-- Python-based client for interacting with the Osmosis AMM. -->

Python SDK for interacting with the Osmosis AMM.

<!-- Badges -->

[![Project Status: WIP -- Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://img.shields.io/badge/repo%20status-WIP-yellow.svg)](https://www.repostatus.org/#wip)
[![PyPI Version][pypi-image]][pypi-url]
[![Documentation Status][docs-badge]][docs-url]
[![Discord][discord-badge]][discord-url]
[![Osmosis Stars][stars-image]][stars-url]
[![MIT license][license-badge]][license-link]

<!-- Badges links -->

[docs-badge]: https://img.shields.io/badge/docs-passing-green.svg
[docs-url]: https://docs.osmosis.zone/
[discord-badge]: https://dcbadge.vercel.app/api/server/osmosis?style=flat
[discord-url]: https://discord.gg/osmosis
[stars-image]: https://img.shields.io/github/stars/osmosis-labs?style=social
[stars-url]: https://github.com/osmosis-labs
[pypi-image]: https://img.shields.io/pypi/v/osmosispy
[pypi-url]: https://pypi.org/project/osmosispy/
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[license-link]: https://github.com/sbneo2022/osmosispy/blob/master/LICENSE

The `osmosispy` and `osmosis_proto` package allows you to interact with the Osmosis AMM using Python.

#### README Contents

- [Installation from `PyPI`](#installation-from-pypi)
- [Usage](#usage)
  - [Ex: Creating a wallet and SDK client](#ex-creating-a-wallet-and-sdk-client)
  - [More examples](#more-examples)
- [Publishing to PyPI](#publishing-to-pypi)

## Installation from `PyPI`

```bash
python -m pip install --upgrade pip

pip install osmosispy  # requires Python 3.11.2+
```

## Usage

### Ex: Creating a wallet and SDK client

**example.py**

```python
#!/usr/bin/env python3

import osmosispy

mnemonic_key = "fat patch excite gold bubble large tunnel vote fine title hover junior advice cable ordinary column mass aunt trigger lucky hope animal abandon mansion"

# authorize in the mainnet
network = osmosispy.Network.mainnet()

trader = osmosispy.Sdk.authorize(key=mnemonic_key).with_network(network)

# print the address
print(trader.address)
```

```console
$ python3 example.py
osmo1jggt8pcj2d8m9n62luytf8sdncj5uxfs3su2my
```

### More examples

For more examples see the [examples directory](/examples).

- [connection and base methods](/examples/connect.ipynb)
- [trading client](/examples/trading_client.ipynb)

## Publishing to PyPI

The publish workflow looks like this:

1. Code-gen the new types from the chain. If there are changes, these should be committed.

   ```sh
   poetry run make proto-gen
   ```

2. Increment the package version. For example, use `poetry version preminor` to do a pre-release for a minor version.

   ```sh
   poetry version [update-keyword]
   ```

3. Create a tag and push it the remote origin.

   ```sh
   git tag -asm "v1.2.3" v1.2.3
   git push --tags
   ```

4. The tag will trigger a [GitHub Action Workflow](https://github.com/sbneo2022/osmosispy/actions/workflows/publish.yml).


## Convert ProtoBuf Files to Python

   **Requirements**
   - protobuf-compiler installed on the computer
      
      For example in MacOs:
      ```sh
      brew install protobuf
      ```
   - mypy-protobuf library installed on python
      ```sh
      pip install mypy-protobuf
      ```


1. **Some background**:
   - The Osmosis SDK uses protobuf files to communicate with the osmosis chain, similar to the Cosmos SDK.
   - The protobuf files of the most important SDKs on Cosmos are located in the `repos_protobufs` folder.
   - The Python files converted from `repos_protobufs` are located in the `osmosis_proto` folder.

2. In the `scripts/generate_python_from_protobuf.py` file, you can convert the proto files to Python files.

3. In the variable `PROTO_FILES`, there are two examples:
   - `concentratedliquidity/v1beta1/query.proto`
   - `concentratedliquidity/v1beta1/tick_info.proto`

4. Choose the paths of the proto files you want to convert. You can add more proto files to `PROTO_FILES` to be converted into Python files.

5. Run the script with the command `python generate_python_from_protobuf.py` in the directory of the script:
   ```sh
   python generate_python_from_protobuf.py
   ```

   - If the script runs successfully, the Python files will be generated in the `tmp` folder. Copy the files to their destination in the `osmosis_proto` folder. Try to maintain the same folder structure as the `repos_protobufs` folder, like how the protobuf files are organized.

   - If the script retrieves a "File not found" error, there is probably a missing dependency. This means some protobuf files of some SDK are not present in the `repos_protobufs` folder.
     1. The error will provide the name of the missing dependency.
     2. Copy the dependency name, search for it on GitHub, and add the new proto files to the `repos_protobufs` folder.
     3. Add the new path of the proto SDK repositories to the global variables, as in the example:
        ```python
        GOGO_PROTO_DIR = os.path.join(ROOT_PROTO_DIR, "gogoproto")
        ```