from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_deployment_condition import V1DeploymentCondition
from pydantic import BeforeValidator

__all__ = ("V1DeploymentStatus",)


class V1DeploymentStatus(BaseModel):
    """DeploymentStatus is the most recently observed status of the Deployment."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.DeploymentStatus"

    available_replicas: Annotated[
        int | None,
        Field(
            alias="availableReplicas",
            description="""Total number of available non-terminating pods (ready for at least minReadySeconds) targeted by this deployment.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    collision_count: Annotated[
        int | None,
        Field(
            alias="collisionCount",
            description="""Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    conditions: Annotated[
        list[V1DeploymentCondition],
        Field(
            description="""Represents the latest available observations of a deployment's current state.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""The generation observed by the deployment controller.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    ready_replicas: Annotated[
        int | None,
        Field(
            alias="readyReplicas",
            description="""Total number of non-terminating pods targeted by this Deployment with a Ready Condition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    replicas: Annotated[
        int | None,
        Field(
            description="""Total number of non-terminating pods targeted by this deployment (their labels match the selector).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    terminating_replicas: Annotated[
        int | None,
        Field(
            alias="terminatingReplicas",
            description="""Total number of terminating pods targeted by this deployment. Terminating pods have a non-null .metadata.deletionTimestamp and have not yet reached the Failed or Succeeded .status.phase.

This is an alpha field. Enable DeploymentReplicaSetTerminatingReplicas to be able to use this field.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    unavailable_replicas: Annotated[
        int | None,
        Field(
            alias="unavailableReplicas",
            description="""Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    updated_replicas: Annotated[
        int | None,
        Field(
            alias="updatedReplicas",
            description="""Total number of non-terminating pods targeted by this deployment that have the desired template spec.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
