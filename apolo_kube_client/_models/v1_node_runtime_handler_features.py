from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1NodeRuntimeHandlerFeatures",)


class V1NodeRuntimeHandlerFeatures(BaseModel):
    recursive_read_only_mounts: bool | None = Field(
        default=None,
        serialization_alias="recursiveReadOnlyMounts",
        validation_alias=AliasChoices(
            "recursive_read_only_mounts", "recursiveReadOnlyMounts"
        ),
    )

    user_namespaces: bool | None = Field(
        default=None,
        serialization_alias="userNamespaces",
        validation_alias=AliasChoices("user_namespaces", "userNamespaces"),
    )
