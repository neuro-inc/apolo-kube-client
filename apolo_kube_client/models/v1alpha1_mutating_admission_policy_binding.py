from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_mutating_admission_policy_binding_spec import (
    V1alpha1MutatingAdmissionPolicyBindingSpec,
)

__all__ = ("V1alpha1MutatingAdmissionPolicyBinding",)


class V1alpha1MutatingAdmissionPolicyBinding(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1alpha1MutatingAdmissionPolicyBindingSpec = Field(
        default_factory=lambda: V1alpha1MutatingAdmissionPolicyBindingSpec(),
        alias="spec",
    )
