from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_node_selector_term import V1NodeSelectorTerm

__all__ = ("V1NodeSelector",)


class V1NodeSelector(BaseModel):
    node_selector_terms: list[V1NodeSelectorTerm] | None = Field(
        None, alias="nodeSelectorTerms"
    )
