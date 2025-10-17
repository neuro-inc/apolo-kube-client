from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_deployment import V1Deployment
from .v1_list_meta import V1ListMeta

__all__ = ("V1DeploymentList",)


class V1DeploymentList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1Deployment] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
