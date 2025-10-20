from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1PersistentVolumeClaimVolumeSource",)


class V1PersistentVolumeClaimVolumeSource(BaseModel):
    claim_name: str | None = Field(
        default=None,
        serialization_alias="claimName",
        validation_alias=AliasChoices("claim_name", "claimName"),
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )
