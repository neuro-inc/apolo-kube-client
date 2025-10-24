from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_node_selector_requirement import V1NodeSelectorRequirement
from pydantic import BeforeValidator

__all__ = ("V1NodeSelectorTerm",)


class V1NodeSelectorTerm(BaseModel):
    """A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeSelectorTerm"

    match_expressions: Annotated[
        list[V1NodeSelectorRequirement],
        Field(
            alias="matchExpressions",
            description="""A list of node selector requirements by node's labels.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    match_fields: Annotated[
        list[V1NodeSelectorRequirement],
        Field(
            alias="matchFields",
            description="""A list of node selector requirements by node's fields.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
