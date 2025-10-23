from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LimitRangeItem",)


class V1LimitRangeItem(BaseModel):
    default: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = (
        Field(default={}, exclude_if=_exclude_if)
    )

    default_request: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="defaultRequest",
        validation_alias=AliasChoices("default_request", "defaultRequest"),
        exclude_if=_exclude_if,
    )

    max: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = Field(
        default={}, exclude_if=_exclude_if
    )

    max_limit_request_ratio: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="maxLimitRequestRatio",
        validation_alias=AliasChoices(
            "max_limit_request_ratio", "maxLimitRequestRatio"
        ),
        exclude_if=_exclude_if,
    )

    min: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = Field(
        default={}, exclude_if=_exclude_if
    )

    type: str | None = Field(default=None, exclude_if=_exclude_if)
