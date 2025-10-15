from pydantic import BaseModel, Field

from .v1_rolling_update_deployment import V1RollingUpdateDeployment


class V1DeploymentStrategy(BaseModel):
    rolling_update: V1RollingUpdateDeployment | None = Field(
        None, alias="rollingUpdate"
    )

    type: str | None = Field(None, alias="type")
