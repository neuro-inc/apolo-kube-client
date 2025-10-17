from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_job import V1Job
from .v1_list_meta import V1ListMeta

__all__ = ("V1JobList",)


class V1JobList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1Job] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
