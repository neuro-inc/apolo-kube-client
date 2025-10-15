from pydantic import BaseModel, Field

from .v1_secret_reference import V1SecretReference


class V1FlexPersistentVolumeSource(BaseModel):
    driver: str | None = Field(None, alias="driver")

    fs_type: str | None = Field(None, alias="fsType")

    options: dict(str, str) | None = Field(None, alias="options")

    read_only: bool | None = Field(None, alias="readOnly")

    secret_ref: V1SecretReference | None = Field(None, alias="secretRef")
