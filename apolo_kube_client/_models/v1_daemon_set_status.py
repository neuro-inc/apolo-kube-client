from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_daemon_set_condition import V1DaemonSetCondition
from pydantic import BeforeValidator

__all__ = ("V1DaemonSetStatus",)


class V1DaemonSetStatus(BaseModel):
    """DaemonSetStatus represents the current status of a daemon set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.DaemonSetStatus"

    collision_count: Annotated[
        int | None,
        Field(
            alias="collisionCount",
            description="""Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    conditions: Annotated[
        list[V1DaemonSetCondition],
        Field(
            description="""Represents the latest available observations of a DaemonSet's current state.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    current_number_scheduled: Annotated[
        int,
        Field(
            alias="currentNumberScheduled",
            description="""The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/""",
        ),
    ]

    desired_number_scheduled: Annotated[
        int,
        Field(
            alias="desiredNumberScheduled",
            description="""The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/""",
        ),
    ]

    number_available: Annotated[
        int | None,
        Field(
            alias="numberAvailable",
            description="""The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    number_misscheduled: Annotated[
        int,
        Field(
            alias="numberMisscheduled",
            description="""The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/""",
        ),
    ]

    number_ready: Annotated[
        int,
        Field(
            alias="numberReady",
            description="""numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition.""",
        ),
    ]

    number_unavailable: Annotated[
        int | None,
        Field(
            alias="numberUnavailable",
            description="""The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""The most recent generation observed by the daemon set controller.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    updated_number_scheduled: Annotated[
        int | None,
        Field(
            alias="updatedNumberScheduled",
            description="""The total number of nodes that are running updated daemon pod""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
