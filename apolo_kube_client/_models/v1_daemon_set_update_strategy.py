from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_rolling_update_daemon_set import V1RollingUpdateDaemonSet
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DaemonSetUpdateStrategy",)


class V1DaemonSetUpdateStrategy(BaseModel):
    rolling_update: Annotated[
        V1RollingUpdateDaemonSet,
        BeforeValidator(_default_if_none(V1RollingUpdateDaemonSet)),
    ] = Field(
        default_factory=lambda: V1RollingUpdateDaemonSet(),
        serialization_alias="rollingUpdate",
        validation_alias=AliasChoices("rolling_update", "rollingUpdate"),
    )

    type: str | None = None
