from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_label_selector_requirement import V1LabelSelectorRequirement
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LabelSelectorAttributes",)


class V1LabelSelectorAttributes(BaseModel):
    raw_selector: str | None = Field(
        default=None,
        serialization_alias="rawSelector",
        validation_alias=AliasChoices("raw_selector", "rawSelector"),
    )

    requirements: Annotated[
        list[V1LabelSelectorRequirement], BeforeValidator(_collection_if_none("[]"))
    ] = []
