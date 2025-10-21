from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_label_selector import V1LabelSelector
from .v1_pod_failure_policy import V1PodFailurePolicy
from .v1_pod_template_spec import V1PodTemplateSpec
from .v1_success_policy import V1SuccessPolicy
from pydantic import BeforeValidator
from typing import Annotated

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

    completions: int | None = None

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

    parallelism: int | None = None

    pod_failure_policy: Annotated[
        V1PodFailurePolicy, BeforeValidator(_default_if_none(V1PodFailurePolicy))
    ] = Field(
        default_factory=lambda: V1PodFailurePolicy(),
        serialization_alias="podFailurePolicy",
        validation_alias=AliasChoices("pod_failure_policy", "podFailurePolicy"),
    )

    pod_replacement_policy: str | None = Field(
        default=None,
        serialization_alias="podReplacementPolicy",
        validation_alias=AliasChoices("pod_replacement_policy", "podReplacementPolicy"),
    )

    selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(default_factory=lambda: V1LabelSelector())

    success_policy: Annotated[
        V1SuccessPolicy, BeforeValidator(_default_if_none(V1SuccessPolicy))
    ] = Field(
        default_factory=lambda: V1SuccessPolicy(),
        serialization_alias="successPolicy",
        validation_alias=AliasChoices("success_policy", "successPolicy"),
    )

    suspend: bool | None = None

    template: Annotated[
        V1PodTemplateSpec, BeforeValidator(_default_if_none(V1PodTemplateSpec))
    ] = Field(default_factory=lambda: V1PodTemplateSpec())

    ttl_seconds_after_finished: int | None = Field(
        default=None,
        serialization_alias="ttlSecondsAfterFinished",
        validation_alias=AliasChoices(
            "ttl_seconds_after_finished", "ttlSecondsAfterFinished"
        ),
    )
