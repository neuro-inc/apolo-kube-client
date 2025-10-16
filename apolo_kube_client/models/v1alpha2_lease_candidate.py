from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1alpha2_lease_candidate_spec import V1alpha2LeaseCandidateSpec

__all__ = ("V1alpha2LeaseCandidate",)


class V1alpha2LeaseCandidate(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1alpha2LeaseCandidateSpec = Field(
        default_factory=lambda: V1alpha2LeaseCandidateSpec(), alias="spec"
    )
