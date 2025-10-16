from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_bound_object_reference import V1BoundObjectReference

__all__ = ("V1TokenRequestSpec",)


class V1TokenRequestSpec(BaseModel):
    audiences: list[str] | None = Field(None, alias="audiences")

    bound_object_ref: V1BoundObjectReference | None = Field(
        None, alias="boundObjectRef"
    )

    expiration_seconds: int | None = Field(None, alias="expirationSeconds")
