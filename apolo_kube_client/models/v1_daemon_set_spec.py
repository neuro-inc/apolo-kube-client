from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_daemon_set_update_strategy import V1DaemonSetUpdateStrategy
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1DaemonSetSpec",)


class V1DaemonSetSpec(BaseModel):
    min_ready_seconds: int | None = Field(None, alias="minReadySeconds")

    revision_history_limit: int | None = Field(None, alias="revisionHistoryLimit")

    selector: V1LabelSelector | None = Field(None, alias="selector")

    template: V1PodTemplateSpec | None = Field(None, alias="template")

    update_strategy: V1DaemonSetUpdateStrategy | None = Field(
        None, alias="updateStrategy"
    )
