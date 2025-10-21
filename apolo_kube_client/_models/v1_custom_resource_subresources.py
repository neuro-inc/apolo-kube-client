from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1_custom_resource_subresource_scale import V1CustomResourceSubresourceScale
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CustomResourceSubresources",)


class V1CustomResourceSubresources(BaseModel):
    scale: Annotated[
        V1CustomResourceSubresourceScale,
        BeforeValidator(_default_if_none(V1CustomResourceSubresourceScale)),
    ] = Field(default_factory=lambda: V1CustomResourceSubresourceScale())

    status: JsonType = {}
