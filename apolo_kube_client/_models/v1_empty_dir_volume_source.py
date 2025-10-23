from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1EmptyDirVolumeSource",)


class V1EmptyDirVolumeSource(BaseModel):
    medium: str | None = Field(default=None, exclude_if=_exclude_if)

    size_limit: str | None = Field(
        default=None,
        serialization_alias="sizeLimit",
        validation_alias=AliasChoices("size_limit", "sizeLimit"),
        exclude_if=_exclude_if,
    )
