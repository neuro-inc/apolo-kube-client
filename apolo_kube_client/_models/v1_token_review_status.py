from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_user_info import V1UserInfo
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1TokenReviewStatus",)


class V1TokenReviewStatus(BaseModel):
    audiences: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    authenticated: bool | None = None

    error: str | None = None

    user: Annotated[V1UserInfo, BeforeValidator(_default_if_none(V1UserInfo))] = Field(
        default_factory=lambda: V1UserInfo()
    )
