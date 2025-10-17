from pydantic import AliasChoices, BaseModel, Field
from .v1_deployment_strategy import V1DeploymentStrategy
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1DeploymentSpec",)


class V1DeploymentSpec(BaseModel):
    min_ready_seconds: int | None = Field(
        default=None,
        serialization_alias="minReadySeconds",
        validation_alias=AliasChoices("min_ready_seconds", "minReadySeconds"),
    )

    paused: bool | None = None

    progress_deadline_seconds: int | None = Field(
        default=None,
        serialization_alias="progressDeadlineSeconds",
        validation_alias=AliasChoices(
            "progress_deadline_seconds", "progressDeadlineSeconds"
        ),
    )

    replicas: int | None = None

    revision_history_limit: int | None = Field(
        default=None,
        serialization_alias="revisionHistoryLimit",
        validation_alias=AliasChoices("revision_history_limit", "revisionHistoryLimit"),
    )

    selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())

    strategy: V1DeploymentStrategy = Field(
        default_factory=lambda: V1DeploymentStrategy()
    )

    template: V1PodTemplateSpec = Field(default_factory=lambda: V1PodTemplateSpec())
