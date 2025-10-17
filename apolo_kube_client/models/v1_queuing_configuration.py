from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1QueuingConfiguration",)


class V1QueuingConfiguration(BaseModel):
    hand_size: int | None = Field(
        default=None,
        serialization_alias="handSize",
        validation_alias=AliasChoices("hand_size", "handSize"),
    )

    queue_length_limit: int | None = Field(
        default=None,
        serialization_alias="queueLengthLimit",
        validation_alias=AliasChoices("queue_length_limit", "queueLengthLimit"),
    )

    queues: int | None = Field(default=None)
