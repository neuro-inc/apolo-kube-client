from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_daemon_set_update_strategy import V1DaemonSetUpdateStrategy
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec
from pydantic import BeforeValidator

__all__ = ("V1DaemonSetSpec",)


class V1DaemonSetSpec(BaseModel):
    """DaemonSetSpec is the specification of a daemon set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.DaemonSetSpec"

    min_ready_seconds: Annotated[
        int | None,
        Field(
            alias="minReadySeconds",
            description="""The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    revision_history_limit: Annotated[
        int | None,
        Field(
            alias="revisionHistoryLimit",
            description="""The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    selector: Annotated[
        V1LabelSelector,
        Field(
            description="""A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors"""
        ),
    ]

    template: Annotated[
        V1PodTemplateSpec,
        Field(
            description="""An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template"""
        ),
    ]

    update_strategy: Annotated[
        V1DaemonSetUpdateStrategy,
        Field(
            alias="updateStrategy",
            description="""An update strategy to replace existing DaemonSet pods with new pods.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1DaemonSetUpdateStrategy)),
    ] = V1DaemonSetUpdateStrategy()
