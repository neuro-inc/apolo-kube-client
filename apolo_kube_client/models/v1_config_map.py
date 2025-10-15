from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta


class V1ConfigMap(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    binary_data: dict(str, str) | None = Field(None, alias="binaryData")

    data: dict(str, str) | None = Field(None, alias="data")

    immutable: bool | None = Field(None, alias="immutable")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")
