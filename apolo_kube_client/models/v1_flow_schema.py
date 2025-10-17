from pydantic import AliasChoices, BaseModel, Field
from .v1_flow_schema_spec import V1FlowSchemaSpec
from .v1_flow_schema_status import V1FlowSchemaStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1FlowSchema",)


class V1FlowSchema(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1FlowSchemaSpec = Field(default_factory=lambda: V1FlowSchemaSpec())

    status: V1FlowSchemaStatus = Field(default_factory=lambda: V1FlowSchemaStatus())
