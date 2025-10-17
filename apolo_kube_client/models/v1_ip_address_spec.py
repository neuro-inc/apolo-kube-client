from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_parent_reference import V1ParentReference

__all__ = ("V1IPAddressSpec",)


class V1IPAddressSpec(BaseModel):
    parent_ref: V1ParentReference = Field(
        default_factory=lambda: V1ParentReference(), alias="parentRef"
    )
