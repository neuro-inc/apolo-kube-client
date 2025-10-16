from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_validating_admission_policy_binding import V1ValidatingAdmissionPolicyBinding

__all__ = ("V1ValidatingAdmissionPolicyBindingList",)


class V1ValidatingAdmissionPolicyBindingList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1ValidatingAdmissionPolicyBinding] = Field(
        default_factory=lambda: [], alias="items"
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
