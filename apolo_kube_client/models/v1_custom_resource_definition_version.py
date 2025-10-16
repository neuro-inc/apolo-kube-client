from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_custom_resource_column_definition import V1CustomResourceColumnDefinition
from .v1_custom_resource_subresources import V1CustomResourceSubresources
from .v1_custom_resource_validation import V1CustomResourceValidation
from .v1_selectable_field import V1SelectableField

__all__ = ("V1CustomResourceDefinitionVersion",)


class V1CustomResourceDefinitionVersion(BaseModel):
    additional_printer_columns: list[V1CustomResourceColumnDefinition] = Field(
        default_factory=lambda: [], alias="additionalPrinterColumns"
    )

    deprecated: bool | None = Field(default_factory=lambda: None, alias="deprecated")

    deprecation_warning: str | None = Field(
        default_factory=lambda: None, alias="deprecationWarning"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")

    schema_: V1CustomResourceValidation = Field(
        default_factory=lambda: V1CustomResourceValidation(), alias="schema"
    )

    selectable_fields: list[V1SelectableField] = Field(
        default_factory=lambda: [], alias="selectableFields"
    )

    served: bool | None = Field(default_factory=lambda: None, alias="served")

    storage: bool | None = Field(default_factory=lambda: None, alias="storage")

    subresources: V1CustomResourceSubresources = Field(
        default_factory=lambda: V1CustomResourceSubresources(), alias="subresources"
    )
