from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1AppArmorProfile",)


class V1AppArmorProfile(BaseModel):
    localhost_profile: str | None = Field(
        default=None,
        serialization_alias="localhostProfile",
        validation_alias=AliasChoices("localhost_profile", "localhostProfile"),
    )

    type: str | None = None
