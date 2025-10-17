from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1alpha1MigrationCondition",)


class V1alpha1MigrationCondition(BaseModel):
    last_update_time: datetime | None = Field(
        default=None,
        serialization_alias="lastUpdateTime",
        validation_alias=AliasChoices("last_update_time", "lastUpdateTime"),
    )

    message: str | None = None

    reason: str | None = None

    status: str | None = None

    type: str | None = None
