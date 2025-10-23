from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1LocalVolumeSource",)


class V1LocalVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
        exclude_if=_exclude_if,
    )

    path: str | None = Field(default=None, exclude_if=_exclude_if)
