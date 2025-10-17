from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1beta2_resource_slice_spec import V1beta2ResourceSliceSpec

__all__ = ("V1beta2ResourceSlice",)


class V1beta2ResourceSlice(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1beta2ResourceSliceSpec = Field(
        default_factory=lambda: V1beta2ResourceSliceSpec()
    )
