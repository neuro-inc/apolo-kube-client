from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector
from .v1_pod_failure_policy import V1PodFailurePolicy
from .v1_pod_template_spec import V1PodTemplateSpec
from .v1_success_policy import V1SuccessPolicy

__all__ = ("V1JobSpec",)


class V1JobSpec(BaseModel):
    active_deadline_seconds: int | None = Field(
        default_factory=lambda: None, alias="activeDeadlineSeconds"
    )

    backoff_limit: int | None = Field(
        default_factory=lambda: None, alias="backoffLimit"
    )

    backoff_limit_per_index: int | None = Field(
        default_factory=lambda: None, alias="backoffLimitPerIndex"
    )

    completion_mode: str | None = Field(
        default_factory=lambda: None, alias="completionMode"
    )

    completions: int | None = Field(default_factory=lambda: None, alias="completions")

    managed_by: str | None = Field(default_factory=lambda: None, alias="managedBy")

    manual_selector: bool | None = Field(
        default_factory=lambda: None, alias="manualSelector"
    )

    max_failed_indexes: int | None = Field(
        default_factory=lambda: None, alias="maxFailedIndexes"
    )

    parallelism: int | None = Field(default_factory=lambda: None, alias="parallelism")

    pod_failure_policy: V1PodFailurePolicy = Field(
        default_factory=lambda: V1PodFailurePolicy(), alias="podFailurePolicy"
    )

    pod_replacement_policy: str | None = Field(
        default_factory=lambda: None, alias="podReplacementPolicy"
    )

    selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="selector"
    )

    success_policy: V1SuccessPolicy = Field(
        default_factory=lambda: V1SuccessPolicy(), alias="successPolicy"
    )

    suspend: bool | None = Field(default_factory=lambda: None, alias="suspend")

    template: V1PodTemplateSpec = Field(
        default_factory=lambda: V1PodTemplateSpec(), alias="template"
    )

    ttl_seconds_after_finished: int | None = Field(
        default_factory=lambda: None, alias="ttlSecondsAfterFinished"
    )
