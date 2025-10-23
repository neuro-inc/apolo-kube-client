from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1DeviceConstraint",)


class V1beta1DeviceConstraint(BaseModel):
    distinct_attribute: str | None = Field(
        default=None,
        serialization_alias="distinctAttribute",
        validation_alias=AliasChoices("distinct_attribute", "distinctAttribute"),
        exclude_if=_exclude_if,
    )

    match_attribute: str | None = Field(
        default=None,
        serialization_alias="matchAttribute",
        validation_alias=AliasChoices("match_attribute", "matchAttribute"),
        exclude_if=_exclude_if,
    )

    requests: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )
