from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ReplicaSetSpec",)


class V1ReplicaSetSpec(BaseModel):
    min_ready_seconds: int | None = Field(
        default=None,
        serialization_alias="minReadySeconds",
        validation_alias=AliasChoices("min_ready_seconds", "minReadySeconds"),
        exclude_if=_exclude_if,
    )

    replicas: int | None = Field(default=None, exclude_if=_exclude_if)

    selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(default_factory=lambda: V1LabelSelector(), exclude_if=_exclude_if)

    template: Annotated[
        V1PodTemplateSpec, BeforeValidator(_default_if_none(V1PodTemplateSpec))
    ] = Field(default_factory=lambda: V1PodTemplateSpec(), exclude_if=_exclude_if)
