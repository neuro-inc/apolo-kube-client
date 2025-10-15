from pydantic import BaseModel, Field


class V1FlockerVolumeSource(BaseModel):
    dataset_name: str | None = Field(None, alias="datasetName")

    dataset_uuid: str | None = Field(None, alias="datasetUUID")
