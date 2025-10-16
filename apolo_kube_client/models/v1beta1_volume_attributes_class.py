from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta

__all__ = ("V1beta1VolumeAttributesClass",)


class V1beta1VolumeAttributesClass(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    driver_name: str | None = Field(None, alias="driverName")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    parameters: dict[str, str] | None = Field(None, alias="parameters")
