from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_label_selector import V1LabelSelector
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodDisruptionBudgetSpec",)


class V1PodDisruptionBudgetSpec(BaseModel):
    max_unavailable: JsonType = Field(
        default={},
        serialization_alias="maxUnavailable",
        validation_alias=AliasChoices("max_unavailable", "maxUnavailable"),
        exclude_if=_exclude_if,
    )

    min_available: JsonType = Field(
        default={},
        serialization_alias="minAvailable",
        validation_alias=AliasChoices("min_available", "minAvailable"),
        exclude_if=_exclude_if,
    )

    selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(default_factory=lambda: V1LabelSelector(), exclude_if=_exclude_if)

    unhealthy_pod_eviction_policy: str | None = Field(
        default=None,
        serialization_alias="unhealthyPodEvictionPolicy",
        validation_alias=AliasChoices(
            "unhealthy_pod_eviction_policy", "unhealthyPodEvictionPolicy"
        ),
        exclude_if=_exclude_if,
    )
