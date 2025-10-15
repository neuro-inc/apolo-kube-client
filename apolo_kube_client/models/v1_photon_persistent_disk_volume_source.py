from pydantic import BaseModel, Field


class V1PhotonPersistentDiskVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    pd_id: str | None = Field(None, alias="pdID")
