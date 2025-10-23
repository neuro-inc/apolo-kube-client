from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_node_selector_term import V1NodeSelectorTerm
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PreferredSchedulingTerm",)


class V1PreferredSchedulingTerm(BaseModel):
    preference: Annotated[
        V1NodeSelectorTerm, BeforeValidator(_default_if_none(V1NodeSelectorTerm))
    ] = Field(default_factory=lambda: V1NodeSelectorTerm(), exclude_if=_exclude_if)

    weight: int | None = Field(default=None, exclude_if=_exclude_if)
