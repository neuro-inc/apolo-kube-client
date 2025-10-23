from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    match_label_keys: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="matchLabelKeys",
        validation_alias=AliasChoices("match_label_keys", "matchLabelKeys"),
        exclude_if=_exclude_if,
    )

    max_skew: int | None = Field(
        default=None,
        serialization_alias="maxSkew",
        validation_alias=AliasChoices("max_skew", "maxSkew"),
        exclude_if=_exclude_if,
    )

    min_domains: int | None = Field(
        default=None,
        serialization_alias="minDomains",
        validation_alias=AliasChoices("min_domains", "minDomains"),
        exclude_if=_exclude_if,
    )

    node_affinity_policy: str | None = Field(
        default=None,
        serialization_alias="nodeAffinityPolicy",
        validation_alias=AliasChoices("node_affinity_policy", "nodeAffinityPolicy"),
        exclude_if=_exclude_if,
    )

    node_taints_policy: str | None = Field(
        default=None,
        serialization_alias="nodeTaintsPolicy",
        validation_alias=AliasChoices("node_taints_policy", "nodeTaintsPolicy"),
        exclude_if=_exclude_if,
    )

    topology_key: str | None = Field(
        default=None,
        serialization_alias="topologyKey",
        validation_alias=AliasChoices("topology_key", "topologyKey"),
        exclude_if=_exclude_if,
    )

    when_unsatisfiable: str | None = Field(
        default=None,
        serialization_alias="whenUnsatisfiable",
        validation_alias=AliasChoices("when_unsatisfiable", "whenUnsatisfiable"),
        exclude_if=_exclude_if,
    )
