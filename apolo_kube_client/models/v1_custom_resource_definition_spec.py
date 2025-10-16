from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_custom_resource_conversion import V1CustomResourceConversion
from .v1_custom_resource_definition_names import V1CustomResourceDefinitionNames
from .v1_custom_resource_definition_version import V1CustomResourceDefinitionVersion

__all__ = ("V1CustomResourceDefinitionSpec",)


class V1CustomResourceDefinitionSpec(BaseModel):
    conversion: V1CustomResourceConversion | None = Field(None, alias="conversion")

    group: str | None = Field(None, alias="group")

    names: V1CustomResourceDefinitionNames | None = Field(None, alias="names")

    preserve_unknown_fields: bool | None = Field(None, alias="preserveUnknownFields")

    scope: str | None = Field(None, alias="scope")

    versions: list[V1CustomResourceDefinitionVersion] | None = Field(
        None, alias="versions"
    )
