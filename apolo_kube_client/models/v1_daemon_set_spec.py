from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_daemon_set_update_strategy import V1DaemonSetUpdateStrategy
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1DaemonSetSpec",)


class V1DaemonSetSpec(BaseModel):
    min_ready_seconds: int | None = Field(
        default_factory=lambda: None, alias="minReadySeconds"
    )

    revision_history_limit: int | None = Field(
        default_factory=lambda: None, alias="revisionHistoryLimit"
    )

    selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())

    template: V1PodTemplateSpec = Field(default_factory=lambda: V1PodTemplateSpec())

    update_strategy: V1DaemonSetUpdateStrategy = Field(
        default_factory=lambda: V1DaemonSetUpdateStrategy(), alias="updateStrategy"
    )
