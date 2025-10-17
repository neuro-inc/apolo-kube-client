from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_key_to_path import V1KeyToPath

__all__ = ("V1ConfigMapVolumeSource",)


class V1ConfigMapVolumeSource(BaseModel):
    default_mode: int | None = Field(
        default=None,
        serialization_alias="defaultMode",
        validation_alias=AliasChoices("default_mode", "defaultMode"),
    )

    items: list[V1KeyToPath] = Field(default=[])

    name: str | None = Field(default=None)

    optional: bool | None = Field(default=None)
