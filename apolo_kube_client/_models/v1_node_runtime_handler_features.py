from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1NodeRuntimeHandlerFeatures",)


class V1NodeRuntimeHandlerFeatures(BaseModel):
    recursive_read_only_mounts: bool | None = Field(
        default=None,
        serialization_alias="recursiveReadOnlyMounts",
        validation_alias=AliasChoices(
            "recursive_read_only_mounts", "recursiveReadOnlyMounts"
        ),
        exclude_if=_exclude_if,
    )

    user_namespaces: bool | None = Field(
        default=None,
        serialization_alias="userNamespaces",
        validation_alias=AliasChoices("user_namespaces", "userNamespaces"),
        exclude_if=_exclude_if,
    )
