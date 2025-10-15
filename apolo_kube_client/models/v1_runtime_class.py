from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_overhead import V1Overhead
from .v1_scheduling import V1Scheduling


class V1RuntimeClass(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    handler: str | None = Field(None, alias="handler")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    overhead: V1Overhead | None = Field(None, alias="overhead")

    scheduling: V1Scheduling | None = Field(None, alias="scheduling")
