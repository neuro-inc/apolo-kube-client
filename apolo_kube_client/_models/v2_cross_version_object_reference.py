from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V2CrossVersionObjectReference",)


class V2CrossVersionObjectReference(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)
