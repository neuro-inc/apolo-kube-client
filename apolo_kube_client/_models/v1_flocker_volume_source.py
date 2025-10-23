from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1FlockerVolumeSource",)


class V1FlockerVolumeSource(BaseModel):
    dataset_name: str | None = Field(
        default=None,
        serialization_alias="datasetName",
        validation_alias=AliasChoices("dataset_name", "datasetName"),
        exclude_if=_exclude_if,
    )

    dataset_uuid: str | None = Field(
        default=None,
        serialization_alias="datasetUUID",
        validation_alias=AliasChoices("dataset_uuid", "datasetUUID"),
        exclude_if=_exclude_if,
    )
