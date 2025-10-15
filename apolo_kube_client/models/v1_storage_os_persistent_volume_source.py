from pydantic import BaseModel, Field

from .v1_object_reference import V1ObjectReference


class V1StorageOSPersistentVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    read_only: bool | None = Field(None, alias="readOnly")

    secret_ref: V1ObjectReference | None = Field(None, alias="secretRef")

    volume_name: str | None = Field(None, alias="volumeName")

    volume_namespace: str | None = Field(None, alias="volumeNamespace")
