from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1alpha1MigrationCondition",)


class V1alpha1MigrationCondition(BaseModel):
    last_update_time: datetime | None = Field(
        default=None,
        serialization_alias="lastUpdateTime",
        validation_alias=AliasChoices("last_update_time", "lastUpdateTime"),
        exclude_if=_exclude_if,
    )

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    reason: str | None = Field(default=None, exclude_if=_exclude_if)

    status: str | None = Field(default=None, exclude_if=_exclude_if)

    type: str | None = Field(default=None, exclude_if=_exclude_if)
