from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_custom_resource_column_definition import V1CustomResourceColumnDefinition
from .v1_custom_resource_subresources import V1CustomResourceSubresources
from .v1_custom_resource_validation import V1CustomResourceValidation
from .v1_selectable_field import V1SelectableField
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CustomResourceDefinitionVersion",)


class V1CustomResourceDefinitionVersion(BaseModel):
    additional_printer_columns: Annotated[
        list[V1CustomResourceColumnDefinition],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(
        default=[],
        serialization_alias="additionalPrinterColumns",
        validation_alias=AliasChoices(
            "additional_printer_columns", "additionalPrinterColumns"
        ),
        exclude_if=_exclude_if,
    )

    deprecated: bool | None = Field(default=None, exclude_if=_exclude_if)

    deprecation_warning: str | None = Field(
        default=None,
        serialization_alias="deprecationWarning",
        validation_alias=AliasChoices("deprecation_warning", "deprecationWarning"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    schema_: Annotated[
        V1CustomResourceValidation,
        BeforeValidator(_default_if_none(V1CustomResourceValidation)),
    ] = Field(
        default_factory=lambda: V1CustomResourceValidation(),
        serialization_alias="schema",
        validation_alias=AliasChoices("schema_", "schema"),
        exclude_if=_exclude_if,
    )

    selectable_fields: Annotated[
        list[V1SelectableField], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="selectableFields",
        validation_alias=AliasChoices("selectable_fields", "selectableFields"),
        exclude_if=_exclude_if,
    )

    served: bool | None = Field(default=None, exclude_if=_exclude_if)

    storage: bool | None = Field(default=None, exclude_if=_exclude_if)

    subresources: Annotated[
        V1CustomResourceSubresources,
        BeforeValidator(_default_if_none(V1CustomResourceSubresources)),
    ] = Field(
        default_factory=lambda: V1CustomResourceSubresources(), exclude_if=_exclude_if
    )
