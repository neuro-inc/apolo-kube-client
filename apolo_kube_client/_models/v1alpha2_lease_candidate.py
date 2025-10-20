from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1alpha2_lease_candidate_spec import V1alpha2LeaseCandidateSpec

__all__ = ("V1alpha2LeaseCandidate",)


class V1alpha2LeaseCandidate(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1alpha2LeaseCandidateSpec = Field(
        default_factory=lambda: V1alpha2LeaseCandidateSpec()
    )
