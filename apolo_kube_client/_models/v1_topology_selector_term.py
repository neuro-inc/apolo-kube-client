from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_topology_selector_label_requirement import V1TopologySelectorLabelRequirement
from pydantic import BeforeValidator

__all__ = ("V1TopologySelectorTerm",)


class V1TopologySelectorTerm(BaseModel):
    """A topology selector term represents the result of label queries. A null or empty topology selector term matches no objects. The requirements of them are ANDed. It provides a subset of functionality as NodeSelectorTerm. This is an alpha feature and may change in the future."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.TopologySelectorTerm"

    match_label_expressions: Annotated[
        list[V1TopologySelectorLabelRequirement],
        Field(
            alias="matchLabelExpressions",
            description="""A list of topology selector requirements by labels.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
