from pydantic import Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_pod_spec import V1PodSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodTemplateSpec",)


class V1PodTemplateSpec(ResourceModel):
    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[V1PodSpec, BeforeValidator(_default_if_none(V1PodSpec))] = Field(
        default_factory=lambda: V1PodSpec()
    )
