from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_config_map_node_config_source import V1ConfigMapNodeConfigSource

__all__ = ("V1NodeConfigSource",)


class V1NodeConfigSource(BaseModel):
    """NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeConfigSource"

    config_map: Annotated[
        V1ConfigMapNodeConfigSource | None,
        Field(
            alias="configMap",
            description="""ConfigMap is a reference to a Node's ConfigMap""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
