from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_rolling_update_deployment import V1RollingUpdateDeployment
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeploymentStrategy",)


class V1DeploymentStrategy(BaseModel):
    rolling_update: Annotated[
        V1RollingUpdateDeployment,
        BeforeValidator(_default_if_none(V1RollingUpdateDeployment)),
    ] = Field(
        default_factory=lambda: V1RollingUpdateDeployment(),
        serialization_alias="rollingUpdate",
        validation_alias=AliasChoices("rolling_update", "rollingUpdate"),
        exclude_if=_exclude_if,
    )

    type: str | None = Field(default=None, exclude_if=_exclude_if)
