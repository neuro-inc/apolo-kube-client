from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_rolling_update_deployment import V1RollingUpdateDeployment
from pydantic import BeforeValidator

__all__ = ("V1DeploymentStrategy",)


class V1DeploymentStrategy(BaseModel):
    """DeploymentStrategy describes how to replace existing pods with new ones."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.DeploymentStrategy"

    rolling_update: Annotated[
        V1RollingUpdateDeployment,
        Field(
            alias="rollingUpdate",
            description="""Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1RollingUpdateDeployment)),
    ] = V1RollingUpdateDeployment()

    type: Annotated[
        str | None,
        Field(
            description="""Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
