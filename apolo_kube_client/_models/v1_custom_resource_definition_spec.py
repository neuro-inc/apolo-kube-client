from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_custom_resource_conversion import V1CustomResourceConversion
from .v1_custom_resource_definition_names import V1CustomResourceDefinitionNames
from .v1_custom_resource_definition_version import V1CustomResourceDefinitionVersion
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CustomResourceDefinitionSpec",)


class V1CustomResourceDefinitionSpec(BaseModel):
    conversion: Annotated[
        V1CustomResourceConversion,
        BeforeValidator(_default_if_none(V1CustomResourceConversion)),
    ] = Field(
        default_factory=lambda: V1CustomResourceConversion(), exclude_if=_exclude_if
    )

    group: str | None = Field(default=None, exclude_if=_exclude_if)

    names: Annotated[
        V1CustomResourceDefinitionNames,
        BeforeValidator(_default_if_none(V1CustomResourceDefinitionNames)),
    ] = Field(
        default_factory=lambda: V1CustomResourceDefinitionNames(),
        exclude_if=_exclude_if,
    )

    preserve_unknown_fields: bool | None = Field(
        default=None,
        serialization_alias="preserveUnknownFields",
        validation_alias=AliasChoices(
            "preserve_unknown_fields", "preserveUnknownFields"
        ),
        exclude_if=_exclude_if,
    )

    scope: str | None = Field(default=None, exclude_if=_exclude_if)

    versions: Annotated[
        list[V1CustomResourceDefinitionVersion],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)
