from pydantic import AliasChoices, Field
from .base import ListModel
from .base import _default_if_none
from .v1_list_meta import V1ListMeta
from .v2_horizontal_pod_autoscaler import V2HorizontalPodAutoscaler
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2HorizontalPodAutoscalerList",)


class V2HorizontalPodAutoscalerList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V2HorizontalPodAutoscaler] = []

    kind: str | None = None

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta())
    )
