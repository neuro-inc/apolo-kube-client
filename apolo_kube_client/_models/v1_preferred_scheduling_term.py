from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_node_selector_term import V1NodeSelectorTerm

__all__ = ("V1PreferredSchedulingTerm",)


class V1PreferredSchedulingTerm(BaseModel):
    """An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op)."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PreferredSchedulingTerm"

    preference: Annotated[
        V1NodeSelectorTerm,
        Field(
            description="""A node selector term, associated with the corresponding weight."""
        ),
    ]

    weight: Annotated[
        int,
        Field(
            description="""Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100."""
        ),
    ]
