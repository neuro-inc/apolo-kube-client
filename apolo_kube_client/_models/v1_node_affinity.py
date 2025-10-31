from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_node_selector import V1NodeSelector
from .v1_preferred_scheduling_term import V1PreferredSchedulingTerm
from pydantic import BeforeValidator

__all__ = ("V1NodeAffinity",)


class V1NodeAffinity(BaseModel):
    """Node affinity is a group of node affinity scheduling rules."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeAffinity"

    preferred_during_scheduling_ignored_during_execution: Annotated[
        list[V1PreferredSchedulingTerm],
        Field(
            alias="preferredDuringSchedulingIgnoredDuringExecution",
            description="""The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    required_during_scheduling_ignored_during_execution: Annotated[
        V1NodeSelector | None,
        Field(
            alias="requiredDuringSchedulingIgnoredDuringExecution",
            description="""If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
