from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v2_metric_target import V2MetricTarget

__all__ = ("V2ResourceMetricSource",)


class V2ResourceMetricSource(BaseModel):
    """ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  The values will be averaged together before being compared to the target.  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.  Only one "target" type should be set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.ResourceMetricSource"
    )

    name: Annotated[
        str, Field(description="""name is the name of the resource in question.""")
    ]

    target: Annotated[
        V2MetricTarget,
        Field(description="""target specifies the target value for the given metric"""),
    ]
