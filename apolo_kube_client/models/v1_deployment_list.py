from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_deployment import V1Deployment
from .v1_list_meta import V1ListMeta

__all__ = ("V1DeploymentList",)


class V1DeploymentList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1Deployment] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
