from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_status_details import V1StatusDetails

__all__ = ("V1Status",)


class V1Status(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    code: int | None = Field(None, alias="code")

    details: V1StatusDetails | None = Field(None, alias="details")

    kind: str | None = Field(None, alias="kind")

    message: str | None = Field(None, alias="message")

    metadata: V1ListMeta | None = Field(None, alias="metadata")

    reason: str | None = Field(None, alias="reason")

    status: str | None = Field(None, alias="status")
