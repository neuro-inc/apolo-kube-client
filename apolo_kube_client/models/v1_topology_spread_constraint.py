from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector


class V1TopologySpreadConstraint(BaseModel):
    label_selector: V1LabelSelector | None = Field(None, alias="labelSelector")

    match_label_keys: list[str] | None = Field(None, alias="matchLabelKeys")

    max_skew: int | None = Field(None, alias="maxSkew")

    min_domains: int | None = Field(None, alias="minDomains")

    node_affinity_policy: str | None = Field(None, alias="nodeAffinityPolicy")

    node_taints_policy: str | None = Field(None, alias="nodeTaintsPolicy")

    topology_key: str | None = Field(None, alias="topologyKey")

    when_unsatisfiable: str | None = Field(None, alias="whenUnsatisfiable")
