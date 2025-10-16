from __future__ import annotations

from pydantic import BaseModel, Field

from apolo_kube_client._typedefs import JsonType

from .v1_custom_resource_subresource_scale import V1CustomResourceSubresourceScale

__all__ = ("V1CustomResourceSubresources",)


class V1CustomResourceSubresources(BaseModel):
    scale: V1CustomResourceSubresourceScale | None = Field(None, alias="scale")

    status: JsonType | None = Field(None, alias="status")
