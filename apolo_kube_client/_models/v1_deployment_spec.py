from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_deployment_strategy import V1DeploymentStrategy
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec
from pydantic import BeforeValidator

__all__ = ("V1DeploymentSpec",)


class V1DeploymentSpec(BaseModel):
    """DeploymentSpec is the specification of the desired behavior of the Deployment."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.DeploymentSpec"

    min_ready_seconds: Annotated[
        int | None,
        Field(
            alias="minReadySeconds",
            description="""Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    paused: Annotated[
        bool | None,
        Field(
            description="""Indicates that the deployment is paused.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    progress_deadline_seconds: Annotated[
        int | None,
        Field(
            alias="progressDeadlineSeconds",
            description="""The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    replicas: Annotated[
        int | None,
        Field(
            description="""Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    revision_history_limit: Annotated[
        int | None,
        Field(
            alias="revisionHistoryLimit",
            description="""The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    selector: Annotated[
        V1LabelSelector,
        Field(
            description="""Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels."""
        ),
    ]

    strategy: Annotated[
        V1DeploymentStrategy,
        Field(
            description="""The deployment strategy to use to replace existing pods with new ones.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1DeploymentStrategy)),
    ] = V1DeploymentStrategy()

    template: Annotated[
        V1PodTemplateSpec,
        Field(
            description="""Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always"."""
        ),
    ]
