from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1PodFailurePolicyOnPodConditionsPattern",)


class V1PodFailurePolicyOnPodConditionsPattern(BaseModel):
    """PodFailurePolicyOnPodConditionsPattern describes a pattern for matching an actual pod condition type."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.batch.v1.PodFailurePolicyOnPodConditionsPattern"
    )

    status: Annotated[
        str,
        Field(
            description="""Specifies the required Pod condition status. To match a pod condition it is required that the specified status equals the pod condition status. Defaults to True."""
        ),
    ]

    type: Annotated[
        str,
        Field(
            description="""Specifies the required Pod condition type. To match a pod condition it is required that specified type equals the pod condition type."""
        ),
    ]
