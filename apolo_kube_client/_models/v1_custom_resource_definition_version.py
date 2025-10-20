from pydantic import AliasChoices, BaseModel, Field
from .v1_custom_resource_column_definition import V1CustomResourceColumnDefinition
from .v1_custom_resource_subresources import V1CustomResourceSubresources
from .v1_custom_resource_validation import V1CustomResourceValidation
from .v1_selectable_field import V1SelectableField

__all__ = ("V1CustomResourceDefinitionVersion",)


class V1CustomResourceDefinitionVersion(BaseModel):
    additional_printer_columns: list[V1CustomResourceColumnDefinition] = Field(
        default=[],
        serialization_alias="additionalPrinterColumns",
        validation_alias=AliasChoices(
            "additional_printer_columns", "additionalPrinterColumns"
        ),
    )

    deprecated: bool | None = None

    deprecation_warning: str | None = Field(
        default=None,
        serialization_alias="deprecationWarning",
        validation_alias=AliasChoices("deprecation_warning", "deprecationWarning"),
    )

    name: str | None = None

    schema_: V1CustomResourceValidation = Field(
        default_factory=lambda: V1CustomResourceValidation(),
        serialization_alias="schema",
        validation_alias=AliasChoices("schema_", "schema"),
    )

    selectable_fields: list[V1SelectableField] = Field(
        default=[],
        serialization_alias="selectableFields",
        validation_alias=AliasChoices("selectable_fields", "selectableFields"),
    )

    served: bool | None = None

    storage: bool | None = None

    subresources: V1CustomResourceSubresources = Field(
        default_factory=lambda: V1CustomResourceSubresources()
    )
