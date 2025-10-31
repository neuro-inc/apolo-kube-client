from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_custom_resource_subresource_scale import V1CustomResourceSubresourceScale
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1CustomResourceSubresources",)


class V1CustomResourceSubresources(BaseModel):
    """CustomResourceSubresources defines the status and scale subresources for CustomResources."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceSubresources"
    )

    scale: Annotated[
        V1CustomResourceSubresourceScale | None,
        Field(
            description="""scale indicates the custom resource should serve a `/scale` subresource that returns an `autoscaling/v1` Scale object.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        JsonType,
        Field(
            description="""status indicates the custom resource should serve a `/status` subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the `status` stanza of the object. 2. requests to the custom resource `/status` subresource ignore changes to anything other than the `status` stanza of the object.""",
            exclude_if=lambda v: v == {},
        ),
    ] = {}
