from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v2_container_resource_metric_source import V2ContainerResourceMetricSource
from .v2_external_metric_source import V2ExternalMetricSource
from .v2_object_metric_source import V2ObjectMetricSource
from .v2_pods_metric_source import V2PodsMetricSource
from .v2_resource_metric_source import V2ResourceMetricSource
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2MetricSpec",)


class V2MetricSpec(BaseModel):
    container_resource: Annotated[
        V2ContainerResourceMetricSource,
        BeforeValidator(_default_if_none(V2ContainerResourceMetricSource)),
    ] = Field(
        default_factory=lambda: V2ContainerResourceMetricSource(),
        serialization_alias="containerResource",
        validation_alias=AliasChoices("container_resource", "containerResource"),
    )

    external: Annotated[
        V2ExternalMetricSource,
        BeforeValidator(_default_if_none(V2ExternalMetricSource)),
    ] = Field(default_factory=lambda: V2ExternalMetricSource())

    object: Annotated[
        V2ObjectMetricSource, BeforeValidator(_default_if_none(V2ObjectMetricSource))
    ] = Field(default_factory=lambda: V2ObjectMetricSource())

    pods: Annotated[
        V2PodsMetricSource, BeforeValidator(_default_if_none(V2PodsMetricSource))
    ] = Field(default_factory=lambda: V2PodsMetricSource())

    resource: Annotated[
        V2ResourceMetricSource,
        BeforeValidator(_default_if_none(V2ResourceMetricSource)),
    ] = Field(default_factory=lambda: V2ResourceMetricSource())

    type: str | None = None
