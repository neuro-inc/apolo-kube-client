from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_audit_annotation import V1AuditAnnotation
from .v1_match_condition import V1MatchCondition
from .v1_match_resources import V1MatchResources
from .v1_param_kind import V1ParamKind
from .v1_validation import V1Validation
from .v1_variable import V1Variable
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ValidatingAdmissionPolicySpec",)


class V1ValidatingAdmissionPolicySpec(BaseModel):
    audit_annotations: Annotated[
        list[V1AuditAnnotation], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="auditAnnotations",
        validation_alias=AliasChoices("audit_annotations", "auditAnnotations"),
    )

    failure_policy: str | None = Field(
        default=None,
        serialization_alias="failurePolicy",
        validation_alias=AliasChoices("failure_policy", "failurePolicy"),
    )

    match_conditions: Annotated[
        list[V1MatchCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="matchConditions",
        validation_alias=AliasChoices("match_conditions", "matchConditions"),
    )

    match_constraints: Annotated[
        V1MatchResources, BeforeValidator(_default_if_none(V1MatchResources))
    ] = Field(
        default_factory=lambda: V1MatchResources(),
        serialization_alias="matchConstraints",
        validation_alias=AliasChoices("match_constraints", "matchConstraints"),
    )

    param_kind: Annotated[
        V1ParamKind, BeforeValidator(_default_if_none(V1ParamKind))
    ] = Field(
        default_factory=lambda: V1ParamKind(),
        serialization_alias="paramKind",
        validation_alias=AliasChoices("param_kind", "paramKind"),
    )

    validations: Annotated[
        list[V1Validation], BeforeValidator(_collection_if_none("[]"))
    ] = []

    variables: Annotated[
        list[V1Variable], BeforeValidator(_collection_if_none("[]"))
    ] = []
