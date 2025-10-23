from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1QueuingConfiguration",)


class V1QueuingConfiguration(BaseModel):
    hand_size: int | None = Field(
        default=None,
        serialization_alias="handSize",
        validation_alias=AliasChoices("hand_size", "handSize"),
        exclude_if=_exclude_if,
    )

    queue_length_limit: int | None = Field(
        default=None,
        serialization_alias="queueLengthLimit",
        validation_alias=AliasChoices("queue_length_limit", "queueLengthLimit"),
        exclude_if=_exclude_if,
    )

    queues: int | None = Field(default=None, exclude_if=_exclude_if)
