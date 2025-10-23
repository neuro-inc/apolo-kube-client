from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1PhotonPersistentDiskVolumeSource",)


class V1PhotonPersistentDiskVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
        exclude_if=_exclude_if,
    )

    pd_id: str | None = Field(
        default=None,
        serialization_alias="pdID",
        validation_alias=AliasChoices("pd_id", "pdID"),
        exclude_if=_exclude_if,
    )
