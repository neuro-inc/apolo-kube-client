from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V2MetricTarget",)


class V2MetricTarget(BaseModel):
    """MetricTarget defines the target value, average value, or average utilization of a specific metric"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v2.MetricTarget"

    average_utilization: Annotated[
        int | None,
        Field(
            alias="averageUtilization",
            description="""averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    average_value: Annotated[
        str | None,
        Field(
            alias="averageValue",
            description="""averageValue is the target value of the average of the metric across all relevant pods (as a quantity)""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    type: Annotated[
        str,
        Field(
            description="""type represents whether the metric type is Utilization, Value, or AverageValue"""
        ),
    ]

    value: Annotated[
        str | None,
        Field(
            description="""value is the target value of the metric (as a quantity).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
