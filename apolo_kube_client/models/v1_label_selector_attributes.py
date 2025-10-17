from pydantic import AliasChoices, BaseModel, Field
from .v1_label_selector_requirement import V1LabelSelectorRequirement

__all__ = ("V1LabelSelectorAttributes",)


class V1LabelSelectorAttributes(BaseModel):
    raw_selector: str | None = Field(
        default=None,
        serialization_alias="rawSelector",
        validation_alias=AliasChoices("raw_selector", "rawSelector"),
    )

    requirements: list[V1LabelSelectorRequirement] = []
