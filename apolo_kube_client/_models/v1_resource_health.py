from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ResourceHealth",)


class V1ResourceHealth(BaseModel):
    health: str | None = Field(default=None, exclude_if=_exclude_if)

    resource_id: str | None = Field(
        default=None,
        serialization_alias="resourceID",
        validation_alias=AliasChoices("resource_id", "resourceID"),
        exclude_if=_exclude_if,
    )
