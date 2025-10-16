from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_scale_spec import V1ScaleSpec
from .v1_scale_status import V1ScaleStatus

__all__ = ("V1Scale",)


class V1Scale(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1ScaleSpec = Field(default_factory=lambda: V1ScaleSpec(), alias="spec")

    status: V1ScaleStatus = Field(
        default_factory=lambda: V1ScaleStatus(), alias="status"
    )
