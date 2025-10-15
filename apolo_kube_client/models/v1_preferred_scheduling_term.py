from pydantic import BaseModel, Field

from .v1_node_selector_term import V1NodeSelectorTerm


class V1PreferredSchedulingTerm(BaseModel):
    preference: V1NodeSelectorTerm | None = Field(None, alias="preference")

    weight: int | None = Field(None, alias="weight")
