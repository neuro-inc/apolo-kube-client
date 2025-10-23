from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ContainerExtendedResourceRequest",)


class V1ContainerExtendedResourceRequest(BaseModel):
    container_name: str | None = Field(
        default=None,
        serialization_alias="containerName",
        validation_alias=AliasChoices("container_name", "containerName"),
        exclude_if=_exclude_if,
    )

    request_name: str | None = Field(
        default=None,
        serialization_alias="requestName",
        validation_alias=AliasChoices("request_name", "requestName"),
        exclude_if=_exclude_if,
    )

    resource_name: str | None = Field(
        default=None,
        serialization_alias="resourceName",
        validation_alias=AliasChoices("resource_name", "resourceName"),
        exclude_if=_exclude_if,
    )
