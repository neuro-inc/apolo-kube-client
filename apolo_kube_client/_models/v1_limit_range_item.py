from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LimitRangeItem",)


class V1LimitRangeItem(BaseModel):
    default: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}

    default_request: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="defaultRequest",
        validation_alias=AliasChoices("default_request", "defaultRequest"),
    )

    max: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}

    max_limit_request_ratio: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="maxLimitRequestRatio",
        validation_alias=AliasChoices(
            "max_limit_request_ratio", "maxLimitRequestRatio"
        ),
    )

    min: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}

    type: str | None = None
