from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1VolumeMount",)


class V1VolumeMount(BaseModel):
    mount_path: str | None = Field(
        default=None,
        serialization_alias="mountPath",
        validation_alias=AliasChoices("mount_path", "mountPath"),
    )

    mount_propagation: str | None = Field(
        default=None,
        serialization_alias="mountPropagation",
        validation_alias=AliasChoices("mount_propagation", "mountPropagation"),
    )

    name: str | None = None

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    recursive_read_only: str | None = Field(
        default=None,
        serialization_alias="recursiveReadOnly",
        validation_alias=AliasChoices("recursive_read_only", "recursiveReadOnly"),
    )

    sub_path: str | None = Field(
        default=None,
        serialization_alias="subPath",
        validation_alias=AliasChoices("sub_path", "subPath"),
    )

    sub_path_expr: str | None = Field(
        default=None,
        serialization_alias="subPathExpr",
        validation_alias=AliasChoices("sub_path_expr", "subPathExpr"),
    )
