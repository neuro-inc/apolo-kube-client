from pydantic import AliasChoices, BaseModel, Field
from .v1_key_to_path import V1KeyToPath

__all__ = ("V1SecretVolumeSource",)


class V1SecretVolumeSource(BaseModel):
    default_mode: int | None = Field(
        default=None,
        serialization_alias="defaultMode",
        validation_alias=AliasChoices("default_mode", "defaultMode"),
    )

    items: list[V1KeyToPath] = []

    optional: bool | None = None

    secret_name: str | None = Field(
        default=None,
        serialization_alias="secretName",
        validation_alias=AliasChoices("secret_name", "secretName"),
    )
