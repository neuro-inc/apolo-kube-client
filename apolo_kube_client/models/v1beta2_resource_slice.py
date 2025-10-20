from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1beta2_resource_slice_spec import V1beta2ResourceSliceSpec

__all__ = ("V1beta2ResourceSlice",)


class V1beta2ResourceSlice(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1beta2ResourceSliceSpec = Field(
        default_factory=lambda: V1beta2ResourceSliceSpec()
    )
