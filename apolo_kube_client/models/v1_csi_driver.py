from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_csi_driver_spec import V1CSIDriverSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CSIDriver",)


class V1CSIDriver(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1CSIDriverSpec = Field(
        default_factory=lambda: V1CSIDriverSpec(), alias="spec"
    )
