from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_custom_resource_definition_spec import V1CustomResourceDefinitionSpec
from .v1_custom_resource_definition_status import V1CustomResourceDefinitionStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CustomResourceDefinition",)


class V1CustomResourceDefinition(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1CustomResourceDefinitionSpec = Field(
        default_factory=lambda: V1CustomResourceDefinitionSpec()
    )

    status: V1CustomResourceDefinitionStatus = Field(
        default_factory=lambda: V1CustomResourceDefinitionStatus()
    )
