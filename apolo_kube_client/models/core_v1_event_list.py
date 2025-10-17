from pydantic import AliasChoices, BaseModel, Field
from .core_v1_event import CoreV1Event
from .v1_list_meta import V1ListMeta

__all__ = ("CoreV1EventList",)


class CoreV1EventList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[CoreV1Event] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
