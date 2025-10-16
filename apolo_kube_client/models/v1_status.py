from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_status_details import V1StatusDetails

__all__ = ("V1Status",)


class V1Status(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    code: int | None = Field(default_factory=lambda: None, alias="code")

    details: V1StatusDetails = Field(
        default_factory=lambda: V1StatusDetails(), alias="details"
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    message: str | None = Field(default_factory=lambda: None, alias="message")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")

    reason: str | None = Field(default_factory=lambda: None, alias="reason")

    status: str | None = Field(default_factory=lambda: None, alias="status")
