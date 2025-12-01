from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none
from .v1_label_selector_requirement import V1LabelSelectorRequirement


__all__ = ("V1LabelSelector",)


class V1LabelSelector(BaseConfiguredModel):
    """A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector"
    )

    match_expressions: Annotated[
        list[V1LabelSelectorRequirement],
        Field(
            alias="matchExpressions",
            description="""matchExpressions is a list of label selector requirements. The requirements are ANDed.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    match_labels: Annotated[
        dict[str, str],
        Field(
            alias="matchLabels",
            description="""matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}
