from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector

__all__ = ("V1TopologySpreadConstraint",)


class V1TopologySpreadConstraint(BaseModel):
    label_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="labelSelector"
    )

    match_label_keys: list[str] = Field(
        default_factory=lambda: [], alias="matchLabelKeys"
    )

    max_skew: int | None = Field(default_factory=lambda: None, alias="maxSkew")

    min_domains: int | None = Field(default_factory=lambda: None, alias="minDomains")

    node_affinity_policy: str | None = Field(
        default_factory=lambda: None, alias="nodeAffinityPolicy"
    )

    node_taints_policy: str | None = Field(
        default_factory=lambda: None, alias="nodeTaintsPolicy"
    )

    topology_key: str | None = Field(default_factory=lambda: None, alias="topologyKey")

    when_unsatisfiable: str | None = Field(
        default_factory=lambda: None, alias="whenUnsatisfiable"
    )
