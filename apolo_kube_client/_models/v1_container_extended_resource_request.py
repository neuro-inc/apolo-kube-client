from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ContainerExtendedResourceRequest",)


class V1ContainerExtendedResourceRequest(BaseModel):
    container_name: str | None = Field(
        default=None,
        serialization_alias="containerName",
        validation_alias=AliasChoices("container_name", "containerName"),
    )

    request_name: str | None = Field(
        default=None,
        serialization_alias="requestName",
        validation_alias=AliasChoices("request_name", "requestName"),
    )

    resource_name: str | None = Field(
        default=None,
        serialization_alias="resourceName",
        validation_alias=AliasChoices("resource_name", "resourceName"),
    )
