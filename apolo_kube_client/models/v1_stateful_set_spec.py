from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector
from .v1_persistent_volume_claim import V1PersistentVolumeClaim
from .v1_pod_template_spec import V1PodTemplateSpec
from .v1_stateful_set_ordinals import V1StatefulSetOrdinals
from .v1_stateful_set_persistent_volume_claim_retention_policy import (
    V1StatefulSetPersistentVolumeClaimRetentionPolicy,
)
from .v1_stateful_set_update_strategy import V1StatefulSetUpdateStrategy

__all__ = ("V1StatefulSetSpec",)


class V1StatefulSetSpec(BaseModel):
    min_ready_seconds: int | None = Field(
        default_factory=lambda: None, alias="minReadySeconds"
    )

    ordinals: V1StatefulSetOrdinals = Field(
        default_factory=lambda: V1StatefulSetOrdinals(), alias="ordinals"
    )

    persistent_volume_claim_retention_policy: V1StatefulSetPersistentVolumeClaimRetentionPolicy = Field(
        default_factory=lambda: V1StatefulSetPersistentVolumeClaimRetentionPolicy(),
        alias="persistentVolumeClaimRetentionPolicy",
    )

    pod_management_policy: str | None = Field(
        default_factory=lambda: None, alias="podManagementPolicy"
    )

    replicas: int | None = Field(default_factory=lambda: None, alias="replicas")

    revision_history_limit: int | None = Field(
        default_factory=lambda: None, alias="revisionHistoryLimit"
    )

    selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="selector"
    )

    service_name: str | None = Field(default_factory=lambda: None, alias="serviceName")

    template: V1PodTemplateSpec = Field(
        default_factory=lambda: V1PodTemplateSpec(), alias="template"
    )

    update_strategy: V1StatefulSetUpdateStrategy = Field(
        default_factory=lambda: V1StatefulSetUpdateStrategy(), alias="updateStrategy"
    )

    volume_claim_templates: list[V1PersistentVolumeClaim] = Field(
        default_factory=lambda: [], alias="volumeClaimTemplates"
    )
