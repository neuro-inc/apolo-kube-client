from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_flow_schema_spec import V1FlowSchemaSpec
from .v1_flow_schema_status import V1FlowSchemaStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1FlowSchema",)


class V1FlowSchema(ResourceModel):
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
        V1FlowSchemaSpec, BeforeValidator(_default_if_none(V1FlowSchemaSpec))
    ] = Field(default_factory=lambda: V1FlowSchemaSpec(), exclude_if=_exclude_if)

    status: Annotated[
        V1FlowSchemaStatus, BeforeValidator(_default_if_none(V1FlowSchemaStatus))
    ] = Field(default_factory=lambda: V1FlowSchemaStatus(), exclude_if=_exclude_if)
