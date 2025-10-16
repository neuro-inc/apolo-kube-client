from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1QueuingConfiguration",)


class V1QueuingConfiguration(BaseModel):
    hand_size: int | None = Field(None, alias="handSize")

    queue_length_limit: int | None = Field(None, alias="queueLengthLimit")

    queues: int | None = Field(None, alias="queues")
