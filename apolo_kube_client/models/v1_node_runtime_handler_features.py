from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1NodeRuntimeHandlerFeatures",)


class V1NodeRuntimeHandlerFeatures(BaseModel):
    recursive_read_only_mounts: bool | None = Field(
        default_factory=lambda: None, alias="recursiveReadOnlyMounts"
    )

    user_namespaces: bool | None = Field(
        default_factory=lambda: None, alias="userNamespaces"
    )
