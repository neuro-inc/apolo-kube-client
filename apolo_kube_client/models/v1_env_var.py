from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_env_var_source import V1EnvVarSource

__all__ = ("V1EnvVar",)


class V1EnvVar(BaseModel):
    name: str | None = Field(default_factory=lambda: None)

    value: str | None = Field(default_factory=lambda: None)

    value_from: V1EnvVarSource = Field(
        default_factory=lambda: V1EnvVarSource(), alias="valueFrom"
    )
