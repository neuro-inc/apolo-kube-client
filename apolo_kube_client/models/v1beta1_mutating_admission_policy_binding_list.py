from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1beta1_mutating_admission_policy_binding import (
    V1beta1MutatingAdmissionPolicyBinding,
)

__all__ = ("V1beta1MutatingAdmissionPolicyBindingList",)


class V1beta1MutatingAdmissionPolicyBindingList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1beta1MutatingAdmissionPolicyBinding] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
