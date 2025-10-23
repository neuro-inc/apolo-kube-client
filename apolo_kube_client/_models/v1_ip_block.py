from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IPBlock",)


class V1IPBlock(BaseModel):
    cidr: str | None = Field(default=None, exclude_if=_exclude_if)

    except_: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[],
        serialization_alias="except",
        validation_alias=AliasChoices("except_", "except"),
        exclude_if=_exclude_if,
    )
