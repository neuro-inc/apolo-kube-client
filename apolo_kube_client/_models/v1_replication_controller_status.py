from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_replication_controller_condition import V1ReplicationControllerCondition
from pydantic import BeforeValidator

__all__ = ("V1ReplicationControllerStatus",)


class V1ReplicationControllerStatus(BaseModel):
    """ReplicationControllerStatus represents the current status of a replication controller."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.ReplicationControllerStatus"
    )

    available_replicas: Annotated[
        int | None,
        Field(
            alias="availableReplicas",
            description="""The number of available replicas (ready for at least minReadySeconds) for this replication controller.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    conditions: Annotated[
        list[V1ReplicationControllerCondition],
        Field(
            description="""Represents the latest available observations of a replication controller's current state.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    fully_labeled_replicas: Annotated[
        int | None,
        Field(
            alias="fullyLabeledReplicas",
            description="""The number of pods that have labels matching the labels of the pod template of the replication controller.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""ObservedGeneration reflects the generation of the most recently observed replication controller.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    ready_replicas: Annotated[
        int | None,
        Field(
            alias="readyReplicas",
            description="""The number of ready replicas for this replication controller.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    replicas: Annotated[
        int,
        Field(
            description="""Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller"""
        ),
    ]
