from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_resource_slice_spec import V1ResourceSliceSpec

__all__ = ("V1ResourceSlice",)


class V1ResourceSlice(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1ResourceSliceSpec = Field(default_factory=lambda: V1ResourceSliceSpec())
