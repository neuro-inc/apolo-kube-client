from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_status_details import V1StatusDetails

__all__ = ("V1Status",)


class V1Status(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    code: int | None = Field(default=None)

    details: V1StatusDetails = Field(default_factory=lambda: V1StatusDetails())

    kind: str | None = Field(default=None)

    message: str | None = Field(default=None)

    metadata: V1ListMeta

    reason: str | None = Field(default=None)

    status: str | None = Field(default=None)
