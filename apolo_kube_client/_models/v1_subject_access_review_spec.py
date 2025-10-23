from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_non_resource_attributes import V1NonResourceAttributes
from .v1_resource_attributes import V1ResourceAttributes
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SubjectAccessReviewSpec",)


class V1SubjectAccessReviewSpec(BaseModel):
    extra: Annotated[
        dict[str, list[str]], BeforeValidator(_collection_if_none("{}"))
    ] = Field(default={}, exclude_if=_exclude_if)

    groups: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    non_resource_attributes: Annotated[
        V1NonResourceAttributes,
        BeforeValidator(_default_if_none(V1NonResourceAttributes)),
    ] = Field(
        default_factory=lambda: V1NonResourceAttributes(),
        serialization_alias="nonResourceAttributes",
        validation_alias=AliasChoices(
            "non_resource_attributes", "nonResourceAttributes"
        ),
        exclude_if=_exclude_if,
    )

    resource_attributes: Annotated[
        V1ResourceAttributes, BeforeValidator(_default_if_none(V1ResourceAttributes))
    ] = Field(
        default_factory=lambda: V1ResourceAttributes(),
        serialization_alias="resourceAttributes",
        validation_alias=AliasChoices("resource_attributes", "resourceAttributes"),
        exclude_if=_exclude_if,
    )

    uid: str | None = Field(default=None, exclude_if=_exclude_if)

    user: str | None = Field(default=None, exclude_if=_exclude_if)
