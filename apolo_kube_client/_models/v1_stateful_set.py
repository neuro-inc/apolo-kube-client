from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1_stateful_set_spec import V1StatefulSetSpec
from .v1_stateful_set_status import V1StatefulSetStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1StatefulSet",)


class V1StatefulSet(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[
        V1StatefulSetSpec, BeforeValidator(_default_if_none(V1StatefulSetSpec))
    ] = Field(default_factory=lambda: V1StatefulSetSpec(), exclude_if=_exclude_if)

    status: Annotated[
        V1StatefulSetStatus, BeforeValidator(_default_if_none(V1StatefulSetStatus))
    ] = Field(default_factory=lambda: V1StatefulSetStatus(), exclude_if=_exclude_if)
