from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1VolumeMount",)


class V1VolumeMount(BaseModel):
    mount_path: str | None = Field(default_factory=lambda: None, alias="mountPath")

    mount_propagation: str | None = Field(
        default_factory=lambda: None, alias="mountPropagation"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    recursive_read_only: str | None = Field(
        default_factory=lambda: None, alias="recursiveReadOnly"
    )

    sub_path: str | None = Field(default_factory=lambda: None, alias="subPath")

    sub_path_expr: str | None = Field(default_factory=lambda: None, alias="subPathExpr")
