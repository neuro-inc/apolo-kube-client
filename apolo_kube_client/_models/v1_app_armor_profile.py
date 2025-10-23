from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1AppArmorProfile",)


class V1AppArmorProfile(BaseModel):
    localhost_profile: str | None = Field(
        default=None,
        serialization_alias="localhostProfile",
        validation_alias=AliasChoices("localhost_profile", "localhostProfile"),
        exclude_if=_exclude_if,
    )

    type: str | None = Field(default=None, exclude_if=_exclude_if)
