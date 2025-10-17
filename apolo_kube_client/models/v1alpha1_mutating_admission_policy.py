from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_mutating_admission_policy_spec import V1alpha1MutatingAdmissionPolicySpec

__all__ = ("V1alpha1MutatingAdmissionPolicy",)


class V1alpha1MutatingAdmissionPolicy(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1alpha1MutatingAdmissionPolicySpec = Field(
        default_factory=lambda: V1alpha1MutatingAdmissionPolicySpec()
    )
