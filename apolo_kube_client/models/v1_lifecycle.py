from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_lifecycle_handler import V1LifecycleHandler

__all__ = ("V1Lifecycle",)


class V1Lifecycle(BaseModel):
    post_start: V1LifecycleHandler = Field(
        default_factory=lambda: V1LifecycleHandler(), alias="postStart"
    )

    pre_stop: V1LifecycleHandler = Field(
        default_factory=lambda: V1LifecycleHandler(), alias="preStop"
    )

    stop_signal: str | None = Field(default_factory=lambda: None, alias="stopSignal")
