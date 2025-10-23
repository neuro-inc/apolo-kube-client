from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1GroupVersionForDiscovery",)


class V1GroupVersionForDiscovery(BaseModel):
    group_version: str | None = Field(
        default=None,
        serialization_alias="groupVersion",
        validation_alias=AliasChoices("group_version", "groupVersion"),
        exclude_if=_exclude_if,
    )

    version: str | None = Field(default=None, exclude_if=_exclude_if)
