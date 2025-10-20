from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_mutating_admission_policy_binding_spec import (
    V1alpha1MutatingAdmissionPolicyBindingSpec,
)

__all__ = ("V1alpha1MutatingAdmissionPolicyBinding",)


class V1alpha1MutatingAdmissionPolicyBinding(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1alpha1MutatingAdmissionPolicyBindingSpec = Field(
        default_factory=lambda: V1alpha1MutatingAdmissionPolicyBindingSpec()
    )
