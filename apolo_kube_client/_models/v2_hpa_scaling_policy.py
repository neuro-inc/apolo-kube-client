from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V2HPAScalingPolicy",)


class V2HPAScalingPolicy(BaseModel):
    """HPAScalingPolicy is a single policy which must hold true for a specified past interval."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v2.HPAScalingPolicy"

    period_seconds: Annotated[
        int,
        Field(
            alias="periodSeconds",
            description="""periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).""",
        ),
    ]

    type: Annotated[
        str, Field(description="""type is used to specify the scaling policy.""")
    ]

    value: Annotated[
        int,
        Field(
            description="""value contains the amount of change which is permitted by the policy. It must be greater than zero"""
        ),
    ]
