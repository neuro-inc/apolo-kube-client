from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_bound_object_reference import V1BoundObjectReference

__all__ = ("V1TokenRequestSpec",)


class V1TokenRequestSpec(BaseModel):
    audiences: list[str] = Field(default_factory=lambda: [])

    bound_object_ref: V1BoundObjectReference = Field(
        default_factory=lambda: V1BoundObjectReference(), alias="boundObjectRef"
    )

    expiration_seconds: int | None = Field(
        default_factory=lambda: None, alias="expirationSeconds"
    )
