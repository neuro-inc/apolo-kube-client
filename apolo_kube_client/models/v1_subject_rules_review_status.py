from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_non_resource_rule import V1NonResourceRule
from .v1_resource_rule import V1ResourceRule

__all__ = ("V1SubjectRulesReviewStatus",)


class V1SubjectRulesReviewStatus(BaseModel):
    evaluation_error: str | None = Field(
        default_factory=lambda: None, alias="evaluationError"
    )

    incomplete: bool | None = Field(default_factory=lambda: None, alias="incomplete")

    non_resource_rules: list[V1NonResourceRule] = Field(
        default_factory=lambda: [], alias="nonResourceRules"
    )

    resource_rules: list[V1ResourceRule] = Field(
        default_factory=lambda: [], alias="resourceRules"
    )
