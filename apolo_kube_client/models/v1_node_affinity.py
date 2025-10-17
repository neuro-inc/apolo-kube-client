from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_selector import V1NodeSelector
from .v1_preferred_scheduling_term import V1PreferredSchedulingTerm

__all__ = ("V1NodeAffinity",)


class V1NodeAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: list[
        V1PreferredSchedulingTerm
    ] = Field(
        default_factory=lambda: [],
        alias="preferredDuringSchedulingIgnoredDuringExecution",
    )

    required_during_scheduling_ignored_during_execution: V1NodeSelector = Field(
        default_factory=lambda: V1NodeSelector(),
        alias="requiredDuringSchedulingIgnoredDuringExecution",
    )
