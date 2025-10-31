from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v2_container_resource_metric_status import V2ContainerResourceMetricStatus
from .v2_external_metric_status import V2ExternalMetricStatus
from .v2_object_metric_status import V2ObjectMetricStatus
from .v2_pods_metric_status import V2PodsMetricStatus
from .v2_resource_metric_status import V2ResourceMetricStatus

__all__ = ("V2MetricStatus",)


class V2MetricStatus(BaseModel):
    """MetricStatus describes the last-read state of a single metric."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v2.MetricStatus"

    container_resource: Annotated[
        V2ContainerResourceMetricStatus | None,
        Field(
            alias="containerResource",
            description="""container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    external: Annotated[
        V2ExternalMetricStatus | None,
        Field(
            description="""external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    object: Annotated[
        V2ObjectMetricStatus | None,
        Field(
            description="""object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    pods: Annotated[
        V2PodsMetricStatus | None,
        Field(
            description="""pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource: Annotated[
        V2ResourceMetricStatus | None,
        Field(
            description="""resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    type: Annotated[
        str,
        Field(
            description="""type is the type of metric source.  It will be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each corresponds to a matching field in the object."""
        ),
    ]
