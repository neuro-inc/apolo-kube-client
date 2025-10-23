from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_user_info import V1UserInfo
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1TokenReviewStatus",)


class V1TokenReviewStatus(BaseModel):
    audiences: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    authenticated: bool | None = Field(default=None, exclude_if=_exclude_if)

    error: str | None = Field(default=None, exclude_if=_exclude_if)

    user: Annotated[V1UserInfo, BeforeValidator(_default_if_none(V1UserInfo))] = Field(
        default_factory=lambda: V1UserInfo(), exclude_if=_exclude_if
    )
