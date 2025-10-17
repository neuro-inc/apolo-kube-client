from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_field_selector_attributes import V1FieldSelectorAttributes
from .v1_label_selector_attributes import V1LabelSelectorAttributes

__all__ = ("V1ResourceAttributes",)


class V1ResourceAttributes(BaseModel):
    field_selector: V1FieldSelectorAttributes = Field(
        default_factory=lambda: V1FieldSelectorAttributes(),
        serialization_alias="fieldSelector",
        validation_alias=AliasChoices("field_selector", "fieldSelector"),
    )

    group: str | None = Field(default=None)

    label_selector: V1LabelSelectorAttributes = Field(
        default_factory=lambda: V1LabelSelectorAttributes(),
        serialization_alias="labelSelector",
        validation_alias=AliasChoices("label_selector", "labelSelector"),
    )

    name: str | None = Field(default=None)

    namespace: str | None = Field(default=None)

    resource: str | None = Field(default=None)

    subresource: str | None = Field(default=None)

    verb: str | None = Field(default=None)

    version: str | None = Field(default=None)
