from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1beta1_mutating_admission_policy import V1beta1MutatingAdmissionPolicy

__all__ = ("V1beta1MutatingAdmissionPolicyList",)


class V1beta1MutatingAdmissionPolicyList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1beta1MutatingAdmissionPolicy] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
