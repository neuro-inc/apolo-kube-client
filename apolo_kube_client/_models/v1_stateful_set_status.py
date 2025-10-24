from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_stateful_set_condition import V1StatefulSetCondition
from pydantic import BeforeValidator

__all__ = ("V1StatefulSetStatus",)


class V1StatefulSetStatus(BaseModel):
    """StatefulSetStatus represents the current state of a StatefulSet."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.StatefulSetStatus"

    available_replicas: Annotated[
        int | None,
        Field(
            alias="availableReplicas",
            description="""Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    collision_count: Annotated[
        int | None,
        Field(
            alias="collisionCount",
            description="""collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    conditions: Annotated[
        list[V1StatefulSetCondition],
        Field(
            description="""Represents the latest available observations of a statefulset's current state.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    current_replicas: Annotated[
        int | None,
        Field(
            alias="currentReplicas",
            description="""currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    current_revision: Annotated[
        str | None,
        Field(
            alias="currentRevision",
            description="""currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    ready_replicas: Annotated[
        int | None,
        Field(
            alias="readyReplicas",
            description="""readyReplicas is the number of pods created for this StatefulSet with a Ready Condition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    replicas: Annotated[
        int,
        Field(
            description="""replicas is the number of Pods created by the StatefulSet controller."""
        ),
    ]

    update_revision: Annotated[
        str | None,
        Field(
            alias="updateRevision",
            description="""updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    updated_replicas: Annotated[
        int | None,
        Field(
            alias="updatedReplicas",
            description="""updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
