from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_spec import V1NodeSpec
from .v1_node_status import V1NodeStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Node",)


class V1Node(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1NodeSpec = Field(default_factory=lambda: V1NodeSpec(), alias="spec")

    status: V1NodeStatus = Field(default_factory=lambda: V1NodeStatus(), alias="status")
