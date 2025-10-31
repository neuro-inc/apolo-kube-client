from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v2_container_resource_metric_source import V2ContainerResourceMetricSource
from .v2_external_metric_source import V2ExternalMetricSource
from .v2_object_metric_source import V2ObjectMetricSource
from .v2_pods_metric_source import V2PodsMetricSource
from .v2_resource_metric_source import V2ResourceMetricSource

__all__ = ("V2MetricSpec",)


class V2MetricSpec(BaseModel):
    """MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once)."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v2.MetricSpec"

    container_resource: Annotated[
        V2ContainerResourceMetricSource | None,
        Field(
            alias="containerResource",
            description="""containerResource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    external: Annotated[
        V2ExternalMetricSource | None,
        Field(
            description="""external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    object: Annotated[
        V2ObjectMetricSource | None,
        Field(
            description="""object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    pods: Annotated[
        V2PodsMetricSource | None,
        Field(
            description="""pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource: Annotated[
        V2ResourceMetricSource | None,
        Field(
            description="""resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    type: Annotated[
        str,
        Field(
            description="""type is the type of metric source.  It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object."""
        ),
    ]
