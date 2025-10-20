from pydantic import AliasChoices, BaseModel, Field
from .v1_rolling_update_daemon_set import V1RollingUpdateDaemonSet

__all__ = ("V1DaemonSetUpdateStrategy",)


class V1DaemonSetUpdateStrategy(BaseModel):
    rolling_update: V1RollingUpdateDaemonSet = Field(
        default_factory=lambda: V1RollingUpdateDaemonSet(),
        serialization_alias="rollingUpdate",
        validation_alias=AliasChoices("rolling_update", "rollingUpdate"),
    )

    type: str | None = None
