"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.gov.v1beta1.gov_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the gov module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STARTING_PROPOSAL_ID_FIELD_NUMBER: builtins.int
    DEPOSITS_FIELD_NUMBER: builtins.int
    VOTES_FIELD_NUMBER: builtins.int
    PROPOSALS_FIELD_NUMBER: builtins.int
    DEPOSIT_PARAMS_FIELD_NUMBER: builtins.int
    VOTING_PARAMS_FIELD_NUMBER: builtins.int
    TALLY_PARAMS_FIELD_NUMBER: builtins.int
    starting_proposal_id: builtins.int
    """starting_proposal_id is the ID of the starting proposal."""
    @property
    def deposits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.gov.v1beta1.gov_pb2.Deposit]:
        """deposits defines all the deposits present at genesis."""
    @property
    def votes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.gov.v1beta1.gov_pb2.Vote]:
        """votes defines all the votes present at genesis."""
    @property
    def proposals(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.gov.v1beta1.gov_pb2.Proposal]:
        """proposals defines all the proposals present at genesis."""
    @property
    def deposit_params(self) -> cosmos.gov.v1beta1.gov_pb2.DepositParams:
        """params defines all the paramaters of related to deposit."""
    @property
    def voting_params(self) -> cosmos.gov.v1beta1.gov_pb2.VotingParams:
        """params defines all the paramaters of related to voting."""
    @property
    def tally_params(self) -> cosmos.gov.v1beta1.gov_pb2.TallyParams:
        """params defines all the paramaters of related to tally."""
    def __init__(
        self,
        *,
        starting_proposal_id: builtins.int = ...,
        deposits: collections.abc.Iterable[cosmos.gov.v1beta1.gov_pb2.Deposit] | None = ...,
        votes: collections.abc.Iterable[cosmos.gov.v1beta1.gov_pb2.Vote] | None = ...,
        proposals: collections.abc.Iterable[cosmos.gov.v1beta1.gov_pb2.Proposal] | None = ...,
        deposit_params: cosmos.gov.v1beta1.gov_pb2.DepositParams | None = ...,
        voting_params: cosmos.gov.v1beta1.gov_pb2.VotingParams | None = ...,
        tally_params: cosmos.gov.v1beta1.gov_pb2.TallyParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["deposit_params", b"deposit_params", "tally_params", b"tally_params", "voting_params", b"voting_params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deposit_params", b"deposit_params", "deposits", b"deposits", "proposals", b"proposals", "starting_proposal_id", b"starting_proposal_id", "tally_params", b"tally_params", "votes", b"votes", "voting_params", b"voting_params"]) -> None: ...

global___GenesisState = GenesisState
