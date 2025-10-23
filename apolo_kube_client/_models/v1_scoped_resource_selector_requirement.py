from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ScopedResourceSelectorRequirement",)


class V1ScopedResourceSelectorRequirement(BaseModel):
    operator: str | None = Field(default=None, exclude_if=_exclude_if)

    scope_name: str | None = Field(
        default=None,
        serialization_alias="scopeName",
        validation_alias=AliasChoices("scope_name", "scopeName"),
        exclude_if=_exclude_if,
    )

    values: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )
