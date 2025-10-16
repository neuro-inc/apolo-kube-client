from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1GlusterfsPersistentVolumeSource",)


class V1GlusterfsPersistentVolumeSource(BaseModel):
    endpoints: str | None = Field(None, alias="endpoints")

    endpoints_namespace: str | None = Field(None, alias="endpointsNamespace")

    path: str | None = Field(None, alias="path")

    read_only: bool | None = Field(None, alias="readOnly")
