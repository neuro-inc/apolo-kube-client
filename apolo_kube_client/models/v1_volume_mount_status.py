from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1VolumeMountStatus",)


class V1VolumeMountStatus(BaseModel):
    mount_path: str | None = Field(
        default=None,
        serialization_alias="mountPath",
        validation_alias=AliasChoices("mount_path", "mountPath"),
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
