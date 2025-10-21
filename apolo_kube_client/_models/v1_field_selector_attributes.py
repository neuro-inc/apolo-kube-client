from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_field_selector_requirement import V1FieldSelectorRequirement
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1FieldSelectorAttributes",)


class V1FieldSelectorAttributes(BaseModel):
    raw_selector: str | None = Field(
        default=None,
        serialization_alias="rawSelector",
        validation_alias=AliasChoices("raw_selector", "rawSelector"),
    )

    requirements: Annotated[
        list[V1FieldSelectorRequirement], BeforeValidator(_collection_if_none("[]"))
    ] = []
