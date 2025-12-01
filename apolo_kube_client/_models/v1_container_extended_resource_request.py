from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1ContainerExtendedResourceRequest",)


class V1ContainerExtendedResourceRequest(BaseConfiguredModel):
    """ContainerExtendedResourceRequest has the mapping of container name, extended resource name to the device request name."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.ContainerExtendedResourceRequest"
    )

    container_name: Annotated[
        str,
        Field(
            alias="containerName",
            description="""The name of the container requesting resources.""",
        ),
    ]

    request_name: Annotated[
        str,
        Field(
            alias="requestName",
            description="""The name of the request in the special ResourceClaim which corresponds to the extended resource.""",
        ),
    ]

    resource_name: Annotated[
        str,
        Field(
            alias="resourceName",
            description="""The name of the extended resource in that container which gets backed by DRA.""",
        ),
    ]
