from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ConfigMapNodeConfigSource",)


class V1ConfigMapNodeConfigSource(BaseModel):
    kubelet_config_key: str | None = Field(
        default=None,
        serialization_alias="kubeletConfigKey",
        validation_alias=AliasChoices("kubelet_config_key", "kubeletConfigKey"),
    )

    name: str | None = Field(default=None)

    namespace: str | None = Field(default=None)

    resource_version: str | None = Field(
        default=None,
        serialization_alias="resourceVersion",
        validation_alias=AliasChoices("resource_version", "resourceVersion"),
    )

    uid: str | None = Field(default=None)
