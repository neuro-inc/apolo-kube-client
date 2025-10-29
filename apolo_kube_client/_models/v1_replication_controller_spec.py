from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_pod_template_spec import V1PodTemplateSpec
from pydantic import BeforeValidator

__all__ = ("V1ReplicationControllerSpec",)


class V1ReplicationControllerSpec(BaseModel):
    """ReplicationControllerSpec is the specification of a replication controller."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.ReplicationControllerSpec"
    )

    min_ready_seconds: Annotated[
        int | None,
        Field(
            alias="minReadySeconds",
            description="""Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    replicas: Annotated[
        int | None,
        Field(
            description="""Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    selector: Annotated[
        dict[str, str],
        Field(
            description="""Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    template: Annotated[
        V1PodTemplateSpec,
        Field(
            description="""Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1PodTemplateSpec)),
    ] = V1PodTemplateSpec()
