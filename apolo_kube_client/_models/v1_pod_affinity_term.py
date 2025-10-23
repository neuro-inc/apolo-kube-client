from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
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

    mismatch_label_keys: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="mismatchLabelKeys",
        validation_alias=AliasChoices("mismatch_label_keys", "mismatchLabelKeys"),
        exclude_if=_exclude_if,
    )

    namespace_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="namespaceSelector",
        validation_alias=AliasChoices("namespace_selector", "namespaceSelector"),
        exclude_if=_exclude_if,
    )

    namespaces: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )

    topology_key: str | None = Field(
        default=None,
        serialization_alias="topologyKey",
        validation_alias=AliasChoices("topology_key", "topologyKey"),
        exclude_if=_exclude_if,
    )
