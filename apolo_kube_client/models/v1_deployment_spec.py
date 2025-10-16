from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_deployment_strategy import V1DeploymentStrategy
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1DeploymentSpec",)


class V1DeploymentSpec(BaseModel):
    min_ready_seconds: int | None = Field(None, alias="minReadySeconds")

    paused: bool | None = Field(None, alias="paused")

    progress_deadline_seconds: int | None = Field(None, alias="progressDeadlineSeconds")

    replicas: int | None = Field(None, alias="replicas")

    revision_history_limit: int | None = Field(None, alias="revisionHistoryLimit")

    selector: V1LabelSelector | None = Field(None, alias="selector")

    strategy: V1DeploymentStrategy | None = Field(None, alias="strategy")

    template: V1PodTemplateSpec | None = Field(None, alias="template")
