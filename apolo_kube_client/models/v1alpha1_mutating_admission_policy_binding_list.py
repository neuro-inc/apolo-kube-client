from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1alpha1_mutating_admission_policy_binding import (
    V1alpha1MutatingAdmissionPolicyBinding,
)

__all__ = ("V1alpha1MutatingAdmissionPolicyBindingList",)


class V1alpha1MutatingAdmissionPolicyBindingList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1alpha1MutatingAdmissionPolicyBinding] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
