from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_pod_disruption_budget_spec import V1PodDisruptionBudgetSpec
from .v1_pod_disruption_budget_status import V1PodDisruptionBudgetStatus

__all__ = ("V1PodDisruptionBudget",)


class V1PodDisruptionBudget(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1PodDisruptionBudgetSpec = Field(
        default_factory=lambda: V1PodDisruptionBudgetSpec()
    )

    status: V1PodDisruptionBudgetStatus = Field(
        default_factory=lambda: V1PodDisruptionBudgetStatus()
    )
