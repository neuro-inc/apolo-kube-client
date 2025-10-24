from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_replica_set_condition import V1ReplicaSetCondition
from pydantic import BeforeValidator

__all__ = ("V1ReplicaSetStatus",)


class V1ReplicaSetStatus(BaseModel):
    """ReplicaSetStatus represents the current status of a ReplicaSet."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.ReplicaSetStatus"

    available_replicas: Annotated[
        int | None,
        Field(
            alias="availableReplicas",
            description="""The number of available non-terminating pods (ready for at least minReadySeconds) for this replica set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    conditions: Annotated[
        list[V1ReplicaSetCondition],
        Field(
            description="""Represents the latest available observations of a replica set's current state.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    fully_labeled_replicas: Annotated[
        int | None,
        Field(
            alias="fullyLabeledReplicas",
            description="""The number of non-terminating pods that have labels matching the labels of the pod template of the replicaset.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""ObservedGeneration reflects the generation of the most recently observed ReplicaSet.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    ready_replicas: Annotated[
        int | None,
        Field(
            alias="readyReplicas",
            description="""The number of non-terminating pods targeted by this ReplicaSet with a Ready Condition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    replicas: Annotated[
        int,
        Field(
            description="""Replicas is the most recently observed number of non-terminating pods. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset"""
        ),
    ]

    terminating_replicas: Annotated[
        int | None,
        Field(
            alias="terminatingReplicas",
            description="""The number of terminating pods for this replica set. Terminating pods have a non-null .metadata.deletionTimestamp and have not yet reached the Failed or Succeeded .status.phase.

This is an alpha field. Enable DeploymentReplicaSetTerminatingReplicas to be able to use this field.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
