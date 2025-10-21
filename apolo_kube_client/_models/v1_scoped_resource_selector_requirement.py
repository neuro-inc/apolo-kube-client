from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ScopedResourceSelectorRequirement",)


class V1ScopedResourceSelectorRequirement(BaseModel):
    operator: str | None = None

    scope_name: str | None = Field(
        default=None,
        serialization_alias="scopeName",
        validation_alias=AliasChoices("scope_name", "scopeName"),
    )

    values: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
