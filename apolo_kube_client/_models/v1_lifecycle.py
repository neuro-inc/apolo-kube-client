from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_lifecycle_handler import V1LifecycleHandler
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Lifecycle",)


class V1Lifecycle(BaseModel):
    post_start: Annotated[
        V1LifecycleHandler, BeforeValidator(_default_if_none(V1LifecycleHandler))
    ] = Field(
        default_factory=lambda: V1LifecycleHandler(),
        serialization_alias="postStart",
        validation_alias=AliasChoices("post_start", "postStart"),
    )

    pre_stop: Annotated[
        V1LifecycleHandler, BeforeValidator(_default_if_none(V1LifecycleHandler))
    ] = Field(
        default_factory=lambda: V1LifecycleHandler(),
        serialization_alias="preStop",
        validation_alias=AliasChoices("pre_stop", "preStop"),
    )

    stop_signal: str | None = Field(
        default=None,
        serialization_alias="stopSignal",
        validation_alias=AliasChoices("stop_signal", "stopSignal"),
    )
