from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_non_resource_attributes import V1NonResourceAttributes
from .v1_resource_attributes import V1ResourceAttributes
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SubjectAccessReviewSpec",)


class V1SubjectAccessReviewSpec(BaseModel):
    extra: Annotated[
        dict[str, list[str]], BeforeValidator(_collection_if_none("{}"))
    ] = {}

    groups: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    non_resource_attributes: Annotated[
        V1NonResourceAttributes,
        BeforeValidator(_default_if_none(V1NonResourceAttributes)),
    ] = Field(
        default_factory=lambda: V1NonResourceAttributes(),
        serialization_alias="nonResourceAttributes",
        validation_alias=AliasChoices(
            "non_resource_attributes", "nonResourceAttributes"
        ),
    )

    resource_attributes: Annotated[
        V1ResourceAttributes, BeforeValidator(_default_if_none(V1ResourceAttributes))
    ] = Field(
        default_factory=lambda: V1ResourceAttributes(),
        serialization_alias="resourceAttributes",
        validation_alias=AliasChoices("resource_attributes", "resourceAttributes"),
    )

    uid: str | None = None

    user: str | None = None
