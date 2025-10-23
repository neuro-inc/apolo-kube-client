from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1_scale_spec import V1ScaleSpec
from .v1_scale_status import V1ScaleStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Scale",)


class V1Scale(ResourceModel):
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

    spec: Annotated[V1ScaleSpec, BeforeValidator(_default_if_none(V1ScaleSpec))] = (
        Field(default_factory=lambda: V1ScaleSpec(), exclude_if=_exclude_if)
    )

    status: Annotated[
        V1ScaleStatus, BeforeValidator(_default_if_none(V1ScaleStatus))
    ] = Field(default_factory=lambda: V1ScaleStatus(), exclude_if=_exclude_if)
