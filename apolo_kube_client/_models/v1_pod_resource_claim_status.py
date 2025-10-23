from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1PodResourceClaimStatus",)


class V1PodResourceClaimStatus(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    resource_claim_name: str | None = Field(
        default=None,
        serialization_alias="resourceClaimName",
        validation_alias=AliasChoices("resource_claim_name", "resourceClaimName"),
        exclude_if=_exclude_if,
    )
