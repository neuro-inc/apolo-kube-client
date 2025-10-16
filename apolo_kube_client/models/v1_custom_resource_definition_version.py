from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_custom_resource_column_definition import V1CustomResourceColumnDefinition
from .v1_custom_resource_subresources import V1CustomResourceSubresources
from .v1_custom_resource_validation import V1CustomResourceValidation
from .v1_selectable_field import V1SelectableField

__all__ = ("V1CustomResourceDefinitionVersion",)


class V1CustomResourceDefinitionVersion(BaseModel):
    additional_printer_columns: list[V1CustomResourceColumnDefinition] | None = Field(
        None, alias="additionalPrinterColumns"
    )

    deprecated: bool | None = Field(None, alias="deprecated")

    deprecation_warning: str | None = Field(None, alias="deprecationWarning")

    name: str | None = Field(None, alias="name")

    _schema: V1CustomResourceValidation | None = Field(None, alias="schema")

    selectable_fields: list[V1SelectableField] | None = Field(
        None, alias="selectableFields"
    )

    served: bool | None = Field(None, alias="served")

    storage: bool | None = Field(None, alias="storage")

    subresources: V1CustomResourceSubresources | None = Field(
        None, alias="subresources"
    )
