from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PriorityClass",)


class V1PriorityClass(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    description: str | None = None

    global_default: bool | None = Field(
        default=None,
        serialization_alias="globalDefault",
        validation_alias=AliasChoices("global_default", "globalDefault"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    preemption_policy: str | None = Field(
        default=None,
        serialization_alias="preemptionPolicy",
        validation_alias=AliasChoices("preemption_policy", "preemptionPolicy"),
    )

    value: int | None = None
