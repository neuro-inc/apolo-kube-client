from pydantic import AliasChoices, BaseModel, Field
from .v1_downward_api_volume_file import V1DownwardAPIVolumeFile

__all__ = ("V1DownwardAPIVolumeSource",)


class V1DownwardAPIVolumeSource(BaseModel):
    default_mode: int | None = Field(
        default=None,
        serialization_alias="defaultMode",
        validation_alias=AliasChoices("default_mode", "defaultMode"),
    )

    items: list[V1DownwardAPIVolumeFile] = []
