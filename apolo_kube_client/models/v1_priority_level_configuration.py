from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_priority_level_configuration_spec import V1PriorityLevelConfigurationSpec
from .v1_priority_level_configuration_status import V1PriorityLevelConfigurationStatus

__all__ = ("V1PriorityLevelConfiguration",)


class V1PriorityLevelConfiguration(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1PriorityLevelConfigurationSpec | None = Field(None, alias="spec")

    status: V1PriorityLevelConfigurationStatus | None = Field(None, alias="status")
