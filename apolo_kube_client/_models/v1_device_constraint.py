from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceConstraint",)


class V1DeviceConstraint(BaseModel):
    distinct_attribute: str | None = Field(
        default=None,
        serialization_alias="distinctAttribute",
        validation_alias=AliasChoices("distinct_attribute", "distinctAttribute"),
    )

    match_attribute: str | None = Field(
        default=None,
        serialization_alias="matchAttribute",
        validation_alias=AliasChoices("match_attribute", "matchAttribute"),
    )

    requests: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
