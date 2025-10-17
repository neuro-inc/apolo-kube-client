from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_label_selector import V1LabelSelector

__all__ = ("V1PodAffinityTerm",)


class V1PodAffinityTerm(BaseModel):
    label_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="labelSelector",
        validation_alias=AliasChoices("label_selector", "labelSelector"),
    )

    match_label_keys: list[str] = Field(
        default=[],
        serialization_alias="matchLabelKeys",
        validation_alias=AliasChoices("match_label_keys", "matchLabelKeys"),
    )

    mismatch_label_keys: list[str] = Field(
        default=[],
        serialization_alias="mismatchLabelKeys",
        validation_alias=AliasChoices("mismatch_label_keys", "mismatchLabelKeys"),
    )

    namespace_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="namespaceSelector",
        validation_alias=AliasChoices("namespace_selector", "namespaceSelector"),
    )

    namespaces: list[str] = Field(default=[])

    topology_key: str | None = Field(
        default=None,
        serialization_alias="topologyKey",
        validation_alias=AliasChoices("topology_key", "topologyKey"),
    )
