from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_rolling_update_stateful_set_strategy import V1RollingUpdateStatefulSetStrategy
from pydantic import BeforeValidator

__all__ = ("V1StatefulSetUpdateStrategy",)


class V1StatefulSetUpdateStrategy(BaseModel):
    """StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.apps.v1.StatefulSetUpdateStrategy"
    )

    rolling_update: Annotated[
        V1RollingUpdateStatefulSetStrategy,
        Field(
            alias="rollingUpdate",
            description="""RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1RollingUpdateStatefulSetStrategy)),
    ] = V1RollingUpdateStatefulSetStrategy()

    type: Annotated[
        str | None,
        Field(
            description="""Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
