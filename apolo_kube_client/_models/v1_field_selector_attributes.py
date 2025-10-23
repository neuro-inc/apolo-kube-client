from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_field_selector_requirement import V1FieldSelectorRequirement
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1FieldSelectorAttributes",)


class V1FieldSelectorAttributes(BaseModel):
    raw_selector: str | None = Field(
        default=None,
        serialization_alias="rawSelector",
        validation_alias=AliasChoices("raw_selector", "rawSelector"),
        exclude_if=_exclude_if,
    )

    requirements: Annotated[
        list[V1FieldSelectorRequirement], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
