from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, BeforeValidator, Field

from .utils import _collection_if_none
from .v1_scoped_resource_selector_requirement import V1ScopedResourceSelectorRequirement


__all__ = ("V1ScopeSelector",)


class V1ScopeSelector(BaseModel):
    """A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ScopeSelector"

    match_expressions: Annotated[
        list[V1ScopedResourceSelectorRequirement],
        Field(
            alias="matchExpressions",
            description="""A list of scope selector requirements by scope of the resources.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
