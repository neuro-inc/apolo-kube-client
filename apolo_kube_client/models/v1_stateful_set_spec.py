from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector
from .v1_persistent_volume_claim import V1PersistentVolumeClaim
from .v1_pod_template_spec import V1PodTemplateSpec
from .v1_stateful_set_ordinals import V1StatefulSetOrdinals
from .v1_stateful_set_persistent_volume_claim_retention_policy import (
    V1StatefulSetPersistentVolumeClaimRetentionPolicy,
)
from .v1_stateful_set_update_strategy import V1StatefulSetUpdateStrategy


class V1StatefulSetSpec(BaseModel):
    min_ready_seconds: int | None = Field(None, alias="minReadySeconds")

    ordinals: V1StatefulSetOrdinals | None = Field(None, alias="ordinals")

    persistent_volume_claim_retention_policy: (
        V1StatefulSetPersistentVolumeClaimRetentionPolicy | None
    ) = Field(None, alias="persistentVolumeClaimRetentionPolicy")

    pod_management_policy: str | None = Field(None, alias="podManagementPolicy")

    replicas: int | None = Field(None, alias="replicas")

    revision_history_limit: int | None = Field(None, alias="revisionHistoryLimit")

    selector: V1LabelSelector | None = Field(None, alias="selector")

    service_name: str | None = Field(None, alias="serviceName")

    template: V1PodTemplateSpec | None = Field(None, alias="template")

    update_strategy: V1StatefulSetUpdateStrategy | None = Field(
        None, alias="updateStrategy"
    )

    volume_claim_templates: list[V1PersistentVolumeClaim] | None = Field(
        None, alias="volumeClaimTemplates"
    )
