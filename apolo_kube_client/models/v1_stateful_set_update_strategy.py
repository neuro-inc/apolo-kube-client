from pydantic import AliasChoices, BaseModel, Field
from .v1_rolling_update_stateful_set_strategy import V1RollingUpdateStatefulSetStrategy

__all__ = ("V1StatefulSetUpdateStrategy",)


class V1StatefulSetUpdateStrategy(BaseModel):
    rolling_update: V1RollingUpdateStatefulSetStrategy = Field(
        default_factory=lambda: V1RollingUpdateStatefulSetStrategy(),
        serialization_alias="rollingUpdate",
        validation_alias=AliasChoices("rolling_update", "rollingUpdate"),
    )

    type: str | None = None
