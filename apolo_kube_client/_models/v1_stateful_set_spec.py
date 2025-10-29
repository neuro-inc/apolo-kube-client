from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_label_selector import V1LabelSelector
from .v1_persistent_volume_claim import V1PersistentVolumeClaim
from .v1_pod_template_spec import V1PodTemplateSpec
from .v1_stateful_set_ordinals import V1StatefulSetOrdinals
from .v1_stateful_set_persistent_volume_claim_retention_policy import (
    V1StatefulSetPersistentVolumeClaimRetentionPolicy,
)
from .v1_stateful_set_update_strategy import V1StatefulSetUpdateStrategy
from pydantic import BeforeValidator

__all__ = ("V1StatefulSetSpec",)


class V1StatefulSetSpec(BaseModel):
    """A StatefulSetSpec is the specification of a StatefulSet."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.StatefulSetSpec"

    min_ready_seconds: Annotated[
        int | None,
        Field(
            alias="minReadySeconds",
            description="""Minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    ordinals: Annotated[
        V1StatefulSetOrdinals,
        Field(
            description="""ordinals controls the numbering of replica indices in a StatefulSet. The default ordinals behavior assigns a "0" index to the first replica and increments the index by one for each additional replica requested.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1StatefulSetOrdinals)),
    ] = V1StatefulSetOrdinals()

    persistent_volume_claim_retention_policy: Annotated[
        V1StatefulSetPersistentVolumeClaimRetentionPolicy,
        Field(
            alias="persistentVolumeClaimRetentionPolicy",
            description="""persistentVolumeClaimRetentionPolicy describes the lifecycle of persistent volume claims created from volumeClaimTemplates. By default, all persistent volume claims are created as needed and retained until manually deleted. This policy allows the lifecycle to be altered, for example by deleting persistent volume claims when their stateful set is deleted, or when their pod is scaled down.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(
            _default_if_none(V1StatefulSetPersistentVolumeClaimRetentionPolicy)
        ),
    ] = V1StatefulSetPersistentVolumeClaimRetentionPolicy()

    pod_management_policy: Annotated[
        str | None,
        Field(
            alias="podManagementPolicy",
            description="""podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    replicas: Annotated[
        int | None,
        Field(
            description="""replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    revision_history_limit: Annotated[
        int | None,
        Field(
            alias="revisionHistoryLimit",
            description="""revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    selector: Annotated[
        V1LabelSelector,
        Field(
            description="""selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors"""
        ),
    ]

    service_name: Annotated[
        str | None,
        Field(
            alias="serviceName",
            description="""serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is managed by the StatefulSet controller.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    template: Annotated[
        V1PodTemplateSpec,
        Field(
            description="""template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet. Each pod will be named with the format <statefulsetname>-<podindex>. For example, a pod in a StatefulSet named "web" with index number "3" would be named "web-3". The only allowed template.spec.restartPolicy value is "Always"."""
        ),
    ]

    update_strategy: Annotated[
        V1StatefulSetUpdateStrategy,
        Field(
            alias="updateStrategy",
            description="""updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1StatefulSetUpdateStrategy)),
    ] = V1StatefulSetUpdateStrategy()

    volume_claim_templates: Annotated[
        list[V1PersistentVolumeClaim],
        Field(
            alias="volumeClaimTemplates",
            description="""volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
