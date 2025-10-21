from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_api_service_spec import V1APIServiceSpec
from .v1_api_service_status import V1APIServiceStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1APIService",)


class V1APIService(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1APIServiceSpec, BeforeValidator(_default_if_none(V1APIServiceSpec))
    ] = Field(default_factory=lambda: V1APIServiceSpec())

    status: Annotated[
        V1APIServiceStatus, BeforeValidator(_default_if_none(V1APIServiceStatus))
    ] = Field(default_factory=lambda: V1APIServiceStatus())
