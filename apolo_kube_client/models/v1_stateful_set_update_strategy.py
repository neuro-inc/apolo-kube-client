from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_rolling_update_stateful_set_strategy import V1RollingUpdateStatefulSetStrategy

__all__ = ("V1StatefulSetUpdateStrategy",)


class V1StatefulSetUpdateStrategy(BaseModel):
    rolling_update: V1RollingUpdateStatefulSetStrategy | None = Field(
        None, alias="rollingUpdate"
    )

    type: str | None = Field(None, alias="type")
