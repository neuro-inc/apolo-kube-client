from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ContainerExtendedResourceRequest",)


class V1ContainerExtendedResourceRequest(BaseModel):
    container_name: str | None = Field(
        default_factory=lambda: None, alias="containerName"
    )

    request_name: str | None = Field(default_factory=lambda: None, alias="requestName")

    resource_name: str | None = Field(
        default_factory=lambda: None, alias="resourceName"
    )
