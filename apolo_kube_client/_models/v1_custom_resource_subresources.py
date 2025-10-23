from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_custom_resource_subresource_scale import V1CustomResourceSubresourceScale
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CustomResourceSubresources",)


class V1CustomResourceSubresources(BaseModel):
    scale: Annotated[
        V1CustomResourceSubresourceScale,
        BeforeValidator(_default_if_none(V1CustomResourceSubresourceScale)),
    ] = Field(
        default_factory=lambda: V1CustomResourceSubresourceScale(),
        exclude_if=_exclude_if,
    )

    status: JsonType = Field(default={}, exclude_if=_exclude_if)
