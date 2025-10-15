from pydantic import BaseModel, Field

from .v1_field_selector_requirement import V1FieldSelectorRequirement


class V1FieldSelectorAttributes(BaseModel):
    raw_selector: str | None = Field(None, alias="rawSelector")

    requirements: list[V1FieldSelectorRequirement] | None = Field(
        None, alias="requirements"
    )
