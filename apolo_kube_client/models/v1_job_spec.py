from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector
from .v1_pod_failure_policy import V1PodFailurePolicy
from .v1_pod_template_spec import V1PodTemplateSpec
from .v1_success_policy import V1SuccessPolicy


class V1JobSpec(BaseModel):
    active_deadline_seconds: int | None = Field(None, alias="activeDeadlineSeconds")

    backoff_limit: int | None = Field(None, alias="backoffLimit")

    backoff_limit_per_index: int | None = Field(None, alias="backoffLimitPerIndex")

    completion_mode: str | None = Field(None, alias="completionMode")

    completions: int | None = Field(None, alias="completions")

    managed_by: str | None = Field(None, alias="managedBy")

    manual_selector: bool | None = Field(None, alias="manualSelector")

    max_failed_indexes: int | None = Field(None, alias="maxFailedIndexes")

    parallelism: int | None = Field(None, alias="parallelism")

    pod_failure_policy: V1PodFailurePolicy | None = Field(
        None, alias="podFailurePolicy"
    )

    pod_replacement_policy: str | None = Field(None, alias="podReplacementPolicy")

    selector: V1LabelSelector | None = Field(None, alias="selector")

    success_policy: V1SuccessPolicy | None = Field(None, alias="successPolicy")

    suspend: bool | None = Field(None, alias="suspend")

    template: V1PodTemplateSpec | None = Field(None, alias="template")

    ttl_seconds_after_finished: int | None = Field(
        None, alias="ttlSecondsAfterFinished"
    )
