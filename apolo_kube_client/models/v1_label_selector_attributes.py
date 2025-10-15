from pydantic import BaseModel, Field

from .v1_label_selector_requirement import V1LabelSelectorRequirement


class V1LabelSelectorAttributes(BaseModel):
    raw_selector: str | None = Field(None, alias="rawSelector")

    requirements: list[V1LabelSelectorRequirement] | None = Field(
        None, alias="requirements"
    )
