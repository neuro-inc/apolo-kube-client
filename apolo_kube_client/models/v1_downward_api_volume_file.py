from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector

__all__ = ("V1DownwardAPIVolumeFile",)


class V1DownwardAPIVolumeFile(BaseModel):
    field_ref: V1ObjectFieldSelector = Field(
        default_factory=lambda: V1ObjectFieldSelector(), alias="fieldRef"
    )

    mode: int | None = Field(default_factory=lambda: None)

    path: str | None = Field(default_factory=lambda: None)

    resource_field_ref: V1ResourceFieldSelector = Field(
        default_factory=lambda: V1ResourceFieldSelector(), alias="resourceFieldRef"
    )
