from pydantic import BaseModel, Field

from .v1_custom_resource_definition_spec import V1CustomResourceDefinitionSpec
from .v1_custom_resource_definition_status import V1CustomResourceDefinitionStatus
from .v1_object_meta import V1ObjectMeta


class V1CustomResourceDefinition(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1CustomResourceDefinitionSpec | None = Field(None, alias="spec")

    status: V1CustomResourceDefinitionStatus | None = Field(None, alias="status")
