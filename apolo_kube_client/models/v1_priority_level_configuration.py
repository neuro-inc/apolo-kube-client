from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_priority_level_configuration_spec import V1PriorityLevelConfigurationSpec
from .v1_priority_level_configuration_status import V1PriorityLevelConfigurationStatus

__all__ = ("V1PriorityLevelConfiguration",)


class V1PriorityLevelConfiguration(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1PriorityLevelConfigurationSpec = Field(
        default_factory=lambda: V1PriorityLevelConfigurationSpec(), alias="spec"
    )

    status: V1PriorityLevelConfigurationStatus = Field(
        default_factory=lambda: V1PriorityLevelConfigurationStatus(), alias="status"
    )
