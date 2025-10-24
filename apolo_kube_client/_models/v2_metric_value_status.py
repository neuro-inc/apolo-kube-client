from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V2MetricValueStatus",)


class V2MetricValueStatus(BaseModel):
    """MetricValueStatus holds the current value for a metric"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v2.MetricValueStatus"

    average_utilization: Annotated[
        int | None,
        Field(
            alias="averageUtilization",
            description="""currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    average_value: Annotated[
        str | None,
        Field(
            alias="averageValue",
            description="""averageValue is the current value of the average of the metric across all relevant pods (as a quantity)""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    value: Annotated[
        str | None,
        Field(
            description="""value is the current value of the metric (as a quantity).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
