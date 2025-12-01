from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none
from .v1_priority_level_configuration_condition import (
    V1PriorityLevelConfigurationCondition,
)


__all__ = ("V1PriorityLevelConfigurationStatus",)


class V1PriorityLevelConfigurationStatus(BaseConfiguredModel):
    """PriorityLevelConfigurationStatus represents the current state of a "request-priority"."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationStatus"
    )

    conditions: Annotated[
        list[V1PriorityLevelConfigurationCondition],
        Field(
            description="""`conditions` is the current state of "request-priority".""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
