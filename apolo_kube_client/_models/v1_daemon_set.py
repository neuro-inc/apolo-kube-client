from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_daemon_set_spec import V1DaemonSetSpec
from .v1_daemon_set_status import V1DaemonSetStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DaemonSet",)


class V1DaemonSet(ResourceModel):
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
        V1DaemonSetSpec, BeforeValidator(_default_if_none(V1DaemonSetSpec))
    ] = Field(default_factory=lambda: V1DaemonSetSpec(), exclude_if=_exclude_if)

    status: Annotated[
        V1DaemonSetStatus, BeforeValidator(_default_if_none(V1DaemonSetStatus))
    ] = Field(default_factory=lambda: V1DaemonSetStatus(), exclude_if=_exclude_if)
