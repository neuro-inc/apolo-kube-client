from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1beta1_mutating_admission_policy_binding_spec import (
    V1beta1MutatingAdmissionPolicyBindingSpec,
)

__all__ = ("V1beta1MutatingAdmissionPolicyBinding",)


class V1beta1MutatingAdmissionPolicyBinding(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1beta1MutatingAdmissionPolicyBindingSpec = Field(
        default_factory=lambda: V1beta1MutatingAdmissionPolicyBindingSpec()
    )
