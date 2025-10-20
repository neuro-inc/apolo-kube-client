from pydantic import AliasChoices, BaseModel, Field
from .v1_key_to_path import V1KeyToPath

__all__ = ("V1ConfigMapVolumeSource",)


class V1ConfigMapVolumeSource(BaseModel):
    default_mode: int | None = Field(
        default=None,
        serialization_alias="defaultMode",
        validation_alias=AliasChoices("default_mode", "defaultMode"),
    )

    items: list[V1KeyToPath] = []

    name: str | None = None

    optional: bool | None = None
