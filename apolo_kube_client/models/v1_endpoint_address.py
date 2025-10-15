from pydantic import BaseModel, Field

from .v1_object_reference import V1ObjectReference


class V1EndpointAddress(BaseModel):
    hostname: str | None = Field(None, alias="hostname")

    ip: str | None = Field(None, alias="ip")

    node_name: str | None = Field(None, alias="nodeName")

    target_ref: V1ObjectReference | None = Field(None, alias="targetRef")
