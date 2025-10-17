from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_priority_level_configuration_spec import V1PriorityLevelConfigurationSpec
from .v1_priority_level_configuration_status import V1PriorityLevelConfigurationStatus

__all__ = ("V1PriorityLevelConfiguration",)


class V1PriorityLevelConfiguration(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1PriorityLevelConfigurationSpec = Field(
        default_factory=lambda: V1PriorityLevelConfigurationSpec()
    )

    status: V1PriorityLevelConfigurationStatus = Field(
        default_factory=lambda: V1PriorityLevelConfigurationStatus()
    )
