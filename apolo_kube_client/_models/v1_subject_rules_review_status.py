from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    incomplete: bool | None = Field(default=None, exclude_if=_exclude_if)

    non_resource_rules: Annotated[
        list[V1NonResourceRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="nonResourceRules",
        validation_alias=AliasChoices("non_resource_rules", "nonResourceRules"),
        exclude_if=_exclude_if,
    )

    resource_rules: Annotated[
        list[V1ResourceRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="resourceRules",
        validation_alias=AliasChoices("resource_rules", "resourceRules"),
        exclude_if=_exclude_if,
    )
