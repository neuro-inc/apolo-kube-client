from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_replication_controller_spec import V1ReplicationControllerSpec
from .v1_replication_controller_status import V1ReplicationControllerStatus

__all__ = ("V1ReplicationController",)


class V1ReplicationController(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1ReplicationControllerSpec = Field(
        default_factory=lambda: V1ReplicationControllerSpec(), alias="spec"
    )

    status: V1ReplicationControllerStatus = Field(
        default_factory=lambda: V1ReplicationControllerStatus(), alias="status"
    )
