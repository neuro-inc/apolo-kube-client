from pydantic import BaseModel, Field

from .v1_secret_reference import V1SecretReference


class V1CSIPersistentVolumeSource(BaseModel):
    controller_expand_secret_ref: V1SecretReference | None = Field(
        None, alias="controllerExpandSecretRef"
    )

    controller_publish_secret_ref: V1SecretReference | None = Field(
        None, alias="controllerPublishSecretRef"
    )

    driver: str | None = Field(None, alias="driver")

    fs_type: str | None = Field(None, alias="fsType")

    node_expand_secret_ref: V1SecretReference | None = Field(
        None, alias="nodeExpandSecretRef"
    )

    node_publish_secret_ref: V1SecretReference | None = Field(
        None, alias="nodePublishSecretRef"
    )

    node_stage_secret_ref: V1SecretReference | None = Field(
        None, alias="nodeStageSecretRef"
    )

    read_only: bool | None = Field(None, alias="readOnly")

    volume_attributes: dict(str, str) | None = Field(None, alias="volumeAttributes")

    volume_handle: str | None = Field(None, alias="volumeHandle")
