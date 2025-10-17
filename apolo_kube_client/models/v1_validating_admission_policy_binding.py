from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_validating_admission_policy_binding_spec import (
    V1ValidatingAdmissionPolicyBindingSpec,
)

__all__ = ("V1ValidatingAdmissionPolicyBinding",)


class V1ValidatingAdmissionPolicyBinding(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1ValidatingAdmissionPolicyBindingSpec = Field(
        default_factory=lambda: V1ValidatingAdmissionPolicyBindingSpec()
    )
