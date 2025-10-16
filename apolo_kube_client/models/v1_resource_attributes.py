from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_field_selector_attributes import V1FieldSelectorAttributes
from .v1_label_selector_attributes import V1LabelSelectorAttributes

__all__ = ("V1ResourceAttributes",)


class V1ResourceAttributes(BaseModel):
    field_selector: V1FieldSelectorAttributes = Field(
        default_factory=lambda: V1FieldSelectorAttributes(), alias="fieldSelector"
    )

    group: str | None = Field(default_factory=lambda: None, alias="group")

    label_selector: V1LabelSelectorAttributes = Field(
        default_factory=lambda: V1LabelSelectorAttributes(), alias="labelSelector"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")

    namespace: str | None = Field(default_factory=lambda: None, alias="namespace")

    resource: str | None = Field(default_factory=lambda: None, alias="resource")

    subresource: str | None = Field(default_factory=lambda: None, alias="subresource")

    verb: str | None = Field(default_factory=lambda: None, alias="verb")

    version: str | None = Field(default_factory=lambda: None, alias="version")
