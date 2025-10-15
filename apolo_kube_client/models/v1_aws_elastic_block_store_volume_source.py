from pydantic import BaseModel, Field


class V1AWSElasticBlockStoreVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    partition: int | None = Field(None, alias="partition")

    read_only: bool | None = Field(None, alias="readOnly")

    volume_id: str | None = Field(None, alias="volumeID")
