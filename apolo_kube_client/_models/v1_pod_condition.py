from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1PodCondition",)


class V1PodCondition(BaseModel):
    """PodCondition contains details for the current condition of this pod."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PodCondition"

    last_probe_time: Annotated[
        datetime | None,
        Field(
            alias="lastProbeTime",
            description="""Last time we probed the condition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    last_transition_time: Annotated[
        datetime | None,
        Field(
            alias="lastTransitionTime",
            description="""Last time the condition transitioned from one status to another.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""Human-readable message indicating details about last transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""If set, this represents the .metadata.generation that the pod condition was set based upon. This is an alpha field. Enable PodObservedGenerationTracking to be able to use this field.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""Unique, one-word, CamelCase reason for the condition's last transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        str,
        Field(
            description="""Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions"""
        ),
    ]

    type: Annotated[
        str,
        Field(
            description="""Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions"""
        ),
    ]
