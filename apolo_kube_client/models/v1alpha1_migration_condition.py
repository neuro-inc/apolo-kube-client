from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1alpha1MigrationCondition",)


class V1alpha1MigrationCondition(BaseModel):
    last_update_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastUpdateTime"
    )

    message: str | None = Field(default_factory=lambda: None)

    reason: str | None = Field(default_factory=lambda: None)

    status: str | None = Field(default_factory=lambda: None)

    type: str | None = Field(default_factory=lambda: None)
