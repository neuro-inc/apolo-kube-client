from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_queuing_configuration import V1QueuingConfiguration

__all__ = ("V1LimitResponse",)


class V1LimitResponse(BaseModel):
    queuing: V1QueuingConfiguration | None = Field(None, alias="queuing")

    type: str | None = Field(None, alias="type")
