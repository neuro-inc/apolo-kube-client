from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_audit_annotation import V1AuditAnnotation
from .v1_match_condition import V1MatchCondition
from .v1_match_resources import V1MatchResources
from .v1_param_kind import V1ParamKind
from .v1_validation import V1Validation
from .v1_variable import V1Variable

__all__ = ("V1ValidatingAdmissionPolicySpec",)


class V1ValidatingAdmissionPolicySpec(BaseModel):
    audit_annotations: list[V1AuditAnnotation] = Field(
        default_factory=lambda: [], alias="auditAnnotations"
    )

    failure_policy: str | None = Field(
        default_factory=lambda: None, alias="failurePolicy"
    )

    match_conditions: list[V1MatchCondition] = Field(
        default_factory=lambda: [], alias="matchConditions"
    )

    match_constraints: V1MatchResources = Field(
        default_factory=lambda: V1MatchResources(), alias="matchConstraints"
    )

    param_kind: V1ParamKind = Field(
        default_factory=lambda: V1ParamKind(), alias="paramKind"
    )

    validations: list[V1Validation] = Field(
        default_factory=lambda: [], alias="validations"
    )

    variables: list[V1Variable] = Field(default_factory=lambda: [], alias="variables")
