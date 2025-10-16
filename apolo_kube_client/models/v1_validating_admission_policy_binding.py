from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_validating_admission_policy_binding_spec import (
    V1ValidatingAdmissionPolicyBindingSpec,
)

__all__ = ("V1ValidatingAdmissionPolicyBinding",)


class V1ValidatingAdmissionPolicyBinding(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1ValidatingAdmissionPolicyBindingSpec | None = Field(None, alias="spec")
