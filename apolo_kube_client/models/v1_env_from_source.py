from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_config_map_env_source import V1ConfigMapEnvSource
from .v1_secret_env_source import V1SecretEnvSource

__all__ = ("V1EnvFromSource",)


class V1EnvFromSource(BaseModel):
    config_map_ref: V1ConfigMapEnvSource = Field(
        default_factory=lambda: V1ConfigMapEnvSource(), alias="configMapRef"
    )

    prefix: str | None = Field(default_factory=lambda: None)

    secret_ref: V1SecretEnvSource = Field(
        default_factory=lambda: V1SecretEnvSource(), alias="secretRef"
    )
