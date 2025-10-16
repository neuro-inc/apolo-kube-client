from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_rolling_update_stateful_set_strategy import V1RollingUpdateStatefulSetStrategy

__all__ = ("V1StatefulSetUpdateStrategy",)


class V1StatefulSetUpdateStrategy(BaseModel):
    rolling_update: V1RollingUpdateStatefulSetStrategy = Field(
        default_factory=lambda: V1RollingUpdateStatefulSetStrategy(),
        alias="rollingUpdate",
    )

    type: str | None = Field(default_factory=lambda: None, alias="type")
