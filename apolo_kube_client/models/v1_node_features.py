from pydantic import BaseModel, Field


class V1NodeFeatures(BaseModel):
    supplemental_groups_policy: bool | None = Field(
        None, alias="supplementalGroupsPolicy"
    )
