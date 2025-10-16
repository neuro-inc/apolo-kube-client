from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1GlusterfsPersistentVolumeSource",)


class V1GlusterfsPersistentVolumeSource(BaseModel):
    endpoints: str | None = Field(default_factory=lambda: None, alias="endpoints")

    endpoints_namespace: str | None = Field(
        default_factory=lambda: None, alias="endpointsNamespace"
    )

    path: str | None = Field(default_factory=lambda: None, alias="path")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")
