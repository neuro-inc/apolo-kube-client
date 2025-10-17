from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_daemon_set import V1DaemonSet
from .v1_list_meta import V1ListMeta

__all__ = ("V1DaemonSetList",)


class V1DaemonSetList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1DaemonSet] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
