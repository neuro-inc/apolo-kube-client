from pydantic import AliasChoices, BaseModel, Field
from .v1_audit_annotation import V1AuditAnnotation
from .v1_match_condition import V1MatchCondition
from .v1_match_resources import V1MatchResources
from .v1_param_kind import V1ParamKind
from .v1_validation import V1Validation
from .v1_variable import V1Variable

__all__ = ("V1ValidatingAdmissionPolicySpec",)


class V1ValidatingAdmissionPolicySpec(BaseModel):
    audit_annotations: list[V1AuditAnnotation] = Field(
        default=[],
        serialization_alias="auditAnnotations",
        validation_alias=AliasChoices("audit_annotations", "auditAnnotations"),
    )

    failure_policy: str | None = Field(
        default=None,
        serialization_alias="failurePolicy",
        validation_alias=AliasChoices("failure_policy", "failurePolicy"),
    )

    match_conditions: list[V1MatchCondition] = Field(
        default=[],
        serialization_alias="matchConditions",
        validation_alias=AliasChoices("match_conditions", "matchConditions"),
    )

    match_constraints: V1MatchResources = Field(
        default_factory=lambda: V1MatchResources(),
        serialization_alias="matchConstraints",
        validation_alias=AliasChoices("match_constraints", "matchConstraints"),
    )

    param_kind: V1ParamKind = Field(
        default_factory=lambda: V1ParamKind(),
        serialization_alias="paramKind",
        validation_alias=AliasChoices("param_kind", "paramKind"),
    )

    validations: list[V1Validation] = []

    variables: list[V1Variable] = []
