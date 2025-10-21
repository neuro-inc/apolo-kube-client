from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_status_cause import V1StatusCause
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1StatusDetails",)


class V1StatusDetails(BaseModel):
    causes: Annotated[
        list[V1StatusCause], BeforeValidator(_collection_if_none("[]"))
    ] = []

    group: str | None = None

    kind: str | None = None

    name: str | None = None

    retry_after_seconds: int | None = Field(
        default=None,
        serialization_alias="retryAfterSeconds",
        validation_alias=AliasChoices("retry_after_seconds", "retryAfterSeconds"),
    )

    uid: str | None = None
