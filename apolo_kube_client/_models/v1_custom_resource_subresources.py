from pydantic import BaseModel, Field
from .v1_custom_resource_subresource_scale import V1CustomResourceSubresourceScale
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1CustomResourceSubresources",)


class V1CustomResourceSubresources(BaseModel):
    scale: V1CustomResourceSubresourceScale = Field(
        default_factory=lambda: V1CustomResourceSubresourceScale()
    )

    status: JsonType = {}
