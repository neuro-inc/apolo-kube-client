from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_deployment_strategy import V1DeploymentStrategy
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec
from pydantic import BeforeValidator
from typing import Annotated

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

    selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(default_factory=lambda: V1LabelSelector())

    strategy: Annotated[
        V1DeploymentStrategy, BeforeValidator(_default_if_none(V1DeploymentStrategy))
    ] = Field(default_factory=lambda: V1DeploymentStrategy())

    template: Annotated[
        V1PodTemplateSpec, BeforeValidator(_default_if_none(V1PodTemplateSpec))
    ] = Field(default_factory=lambda: V1PodTemplateSpec())
