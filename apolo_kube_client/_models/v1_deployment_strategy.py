from pydantic import AliasChoices, BaseModel, Field
from .v1_rolling_update_deployment import V1RollingUpdateDeployment

__all__ = ("V1DeploymentStrategy",)


class V1DeploymentStrategy(BaseModel):
    rolling_update: V1RollingUpdateDeployment = Field(
        default_factory=lambda: V1RollingUpdateDeployment(),
        serialization_alias="rollingUpdate",
        validation_alias=AliasChoices("rolling_update", "rollingUpdate"),
    )

    type: str | None = None
