from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_priority_level_configuration_condition import (
    V1PriorityLevelConfigurationCondition,
)
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PriorityLevelConfigurationStatus",)


class V1PriorityLevelConfigurationStatus(BaseModel):
    conditions: Annotated[
        list[V1PriorityLevelConfigurationCondition],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)
