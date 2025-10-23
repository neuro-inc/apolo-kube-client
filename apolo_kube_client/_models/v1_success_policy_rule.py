from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1SuccessPolicyRule",)


class V1SuccessPolicyRule(BaseModel):
    succeeded_count: int | None = Field(
        default=None,
        serialization_alias="succeededCount",
        validation_alias=AliasChoices("succeeded_count", "succeededCount"),
        exclude_if=_exclude_if,
    )

    succeeded_indexes: str | None = Field(
        default=None,
        serialization_alias="succeededIndexes",
        validation_alias=AliasChoices("succeeded_indexes", "succeededIndexes"),
        exclude_if=_exclude_if,
    )
