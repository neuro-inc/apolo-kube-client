from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodAffinityTerm",)


class V1PodAffinityTerm(BaseModel):
    label_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="labelSelector",
        validation_alias=AliasChoices("label_selector", "labelSelector"),
    )

    match_label_keys: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="matchLabelKeys",
        validation_alias=AliasChoices("match_label_keys", "matchLabelKeys"),
    )

    mismatch_label_keys: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="mismatchLabelKeys",
        validation_alias=AliasChoices("mismatch_label_keys", "mismatchLabelKeys"),
    )

    namespace_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="namespaceSelector",
        validation_alias=AliasChoices("namespace_selector", "namespaceSelector"),
    )

    namespaces: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    topology_key: str | None = Field(
        default=None,
        serialization_alias="topologyKey",
        validation_alias=AliasChoices("topology_key", "topologyKey"),
    )
