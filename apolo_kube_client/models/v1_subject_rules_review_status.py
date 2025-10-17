from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_non_resource_rule import V1NonResourceRule
from .v1_resource_rule import V1ResourceRule

__all__ = ("V1SubjectRulesReviewStatus",)


class V1SubjectRulesReviewStatus(BaseModel):
    evaluation_error: str | None = Field(
        default=None,
        serialization_alias="evaluationError",
        validation_alias=AliasChoices("evaluation_error", "evaluationError"),
    )

    incomplete: bool | None = Field(default=None)

    non_resource_rules: list[V1NonResourceRule] = Field(
        default=[],
        serialization_alias="nonResourceRules",
        validation_alias=AliasChoices("non_resource_rules", "nonResourceRules"),
    )

    resource_rules: list[V1ResourceRule] = Field(
        default=[],
        serialization_alias="resourceRules",
        validation_alias=AliasChoices("resource_rules", "resourceRules"),
    )
