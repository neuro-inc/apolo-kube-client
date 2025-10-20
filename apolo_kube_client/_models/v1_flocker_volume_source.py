from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1FlockerVolumeSource",)


class V1FlockerVolumeSource(BaseModel):
    dataset_name: str | None = Field(
        default=None,
        serialization_alias="datasetName",
        validation_alias=AliasChoices("dataset_name", "datasetName"),
    )

    dataset_uuid: str | None = Field(
        default=None,
        serialization_alias="datasetUUID",
        validation_alias=AliasChoices("dataset_uuid", "datasetUUID"),
    )
