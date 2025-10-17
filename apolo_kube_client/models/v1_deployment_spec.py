from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_deployment_strategy import V1DeploymentStrategy
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1DeploymentSpec",)


class V1DeploymentSpec(BaseModel):
    min_ready_seconds: int | None = Field(
        default_factory=lambda: None, alias="minReadySeconds"
    )

    paused: bool | None = Field(default_factory=lambda: None)

    progress_deadline_seconds: int | None = Field(
        default_factory=lambda: None, alias="progressDeadlineSeconds"
    )

    replicas: int | None = Field(default_factory=lambda: None)

    revision_history_limit: int | None = Field(
        default_factory=lambda: None, alias="revisionHistoryLimit"
    )

    selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())

    strategy: V1DeploymentStrategy = Field(
        default_factory=lambda: V1DeploymentStrategy()
    )

    template: V1PodTemplateSpec = Field(default_factory=lambda: V1PodTemplateSpec())
