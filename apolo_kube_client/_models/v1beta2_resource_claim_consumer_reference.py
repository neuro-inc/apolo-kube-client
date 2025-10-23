from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1beta2ResourceClaimConsumerReference",)


class V1beta2ResourceClaimConsumerReference(BaseModel):
    api_group: str | None = Field(
        default=None,
        serialization_alias="apiGroup",
        validation_alias=AliasChoices("api_group", "apiGroup"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    resource: str | None = Field(default=None, exclude_if=_exclude_if)

    uid: str | None = Field(default=None, exclude_if=_exclude_if)
