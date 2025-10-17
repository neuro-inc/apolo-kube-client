from pydantic import AliasChoices, BaseModel, Field
from .v1_node_spec import V1NodeSpec
from .v1_node_status import V1NodeStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Node",)


class V1Node(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1NodeSpec = Field(default_factory=lambda: V1NodeSpec())

    status: V1NodeStatus = Field(default_factory=lambda: V1NodeStatus())
