from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1LinuxContainerUser",)


class V1LinuxContainerUser(BaseModel):
    gid: int | None = None

    supplemental_groups: list[int] = Field(
        default=[],
        serialization_alias="supplementalGroups",
        validation_alias=AliasChoices("supplemental_groups", "supplementalGroups"),
    )

    uid: int | None = None
