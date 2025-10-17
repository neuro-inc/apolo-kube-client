from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector

__all__ = ("V1PodAffinityTerm",)


class V1PodAffinityTerm(BaseModel):
    label_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="labelSelector"
    )

    match_label_keys: list[str] = Field(
        default_factory=lambda: [], alias="matchLabelKeys"
    )

    mismatch_label_keys: list[str] = Field(
        default_factory=lambda: [], alias="mismatchLabelKeys"
    )

    namespace_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="namespaceSelector"
    )

    namespaces: list[str] = Field(default_factory=lambda: [])

    topology_key: str | None = Field(default_factory=lambda: None, alias="topologyKey")
