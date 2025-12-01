from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget


__all__ = ("V2ExternalMetricSource",)


class V2ExternalMetricSource(BaseConfiguredModel):
    """ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes object (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster)."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.ExternalMetricSource"
    )

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
