from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_deployment_spec import V1DeploymentSpec
from .v1_deployment_status import V1DeploymentStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Deployment",)


class V1Deployment(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1DeploymentSpec = Field(
        default_factory=lambda: V1DeploymentSpec(), alias="spec"
    )

    status: V1DeploymentStatus = Field(
        default_factory=lambda: V1DeploymentStatus(), alias="status"
    )
