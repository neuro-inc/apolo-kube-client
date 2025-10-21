from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_non_resource_rule import V1NonResourceRule
from .v1_resource_rule import V1ResourceRule
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SubjectRulesReviewStatus",)


class V1SubjectRulesReviewStatus(BaseModel):
    evaluation_error: str | None = Field(
        default=None,
        serialization_alias="evaluationError",
        validation_alias=AliasChoices("evaluation_error", "evaluationError"),
    )

    incomplete: bool | None = None

    non_resource_rules: Annotated[
        list[V1NonResourceRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="nonResourceRules",
        validation_alias=AliasChoices("non_resource_rules", "nonResourceRules"),
    )

    resource_rules: Annotated[
        list[V1ResourceRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="resourceRules",
        validation_alias=AliasChoices("resource_rules", "resourceRules"),
    )
