from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ContainerExtendedResourceRequest",)


class V1ContainerExtendedResourceRequest(BaseModel):
    """ContainerExtendedResourceRequest has the mapping of container name, extended resource name to the device request name."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

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
