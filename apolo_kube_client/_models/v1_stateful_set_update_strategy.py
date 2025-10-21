from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_rolling_update_stateful_set_strategy import V1RollingUpdateStatefulSetStrategy
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1StatefulSetUpdateStrategy",)


class V1StatefulSetUpdateStrategy(BaseModel):
    rolling_update: Annotated[
        V1RollingUpdateStatefulSetStrategy,
        BeforeValidator(_default_if_none(V1RollingUpdateStatefulSetStrategy)),
    ] = Field(
        default_factory=lambda: V1RollingUpdateStatefulSetStrategy(),
        serialization_alias="rollingUpdate",
        validation_alias=AliasChoices("rolling_update", "rollingUpdate"),
    )

    type: str | None = None
