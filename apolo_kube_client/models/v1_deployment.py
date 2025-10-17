from pydantic import AliasChoices, BaseModel, Field
from .v1_deployment_spec import V1DeploymentSpec
from .v1_deployment_status import V1DeploymentStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Deployment",)


class V1Deployment(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1DeploymentSpec = Field(default_factory=lambda: V1DeploymentSpec())

    status: V1DeploymentStatus = Field(default_factory=lambda: V1DeploymentStatus())
