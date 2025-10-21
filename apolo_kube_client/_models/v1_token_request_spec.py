from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_bound_object_reference import V1BoundObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1TokenRequestSpec",)


class V1TokenRequestSpec(BaseModel):
    audiences: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    bound_object_ref: Annotated[
        V1BoundObjectReference,
        BeforeValidator(_default_if_none(V1BoundObjectReference)),
    ] = Field(
        default_factory=lambda: V1BoundObjectReference(),
        serialization_alias="boundObjectRef",
        validation_alias=AliasChoices("bound_object_ref", "boundObjectRef"),
    )

    expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="expirationSeconds",
        validation_alias=AliasChoices("expiration_seconds", "expirationSeconds"),
    )
