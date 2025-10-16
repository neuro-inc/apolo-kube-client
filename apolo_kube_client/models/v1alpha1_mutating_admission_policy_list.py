from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1alpha1_mutating_admission_policy import V1alpha1MutatingAdmissionPolicy

__all__ = ("V1alpha1MutatingAdmissionPolicyList",)


class V1alpha1MutatingAdmissionPolicyList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1alpha1MutatingAdmissionPolicy] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
