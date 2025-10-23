from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1NFSVolumeSource",)


class V1NFSVolumeSource(BaseModel):
    path: str | None = Field(default=None, exclude_if=_exclude_if)

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

    server: str | None = Field(default=None, exclude_if=_exclude_if)
