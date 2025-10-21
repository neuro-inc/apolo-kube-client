from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_parent_reference import V1ParentReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IPAddressSpec",)


class V1IPAddressSpec(BaseModel):
    parent_ref: Annotated[
        V1ParentReference, BeforeValidator(_default_if_none(V1ParentReference))
    ] = Field(
        default_factory=lambda: V1ParentReference(),
        serialization_alias="parentRef",
        validation_alias=AliasChoices("parent_ref", "parentRef"),
    )
