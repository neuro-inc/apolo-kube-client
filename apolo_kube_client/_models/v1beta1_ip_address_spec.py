from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1beta1_parent_reference import V1beta1ParentReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1IPAddressSpec",)


class V1beta1IPAddressSpec(BaseModel):
    parent_ref: Annotated[
        V1beta1ParentReference,
        BeforeValidator(_default_if_none(V1beta1ParentReference)),
    ] = Field(
        default_factory=lambda: V1beta1ParentReference(),
        serialization_alias="parentRef",
        validation_alias=AliasChoices("parent_ref", "parentRef"),
    )
