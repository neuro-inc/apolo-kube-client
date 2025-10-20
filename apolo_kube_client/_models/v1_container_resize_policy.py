from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ContainerResizePolicy",)


class V1ContainerResizePolicy(BaseModel):
    resource_name: str | None = Field(
        default=None,
        serialization_alias="resourceName",
        validation_alias=AliasChoices("resource_name", "resourceName"),
    )

    restart_policy: str | None = Field(
        default=None,
        serialization_alias="restartPolicy",
        validation_alias=AliasChoices("restart_policy", "restartPolicy"),
    )
