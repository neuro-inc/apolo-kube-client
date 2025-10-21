from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_pod_disruption_budget_spec import V1PodDisruptionBudgetSpec
from .v1_pod_disruption_budget_status import V1PodDisruptionBudgetStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodDisruptionBudget",)


class V1PodDisruptionBudget(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1PodDisruptionBudgetSpec,
        BeforeValidator(_default_if_none(V1PodDisruptionBudgetSpec)),
    ] = Field(default_factory=lambda: V1PodDisruptionBudgetSpec())

    status: Annotated[
        V1PodDisruptionBudgetStatus,
        BeforeValidator(_default_if_none(V1PodDisruptionBudgetStatus)),
    ] = Field(default_factory=lambda: V1PodDisruptionBudgetStatus())
