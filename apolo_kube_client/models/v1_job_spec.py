from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_label_selector import V1LabelSelector
from .v1_pod_failure_policy import V1PodFailurePolicy
from .v1_pod_template_spec import V1PodTemplateSpec
from .v1_success_policy import V1SuccessPolicy

__all__ = ("V1JobSpec",)


class V1JobSpec(BaseModel):
    active_deadline_seconds: int | None = Field(
        default=None,
        serialization_alias="activeDeadlineSeconds",
        validation_alias=AliasChoices(
            "active_deadline_seconds", "activeDeadlineSeconds"
        ),
    )

    backoff_limit: int | None = Field(
        default=None,
        serialization_alias="backoffLimit",
        validation_alias=AliasChoices("backoff_limit", "backoffLimit"),
    )

    backoff_limit_per_index: int | None = Field(
        default=None,
        serialization_alias="backoffLimitPerIndex",
        validation_alias=AliasChoices(
            "backoff_limit_per_index", "backoffLimitPerIndex"
        ),
    )

    completion_mode: str | None = Field(
        default=None,
        serialization_alias="completionMode",
        validation_alias=AliasChoices("completion_mode", "completionMode"),
    )

    completions: int | None = Field(default=None)

    managed_by: str | None = Field(
        default=None,
        serialization_alias="managedBy",
        validation_alias=AliasChoices("managed_by", "managedBy"),
    )

    manual_selector: bool | None = Field(
        default=None,
        serialization_alias="manualSelector",
        validation_alias=AliasChoices("manual_selector", "manualSelector"),
    )

    max_failed_indexes: int | None = Field(
        default=None,
        serialization_alias="maxFailedIndexes",
        validation_alias=AliasChoices("max_failed_indexes", "maxFailedIndexes"),
    )

    parallelism: int | None = Field(default=None)

    pod_failure_policy: V1PodFailurePolicy = Field(
        default_factory=lambda: V1PodFailurePolicy(),
        serialization_alias="podFailurePolicy",
        validation_alias=AliasChoices("pod_failure_policy", "podFailurePolicy"),
    )

    pod_replacement_policy: str | None = Field(
        default=None,
        serialization_alias="podReplacementPolicy",
        validation_alias=AliasChoices("pod_replacement_policy", "podReplacementPolicy"),
    )

    selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())

    success_policy: V1SuccessPolicy = Field(
        default_factory=lambda: V1SuccessPolicy(),
        serialization_alias="successPolicy",
        validation_alias=AliasChoices("success_policy", "successPolicy"),
    )

    suspend: bool | None = Field(default=None)

    template: V1PodTemplateSpec = Field(default_factory=lambda: V1PodTemplateSpec())

    ttl_seconds_after_finished: int | None = Field(
        default=None,
        serialization_alias="ttlSecondsAfterFinished",
        validation_alias=AliasChoices(
            "ttl_seconds_after_finished", "ttlSecondsAfterFinished"
        ),
    )
