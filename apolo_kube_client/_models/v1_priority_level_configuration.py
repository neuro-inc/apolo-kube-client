from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1_priority_level_configuration_spec import V1PriorityLevelConfigurationSpec
from .v1_priority_level_configuration_status import V1PriorityLevelConfigurationStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PriorityLevelConfiguration",)


class V1PriorityLevelConfiguration(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[
        V1PriorityLevelConfigurationSpec,
        BeforeValidator(_default_if_none(V1PriorityLevelConfigurationSpec)),
    ] = Field(
        default_factory=lambda: V1PriorityLevelConfigurationSpec(),
        exclude_if=_exclude_if,
    )

    status: Annotated[
        V1PriorityLevelConfigurationStatus,
        BeforeValidator(_default_if_none(V1PriorityLevelConfigurationStatus)),
    ] = Field(
        default_factory=lambda: V1PriorityLevelConfigurationStatus(),
        exclude_if=_exclude_if,
    )
