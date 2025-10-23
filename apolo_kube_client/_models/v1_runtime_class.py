from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1_overhead import V1Overhead
from .v1_scheduling import V1Scheduling
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1RuntimeClass",)


class V1RuntimeClass(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    handler: str | None = Field(default=None, exclude_if=_exclude_if)

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    overhead: Annotated[V1Overhead, BeforeValidator(_default_if_none(V1Overhead))] = (
        Field(default_factory=lambda: V1Overhead(), exclude_if=_exclude_if)
    )

    scheduling: Annotated[
        V1Scheduling, BeforeValidator(_default_if_none(V1Scheduling))
    ] = Field(default_factory=lambda: V1Scheduling(), exclude_if=_exclude_if)
