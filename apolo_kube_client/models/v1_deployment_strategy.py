from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_rolling_update_deployment import V1RollingUpdateDeployment

__all__ = ("V1DeploymentStrategy",)


class V1DeploymentStrategy(BaseModel):
    rolling_update: V1RollingUpdateDeployment = Field(
        default_factory=lambda: V1RollingUpdateDeployment(), alias="rollingUpdate"
    )

    type: str | None = Field(default_factory=lambda: None)
