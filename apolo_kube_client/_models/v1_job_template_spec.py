from pydantic import Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_job_spec import V1JobSpec
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1JobTemplateSpec",)


class V1JobTemplateSpec(ResourceModel):
    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[V1JobSpec, BeforeValidator(_default_if_none(V1JobSpec))] = Field(
        default_factory=lambda: V1JobSpec()
    )
