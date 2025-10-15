from pydantic import BaseModel, Field

from .v1_secret_reference import V1SecretReference


class V1CinderPersistentVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    read_only: bool | None = Field(None, alias="readOnly")

    secret_ref: V1SecretReference | None = Field(None, alias="secretRef")

    volume_id: str | None = Field(None, alias="volumeID")
