from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_validating_admission_policy_spec import V1ValidatingAdmissionPolicySpec
from .v1_validating_admission_policy_status import V1ValidatingAdmissionPolicyStatus

__all__ = ("V1ValidatingAdmissionPolicy",)


class V1ValidatingAdmissionPolicy(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1ValidatingAdmissionPolicySpec = Field(
        default_factory=lambda: V1ValidatingAdmissionPolicySpec()
    )

    status: V1ValidatingAdmissionPolicyStatus = Field(
        default_factory=lambda: V1ValidatingAdmissionPolicyStatus()
    )
