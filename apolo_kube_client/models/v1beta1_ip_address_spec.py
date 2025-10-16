from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_parent_reference import V1beta1ParentReference

__all__ = ("V1beta1IPAddressSpec",)


class V1beta1IPAddressSpec(BaseModel):
    parent_ref: V1beta1ParentReference = Field(
        default_factory=lambda: V1beta1ParentReference(), alias="parentRef"
    )
