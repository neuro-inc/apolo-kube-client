from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget

__all__ = ("V2ObjectMetricSource",)


class V2ObjectMetricSource(BaseModel):
    """ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object)."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.ObjectMetricSource"
    )

    described_object: Annotated[
        V2CrossVersionObjectReference,
        Field(
            alias="describedObject",
            description="""describedObject specifies the descriptions of a object,such as kind,name apiVersion""",
        ),
    ]

    metric: Annotated[
        V2MetricIdentifier,
        Field(
            description="""metric identifies the target metric by name and selector"""
        ),
    ]

    target: Annotated[
        V2MetricTarget,
        Field(description="""target specifies the target value for the given metric"""),
    ]
