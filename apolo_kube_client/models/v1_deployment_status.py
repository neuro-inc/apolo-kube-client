from pydantic import BaseModel, Field

from .v1_deployment_condition import V1DeploymentCondition


class V1DeploymentStatus(BaseModel):
    available_replicas: int | None = Field(None, alias="availableReplicas")

    collision_count: int | None = Field(None, alias="collisionCount")

    conditions: list[V1DeploymentCondition] | None = Field(None, alias="conditions")

    observed_generation: int | None = Field(None, alias="observedGeneration")

    ready_replicas: int | None = Field(None, alias="readyReplicas")

    replicas: int | None = Field(None, alias="replicas")

    unavailable_replicas: int | None = Field(None, alias="unavailableReplicas")

    updated_replicas: int | None = Field(None, alias="updatedReplicas")
