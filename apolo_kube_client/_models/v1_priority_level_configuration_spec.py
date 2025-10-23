from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_exempt_priority_level_configuration import V1ExemptPriorityLevelConfiguration
from .v1_limited_priority_level_configuration import V1LimitedPriorityLevelConfiguration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PriorityLevelConfigurationSpec",)


class V1PriorityLevelConfigurationSpec(BaseModel):
    exempt: Annotated[
        V1ExemptPriorityLevelConfiguration,
        BeforeValidator(_default_if_none(V1ExemptPriorityLevelConfiguration)),
    ] = Field(
        default_factory=lambda: V1ExemptPriorityLevelConfiguration(),
        exclude_if=_exclude_if,
    )

    limited: Annotated[
        V1LimitedPriorityLevelConfiguration,
        BeforeValidator(_default_if_none(V1LimitedPriorityLevelConfiguration)),
    ] = Field(
        default_factory=lambda: V1LimitedPriorityLevelConfiguration(),
        exclude_if=_exclude_if,
    )

    type: str | None = Field(default=None, exclude_if=_exclude_if)
