from pydantic import BaseModel
from .utils import _collection_if_none
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
    ] = []
