from pydantic import BaseModel, Field

from .v1_audit_annotation import V1AuditAnnotation
from .v1_match_condition import V1MatchCondition
from .v1_match_resources import V1MatchResources
from .v1_param_kind import V1ParamKind
from .v1_validation import V1Validation
from .v1_variable import V1Variable


class V1ValidatingAdmissionPolicySpec(BaseModel):
    audit_annotations: list[V1AuditAnnotation] | None = Field(
        None, alias="auditAnnotations"
    )

    failure_policy: str | None = Field(None, alias="failurePolicy")

    match_conditions: list[V1MatchCondition] | None = Field(
        None, alias="matchConditions"
    )

    match_constraints: V1MatchResources | None = Field(None, alias="matchConstraints")

    param_kind: V1ParamKind | None = Field(None, alias="paramKind")

    validations: list[V1Validation] | None = Field(None, alias="validations")

    variables: list[V1Variable] | None = Field(None, alias="variables")
