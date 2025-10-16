from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1beta1_validating_admission_policy import V1beta1ValidatingAdmissionPolicy

__all__ = ("V1beta1ValidatingAdmissionPolicyList",)


class V1beta1ValidatingAdmissionPolicyList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1beta1ValidatingAdmissionPolicy] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
