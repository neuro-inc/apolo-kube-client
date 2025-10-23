from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1Preconditions",)


class V1Preconditions(BaseModel):
    resource_version: str | None = Field(
        default=None,
        serialization_alias="resourceVersion",
        validation_alias=AliasChoices("resource_version", "resourceVersion"),
        exclude_if=_exclude_if,
    )

    uid: str | None = Field(default=None, exclude_if=_exclude_if)
