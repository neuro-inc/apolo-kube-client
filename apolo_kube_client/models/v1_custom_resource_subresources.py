from pydantic import BaseModel, Field

from .object import object
from .v1_custom_resource_subresource_scale import V1CustomResourceSubresourceScale


class V1CustomResourceSubresources(BaseModel):
    scale: V1CustomResourceSubresourceScale | None = Field(None, alias="scale")

    status: object | None = Field(None, alias="status")
