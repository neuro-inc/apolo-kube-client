from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v2_metric_value_status import V2MetricValueStatus

__all__ = ("V2ResourceMetricStatus",)


class V2ResourceMetricStatus(BaseModel):
    """ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.ResourceMetricStatus"
    )

    current: Annotated[
        V2MetricValueStatus,
        Field(
            description="""current contains the current value for the given metric"""
        ),
    ]

    name: Annotated[
        str, Field(description="""name is the name of the resource in question.""")
    ]
