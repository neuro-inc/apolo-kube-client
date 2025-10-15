from pydantic import BaseModel, Field


class V1GCEPersistentDiskVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    partition: int | None = Field(None, alias="partition")

    pd_name: str | None = Field(None, alias="pdName")

    read_only: bool | None = Field(None, alias="readOnly")
