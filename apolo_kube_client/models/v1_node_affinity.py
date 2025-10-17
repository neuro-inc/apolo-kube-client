from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_node_selector import V1NodeSelector
from .v1_preferred_scheduling_term import V1PreferredSchedulingTerm

__all__ = ("V1NodeAffinity",)


class V1NodeAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: list[
        V1PreferredSchedulingTerm
    ] = Field(
        default=[],
        serialization_alias="preferredDuringSchedulingIgnoredDuringExecution",
        validation_alias=AliasChoices(
            "preferred_during_scheduling_ignored_during_execution",
            "preferredDuringSchedulingIgnoredDuringExecution",
        ),
    )

    required_during_scheduling_ignored_during_execution: V1NodeSelector = Field(
        default_factory=lambda: V1NodeSelector(),
        serialization_alias="requiredDuringSchedulingIgnoredDuringExecution",
        validation_alias=AliasChoices(
            "required_during_scheduling_ignored_during_execution",
            "requiredDuringSchedulingIgnoredDuringExecution",
        ),
    )
