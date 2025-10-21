from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_resource_quota_spec import V1ResourceQuotaSpec
from .v1_resource_quota_status import V1ResourceQuotaStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceQuota",)


class V1ResourceQuota(ResourceModel):
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
        V1ResourceQuotaSpec, BeforeValidator(_default_if_none(V1ResourceQuotaSpec))
    ] = Field(default_factory=lambda: V1ResourceQuotaSpec())

    status: Annotated[
        V1ResourceQuotaStatus, BeforeValidator(_default_if_none(V1ResourceQuotaStatus))
    ] = Field(default_factory=lambda: V1ResourceQuotaStatus())
