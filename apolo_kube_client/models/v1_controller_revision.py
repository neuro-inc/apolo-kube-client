from pydantic import BaseModel, Field

from .object import object
from .v1_object_meta import V1ObjectMeta


class V1ControllerRevision(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    data: object | None = Field(None, alias="data")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    revision: int | None = Field(None, alias="revision")
