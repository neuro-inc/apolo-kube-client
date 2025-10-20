from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1NodeFeatures",)


class V1NodeFeatures(BaseModel):
    supplemental_groups_policy: bool | None = Field(
        default=None,
        serialization_alias="supplementalGroupsPolicy",
        validation_alias=AliasChoices(
            "supplemental_groups_policy", "supplementalGroupsPolicy"
        ),
    )
