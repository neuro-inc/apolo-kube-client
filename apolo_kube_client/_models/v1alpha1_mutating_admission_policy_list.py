from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_list_meta import V1ListMeta
from .v1alpha1_mutating_admission_policy import V1alpha1MutatingAdmissionPolicy

__all__ = ("V1alpha1MutatingAdmissionPolicyList",)


class V1alpha1MutatingAdmissionPolicyList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1alpha1MutatingAdmissionPolicy] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
