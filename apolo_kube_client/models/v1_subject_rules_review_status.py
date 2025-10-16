from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_non_resource_rule import V1NonResourceRule
from .v1_resource_rule import V1ResourceRule

__all__ = ("V1SubjectRulesReviewStatus",)


class V1SubjectRulesReviewStatus(BaseModel):
    evaluation_error: str | None = Field(None, alias="evaluationError")

    incomplete: bool | None = Field(None, alias="incomplete")

    non_resource_rules: list[V1NonResourceRule] | None = Field(
        None, alias="nonResourceRules"
    )

    resource_rules: list[V1ResourceRule] | None = Field(None, alias="resourceRules")
