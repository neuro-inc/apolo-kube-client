from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_queuing_configuration import V1QueuingConfiguration

__all__ = ("V1LimitResponse",)


class V1LimitResponse(BaseModel):
    queuing: V1QueuingConfiguration = Field(
        default_factory=lambda: V1QueuingConfiguration(), alias="queuing"
    )

    type: str | None = Field(default_factory=lambda: None, alias="type")
