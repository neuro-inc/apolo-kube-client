from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_validating_admission_policy_spec import V1ValidatingAdmissionPolicySpec
from .v1_validating_admission_policy_status import V1ValidatingAdmissionPolicyStatus

__all__ = ("V1ValidatingAdmissionPolicy",)


class V1ValidatingAdmissionPolicy(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1ValidatingAdmissionPolicySpec = Field(
        default_factory=lambda: V1ValidatingAdmissionPolicySpec()
    )

    status: V1ValidatingAdmissionPolicyStatus = Field(
        default_factory=lambda: V1ValidatingAdmissionPolicyStatus()
    )
