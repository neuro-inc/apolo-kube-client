from pydantic import BaseModel, Field

from .core_v1_event import CoreV1Event
from .v1_list_meta import V1ListMeta


class CoreV1EventList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[CoreV1Event] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
