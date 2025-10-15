from pydantic import BaseModel, Field

from .v1_node_selector import V1NodeSelector
from .v1_preferred_scheduling_term import V1PreferredSchedulingTerm


class V1NodeAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: (
        list[V1PreferredSchedulingTerm] | None
    ) = Field(None, alias="preferredDuringSchedulingIgnoredDuringExecution")

    required_during_scheduling_ignored_during_execution: V1NodeSelector | None = Field(
        None, alias="requiredDuringSchedulingIgnoredDuringExecution"
    )
