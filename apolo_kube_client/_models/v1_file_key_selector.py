from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1FileKeySelector",)


class V1FileKeySelector(BaseModel):
    key: str | None = Field(default=None, exclude_if=_exclude_if)

    optional: bool | None = Field(default=None, exclude_if=_exclude_if)

    path: str | None = Field(default=None, exclude_if=_exclude_if)

    volume_name: str | None = Field(
        default=None,
        serialization_alias="volumeName",
        validation_alias=AliasChoices("volume_name", "volumeName"),
        exclude_if=_exclude_if,
    )
