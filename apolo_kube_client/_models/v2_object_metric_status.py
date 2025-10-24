from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_value_status import V2MetricValueStatus

__all__ = ("V2ObjectMetricStatus",)


class V2ObjectMetricStatus(BaseModel):
    """ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object)."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.ObjectMetricStatus"
    )

    current: Annotated[
        V2MetricValueStatus,
        Field(
            description="""current contains the current value for the given metric"""
        ),
    ]

    described_object: Annotated[
        V2CrossVersionObjectReference,
        Field(
            alias="describedObject",
            description="""DescribedObject specifies the descriptions of a object,such as kind,name apiVersion""",
        ),
    ]

    metric: Annotated[
        V2MetricIdentifier,
        Field(
            description="""metric identifies the target metric by name and selector"""
        ),
    ]
