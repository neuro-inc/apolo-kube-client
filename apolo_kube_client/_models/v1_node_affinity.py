from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_node_selector import V1NodeSelector
from .v1_preferred_scheduling_term import V1PreferredSchedulingTerm
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeAffinity",)


class V1NodeAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: Annotated[
        list[V1PreferredSchedulingTerm], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="preferredDuringSchedulingIgnoredDuringExecution",
        validation_alias=AliasChoices(
            "preferred_during_scheduling_ignored_during_execution",
            "preferredDuringSchedulingIgnoredDuringExecution",
        ),
        exclude_if=_exclude_if,
    )

    required_during_scheduling_ignored_during_execution: Annotated[
        V1NodeSelector, BeforeValidator(_default_if_none(V1NodeSelector))
    ] = Field(
        default_factory=lambda: V1NodeSelector(),
        serialization_alias="requiredDuringSchedulingIgnoredDuringExecution",
        validation_alias=AliasChoices(
            "required_during_scheduling_ignored_during_execution",
            "requiredDuringSchedulingIgnoredDuringExecution",
        ),
        exclude_if=_exclude_if,
    )
