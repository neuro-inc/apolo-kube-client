from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1FlexVolumeSource",)


class V1FlexVolumeSource(BaseModel):
    driver: str | None = Field(default_factory=lambda: None, alias="driver")

    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    options: dict[str, str] = Field(default_factory=lambda: {}, alias="options")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_ref: V1LocalObjectReference = Field(
        default_factory=lambda: V1LocalObjectReference(), alias="secretRef"
    )
