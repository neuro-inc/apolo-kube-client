from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1VolumeMount",)


class V1VolumeMount(BaseModel):
    mount_path: str | None = Field(
        default=None,
        serialization_alias="mountPath",
        validation_alias=AliasChoices("mount_path", "mountPath"),
        exclude_if=_exclude_if,
    )

    mount_propagation: str | None = Field(
        default=None,
        serialization_alias="mountPropagation",
        validation_alias=AliasChoices("mount_propagation", "mountPropagation"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

    recursive_read_only: str | None = Field(
        default=None,
        serialization_alias="recursiveReadOnly",
        validation_alias=AliasChoices("recursive_read_only", "recursiveReadOnly"),
        exclude_if=_exclude_if,
    )

    sub_path: str | None = Field(
        default=None,
        serialization_alias="subPath",
        validation_alias=AliasChoices("sub_path", "subPath"),
        exclude_if=_exclude_if,
    )

    sub_path_expr: str | None = Field(
        default=None,
        serialization_alias="subPathExpr",
        validation_alias=AliasChoices("sub_path_expr", "subPathExpr"),
        exclude_if=_exclude_if,
    )
