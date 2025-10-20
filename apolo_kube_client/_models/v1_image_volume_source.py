from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ImageVolumeSource",)


class V1ImageVolumeSource(BaseModel):
    pull_policy: str | None = Field(
        default=None,
        serialization_alias="pullPolicy",
        validation_alias=AliasChoices("pull_policy", "pullPolicy"),
    )

    reference: str | None = None
