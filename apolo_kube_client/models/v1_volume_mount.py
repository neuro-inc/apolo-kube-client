from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1VolumeMount",)


class V1VolumeMount(BaseModel):
    mount_path: str | None = Field(None, alias="mountPath")

    mount_propagation: str | None = Field(None, alias="mountPropagation")

    name: str | None = Field(None, alias="name")

    read_only: bool | None = Field(None, alias="readOnly")

    recursive_read_only: str | None = Field(None, alias="recursiveReadOnly")

    sub_path: str | None = Field(None, alias="subPath")

    sub_path_expr: str | None = Field(None, alias="subPathExpr")
