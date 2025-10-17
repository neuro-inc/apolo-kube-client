from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_bound_object_reference import V1BoundObjectReference

__all__ = ("V1TokenRequestSpec",)


class V1TokenRequestSpec(BaseModel):
    audiences: list[str] = Field(default=[])

    bound_object_ref: V1BoundObjectReference = Field(
        default_factory=lambda: V1BoundObjectReference(),
        serialization_alias="boundObjectRef",
        validation_alias=AliasChoices("bound_object_ref", "boundObjectRef"),
    )

    expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="expirationSeconds",
        validation_alias=AliasChoices("expiration_seconds", "expirationSeconds"),
    )
