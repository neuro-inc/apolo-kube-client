from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_validating_admission_policy_binding import V1ValidatingAdmissionPolicyBinding

__all__ = ("V1ValidatingAdmissionPolicyBindingList",)


class V1ValidatingAdmissionPolicyBindingList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ValidatingAdmissionPolicyBinding] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
