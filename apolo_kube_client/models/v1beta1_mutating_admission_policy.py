from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1beta1_mutating_admission_policy_spec import V1beta1MutatingAdmissionPolicySpec

__all__ = ("V1beta1MutatingAdmissionPolicy",)


class V1beta1MutatingAdmissionPolicy(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1beta1MutatingAdmissionPolicySpec = Field(
        default_factory=lambda: V1beta1MutatingAdmissionPolicySpec()
    )
