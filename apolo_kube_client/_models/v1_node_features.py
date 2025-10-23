from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1NodeFeatures",)


class V1NodeFeatures(BaseModel):
    supplemental_groups_policy: bool | None = Field(
        default=None,
        serialization_alias="supplementalGroupsPolicy",
        validation_alias=AliasChoices(
            "supplemental_groups_policy", "supplementalGroupsPolicy"
        ),
        exclude_if=_exclude_if,
    )
