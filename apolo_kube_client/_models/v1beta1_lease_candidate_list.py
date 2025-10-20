from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_list_meta import V1ListMeta
from .v1beta1_lease_candidate import V1beta1LeaseCandidate

__all__ = ("V1beta1LeaseCandidateList",)


class V1beta1LeaseCandidateList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1beta1LeaseCandidate] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
