from pydantic import BaseModel, Field

from .v1_stateful_set_condition import V1StatefulSetCondition


class V1StatefulSetStatus(BaseModel):
    available_replicas: int | None = Field(None, alias="availableReplicas")

    collision_count: int | None = Field(None, alias="collisionCount")

    conditions: list[V1StatefulSetCondition] | None = Field(None, alias="conditions")

    current_replicas: int | None = Field(None, alias="currentReplicas")

    current_revision: str | None = Field(None, alias="currentRevision")

    observed_generation: int | None = Field(None, alias="observedGeneration")

    ready_replicas: int | None = Field(None, alias="readyReplicas")

    replicas: int | None = Field(None, alias="replicas")

    update_revision: str | None = Field(None, alias="updateRevision")

    updated_replicas: int | None = Field(None, alias="updatedReplicas")
