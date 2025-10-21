from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1TokenReviewSpec",)


class V1TokenReviewSpec(BaseModel):
    audiences: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    token: str | None = None
