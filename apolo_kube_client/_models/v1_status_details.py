from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_status_cause import V1StatusCause
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1StatusDetails",)


class V1StatusDetails(BaseModel):
    causes: Annotated[
        list[V1StatusCause], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    group: str | None = Field(default=None, exclude_if=_exclude_if)

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    retry_after_seconds: int | None = Field(
        default=None,
        serialization_alias="retryAfterSeconds",
        validation_alias=AliasChoices("retry_after_seconds", "retryAfterSeconds"),
        exclude_if=_exclude_if,
    )

    uid: str | None = Field(default=None, exclude_if=_exclude_if)
