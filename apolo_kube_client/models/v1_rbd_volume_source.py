from pydantic import BaseModel, Field

from .v1_local_object_reference import V1LocalObjectReference


class V1RBDVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    image: str | None = Field(None, alias="image")

    keyring: str | None = Field(None, alias="keyring")

    monitors: list[str] | None = Field(None, alias="monitors")

    pool: str | None = Field(None, alias="pool")

    read_only: bool | None = Field(None, alias="readOnly")

    secret_ref: V1LocalObjectReference | None = Field(None, alias="secretRef")

    user: str | None = Field(None, alias="user")
