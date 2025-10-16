from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_rolling_update_daemon_set import V1RollingUpdateDaemonSet

__all__ = ("V1DaemonSetUpdateStrategy",)


class V1DaemonSetUpdateStrategy(BaseModel):
    rolling_update: V1RollingUpdateDaemonSet | None = Field(None, alias="rollingUpdate")

    type: str | None = Field(None, alias="type")
