from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_label_selector import V1LabelSelector
from .v1_persistent_volume_claim import V1PersistentVolumeClaim
from .v1_pod_template_spec import V1PodTemplateSpec
from .v1_stateful_set_ordinals import V1StatefulSetOrdinals
from .v1_stateful_set_persistent_volume_claim_retention_policy import (
    V1StatefulSetPersistentVolumeClaimRetentionPolicy,
)
from .v1_stateful_set_update_strategy import V1StatefulSetUpdateStrategy
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1StatefulSetSpec",)


class V1StatefulSetSpec(BaseModel):
    min_ready_seconds: int | None = Field(
        default=None,
        serialization_alias="minReadySeconds",
        validation_alias=AliasChoices("min_ready_seconds", "minReadySeconds"),
    )

    ordinals: Annotated[
        V1StatefulSetOrdinals, BeforeValidator(_default_if_none(V1StatefulSetOrdinals))
    ] = Field(default_factory=lambda: V1StatefulSetOrdinals())

    persistent_volume_claim_retention_policy: Annotated[
        V1StatefulSetPersistentVolumeClaimRetentionPolicy,
        BeforeValidator(
            _default_if_none(V1StatefulSetPersistentVolumeClaimRetentionPolicy)
        ),
    ] = Field(
        default_factory=lambda: V1StatefulSetPersistentVolumeClaimRetentionPolicy(),
        serialization_alias="persistentVolumeClaimRetentionPolicy",
        validation_alias=AliasChoices(
            "persistent_volume_claim_retention_policy",
            "persistentVolumeClaimRetentionPolicy",
        ),
    )

    pod_management_policy: str | None = Field(
        default=None,
        serialization_alias="podManagementPolicy",
        validation_alias=AliasChoices("pod_management_policy", "podManagementPolicy"),
    )

    replicas: int | None = None

    revision_history_limit: int | None = Field(
        default=None,
        serialization_alias="revisionHistoryLimit",
        validation_alias=AliasChoices("revision_history_limit", "revisionHistoryLimit"),
    )

    selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(default_factory=lambda: V1LabelSelector())

    service_name: str | None = Field(
        default=None,
        serialization_alias="serviceName",
        validation_alias=AliasChoices("service_name", "serviceName"),
    )

    template: Annotated[
        V1PodTemplateSpec, BeforeValidator(_default_if_none(V1PodTemplateSpec))
    ] = Field(default_factory=lambda: V1PodTemplateSpec())

    update_strategy: Annotated[
        V1StatefulSetUpdateStrategy,
        BeforeValidator(_default_if_none(V1StatefulSetUpdateStrategy)),
    ] = Field(
        default_factory=lambda: V1StatefulSetUpdateStrategy(),
        serialization_alias="updateStrategy",
        validation_alias=AliasChoices("update_strategy", "updateStrategy"),
    )

    volume_claim_templates: list[V1PersistentVolumeClaim] = Field(
        default=[],
        serialization_alias="volumeClaimTemplates",
        validation_alias=AliasChoices("volume_claim_templates", "volumeClaimTemplates"),
    )
