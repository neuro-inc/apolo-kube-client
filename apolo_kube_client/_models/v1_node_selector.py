from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_node_selector_term import V1NodeSelectorTerm

__all__ = ("V1NodeSelector",)


class V1NodeSelector(BaseModel):
    """A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeSelector"

    node_selector_terms: Annotated[
        list[V1NodeSelectorTerm],
        Field(
            alias="nodeSelectorTerms",
            description="""Required. A list of node selector terms. The terms are ORed.""",
        ),
    ]
