from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ConfigMapNodeConfigSource",)


class V1ConfigMapNodeConfigSource(BaseModel):
    kubelet_config_key: str | None = Field(
        default_factory=lambda: None, alias="kubeletConfigKey"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")

    namespace: str | None = Field(default_factory=lambda: None, alias="namespace")

    resource_version: str | None = Field(
        default_factory=lambda: None, alias="resourceVersion"
    )

    uid: str | None = Field(default_factory=lambda: None, alias="uid")
