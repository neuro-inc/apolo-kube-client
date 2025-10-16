from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1beta1_lease_candidate_spec import V1beta1LeaseCandidateSpec

__all__ = ("V1beta1LeaseCandidate",)


class V1beta1LeaseCandidate(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1beta1LeaseCandidateSpec = Field(
        default_factory=lambda: V1beta1LeaseCandidateSpec(), alias="spec"
    )
