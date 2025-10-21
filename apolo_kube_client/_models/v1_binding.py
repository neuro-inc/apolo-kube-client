from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Binding",)


class V1Binding(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    target: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(default_factory=lambda: V1ObjectReference())
