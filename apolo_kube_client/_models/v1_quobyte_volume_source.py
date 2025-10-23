from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1QuobyteVolumeSource",)


class V1QuobyteVolumeSource(BaseModel):
    group: str | None = Field(default=None, exclude_if=_exclude_if)

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

    registry: str | None = Field(default=None, exclude_if=_exclude_if)

    tenant: str | None = Field(default=None, exclude_if=_exclude_if)

    user: str | None = Field(default=None, exclude_if=_exclude_if)

    volume: str | None = Field(default=None, exclude_if=_exclude_if)
