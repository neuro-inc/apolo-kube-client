from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ImageVolumeSource",)


class V1ImageVolumeSource(BaseModel):
    pull_policy: str | None = Field(
        default=None,
        serialization_alias="pullPolicy",
        validation_alias=AliasChoices("pull_policy", "pullPolicy"),
        exclude_if=_exclude_if,
    )

    reference: str | None = Field(default=None, exclude_if=_exclude_if)
