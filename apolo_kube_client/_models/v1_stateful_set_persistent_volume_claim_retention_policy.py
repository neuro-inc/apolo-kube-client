from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1StatefulSetPersistentVolumeClaimRetentionPolicy",)


class V1StatefulSetPersistentVolumeClaimRetentionPolicy(BaseModel):
    when_deleted: str | None = Field(
        default=None,
        serialization_alias="whenDeleted",
        validation_alias=AliasChoices("when_deleted", "whenDeleted"),
        exclude_if=_exclude_if,
    )

    when_scaled: str | None = Field(
        default=None,
        serialization_alias="whenScaled",
        validation_alias=AliasChoices("when_scaled", "whenScaled"),
        exclude_if=_exclude_if,
    )
