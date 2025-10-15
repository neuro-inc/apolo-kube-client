from pydantic import BaseModel, Field

from .v1_local_object_reference import V1LocalObjectReference


class V1CephFSVolumeSource(BaseModel):
    monitors: list[str] | None = Field(None, alias="monitors")

    path: str | None = Field(None, alias="path")

    read_only: bool | None = Field(None, alias="readOnly")

    secret_file: str | None = Field(None, alias="secretFile")

    secret_ref: V1LocalObjectReference | None = Field(None, alias="secretRef")

    user: str | None = Field(None, alias="user")
