from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_bound_object_reference import V1BoundObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1TokenRequestSpec",)


class V1TokenRequestSpec(BaseModel):
    audiences: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    bound_object_ref: Annotated[
        V1BoundObjectReference,
        BeforeValidator(_default_if_none(V1BoundObjectReference)),
    ] = Field(
        default_factory=lambda: V1BoundObjectReference(),
        serialization_alias="boundObjectRef",
        validation_alias=AliasChoices("bound_object_ref", "boundObjectRef"),
        exclude_if=_exclude_if,
    )

    expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="expirationSeconds",
        validation_alias=AliasChoices("expiration_seconds", "expirationSeconds"),
        exclude_if=_exclude_if,
    )
