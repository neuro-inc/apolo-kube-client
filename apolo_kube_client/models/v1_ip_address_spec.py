from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_parent_reference import V1ParentReference

__all__ = ("V1IPAddressSpec",)


class V1IPAddressSpec(BaseModel):
    parent_ref: V1ParentReference = Field(
        default_factory=lambda: V1ParentReference(),
        serialization_alias="parentRef",
        validation_alias=AliasChoices("parent_ref", "parentRef"),
    )
