from pydantic import BaseModel, Field

from .v1beta1_audit_annotation import V1beta1AuditAnnotation
from .v1beta1_match_condition import V1beta1MatchCondition
from .v1beta1_match_resources import V1beta1MatchResources
from .v1beta1_param_kind import V1beta1ParamKind
from .v1beta1_validation import V1beta1Validation
from .v1beta1_variable import V1beta1Variable


class V1beta1ValidatingAdmissionPolicySpec(BaseModel):
    audit_annotations: list[V1beta1AuditAnnotation] | None = Field(
        None, alias="auditAnnotations"
    )

    failure_policy: str | None = Field(None, alias="failurePolicy")

    match_conditions: list[V1beta1MatchCondition] | None = Field(
        None, alias="matchConditions"
    )

    match_constraints: V1beta1MatchResources | None = Field(
        None, alias="matchConstraints"
    )

    param_kind: V1beta1ParamKind | None = Field(None, alias="paramKind")

    validations: list[V1beta1Validation] | None = Field(None, alias="validations")

    variables: list[V1beta1Variable] | None = Field(None, alias="variables")
