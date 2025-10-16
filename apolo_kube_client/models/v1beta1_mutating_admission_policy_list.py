from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1beta1_mutating_admission_policy import V1beta1MutatingAdmissionPolicy

__all__ = ("V1beta1MutatingAdmissionPolicyList",)


class V1beta1MutatingAdmissionPolicyList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1beta1MutatingAdmissionPolicy] = Field(
        default_factory=lambda: [], alias="items"
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
