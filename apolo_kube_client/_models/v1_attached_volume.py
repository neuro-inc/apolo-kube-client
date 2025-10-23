from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1AttachedVolume",)


class V1AttachedVolume(BaseModel):
    device_path: str | None = Field(
        default=None,
        serialization_alias="devicePath",
        validation_alias=AliasChoices("device_path", "devicePath"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)
