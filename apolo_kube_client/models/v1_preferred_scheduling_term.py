from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_selector_term import V1NodeSelectorTerm

__all__ = ("V1PreferredSchedulingTerm",)


class V1PreferredSchedulingTerm(BaseModel):
    preference: V1NodeSelectorTerm = Field(
        default_factory=lambda: V1NodeSelectorTerm(), alias="preference"
    )

    weight: int | None = Field(default_factory=lambda: None, alias="weight")
