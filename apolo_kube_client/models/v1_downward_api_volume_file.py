from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector

__all__ = ("V1DownwardAPIVolumeFile",)


class V1DownwardAPIVolumeFile(BaseModel):
    field_ref: V1ObjectFieldSelector = Field(
        default_factory=lambda: V1ObjectFieldSelector(),
        serialization_alias="fieldRef",
        validation_alias=AliasChoices("field_ref", "fieldRef"),
    )

    mode: int | None = Field(default=None)

    path: str | None = Field(default=None)

    resource_field_ref: V1ResourceFieldSelector = Field(
        default_factory=lambda: V1ResourceFieldSelector(),
        serialization_alias="resourceFieldRef",
        validation_alias=AliasChoices("resource_field_ref", "resourceFieldRef"),
    )
