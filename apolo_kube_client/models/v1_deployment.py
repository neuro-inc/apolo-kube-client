from pydantic import BaseModel, Field

from .v1_deployment_spec import V1DeploymentSpec
from .v1_deployment_status import V1DeploymentStatus
from .v1_object_meta import V1ObjectMeta


class V1Deployment(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1DeploymentSpec | None = Field(None, alias="spec")

    status: V1DeploymentStatus | None = Field(None, alias="status")
