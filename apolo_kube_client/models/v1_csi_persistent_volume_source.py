from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_secret_reference import V1SecretReference

__all__ = ("V1CSIPersistentVolumeSource",)


class V1CSIPersistentVolumeSource(BaseModel):
    controller_expand_secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(), alias="controllerExpandSecretRef"
    )

    controller_publish_secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(), alias="controllerPublishSecretRef"
    )

    driver: str | None = Field(default_factory=lambda: None)

    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    node_expand_secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(), alias="nodeExpandSecretRef"
    )

    node_publish_secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(), alias="nodePublishSecretRef"
    )

    node_stage_secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(), alias="nodeStageSecretRef"
    )

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    volume_attributes: dict[str, str] = Field(
        default_factory=lambda: {}, alias="volumeAttributes"
    )

    volume_handle: str | None = Field(
        default_factory=lambda: None, alias="volumeHandle"
    )
