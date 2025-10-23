from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    backoff_limit: int | None = Field(
        default=None,
        serialization_alias="backoffLimit",
        validation_alias=AliasChoices("backoff_limit", "backoffLimit"),
        exclude_if=_exclude_if,
    )

    backoff_limit_per_index: int | None = Field(
        default=None,
        serialization_alias="backoffLimitPerIndex",
        validation_alias=AliasChoices(
            "backoff_limit_per_index", "backoffLimitPerIndex"
        ),
        exclude_if=_exclude_if,
    )

    completion_mode: str | None = Field(
        default=None,
        serialization_alias="completionMode",
        validation_alias=AliasChoices("completion_mode", "completionMode"),
        exclude_if=_exclude_if,
    )

    completions: int | None = Field(default=None, exclude_if=_exclude_if)

    managed_by: str | None = Field(
        default=None,
        serialization_alias="managedBy",
        validation_alias=AliasChoices("managed_by", "managedBy"),
        exclude_if=_exclude_if,
    )

    manual_selector: bool | None = Field(
        default=None,
        serialization_alias="manualSelector",
        validation_alias=AliasChoices("manual_selector", "manualSelector"),
        exclude_if=_exclude_if,
    )

    max_failed_indexes: int | None = Field(
        default=None,
        serialization_alias="maxFailedIndexes",
        validation_alias=AliasChoices("max_failed_indexes", "maxFailedIndexes"),
        exclude_if=_exclude_if,
    )

    parallelism: int | None = Field(default=None, exclude_if=_exclude_if)

    pod_failure_policy: Annotated[
        V1PodFailurePolicy, BeforeValidator(_default_if_none(V1PodFailurePolicy))
    ] = Field(
        default_factory=lambda: V1PodFailurePolicy(),
        serialization_alias="podFailurePolicy",
        validation_alias=AliasChoices("pod_failure_policy", "podFailurePolicy"),
        exclude_if=_exclude_if,
    )

    pod_replacement_policy: str | None = Field(
        default=None,
        serialization_alias="podReplacementPolicy",
        validation_alias=AliasChoices("pod_replacement_policy", "podReplacementPolicy"),
        exclude_if=_exclude_if,
    )

    selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(default_factory=lambda: V1LabelSelector(), exclude_if=_exclude_if)

    success_policy: Annotated[
        V1SuccessPolicy, BeforeValidator(_default_if_none(V1SuccessPolicy))
    ] = Field(
        default_factory=lambda: V1SuccessPolicy(),
        serialization_alias="successPolicy",
        validation_alias=AliasChoices("success_policy", "successPolicy"),
        exclude_if=_exclude_if,
    )

    suspend: bool | None = Field(default=None, exclude_if=_exclude_if)

    template: Annotated[
        V1PodTemplateSpec, BeforeValidator(_default_if_none(V1PodTemplateSpec))
    ] = Field(default_factory=lambda: V1PodTemplateSpec(), exclude_if=_exclude_if)

    ttl_seconds_after_finished: int | None = Field(
        default=None,
        serialization_alias="ttlSecondsAfterFinished",
        validation_alias=AliasChoices(
            "ttl_seconds_after_finished", "ttlSecondsAfterFinished"
        ),
        exclude_if=_exclude_if,
    )
