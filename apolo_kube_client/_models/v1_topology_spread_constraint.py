from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1TopologySpreadConstraint",)


class V1TopologySpreadConstraint(BaseModel):
    label_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="labelSelector",
        validation_alias=AliasChoices("label_selector", "labelSelector"),
    )

    match_label_keys: list[str] = Field(
        default=[],
        serialization_alias="matchLabelKeys",
        validation_alias=AliasChoices("match_label_keys", "matchLabelKeys"),
    )

    max_skew: int | None = Field(
        default=None,
        serialization_alias="maxSkew",
        validation_alias=AliasChoices("max_skew", "maxSkew"),
    )

    min_domains: int | None = Field(
        default=None,
        serialization_alias="minDomains",
        validation_alias=AliasChoices("min_domains", "minDomains"),
    )

    node_affinity_policy: str | None = Field(
        default=None,
        serialization_alias="nodeAffinityPolicy",
        validation_alias=AliasChoices("node_affinity_policy", "nodeAffinityPolicy"),
    )

    node_taints_policy: str | None = Field(
        default=None,
        serialization_alias="nodeTaintsPolicy",
        validation_alias=AliasChoices("node_taints_policy", "nodeTaintsPolicy"),
    )

    topology_key: str | None = Field(
        default=None,
        serialization_alias="topologyKey",
        validation_alias=AliasChoices("topology_key", "topologyKey"),
    )

    when_unsatisfiable: str | None = Field(
        default=None,
        serialization_alias="whenUnsatisfiable",
        validation_alias=AliasChoices("when_unsatisfiable", "whenUnsatisfiable"),
    )
