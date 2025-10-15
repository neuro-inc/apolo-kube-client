from pydantic import BaseModel, Field

from .v1_for_zone import V1ForZone


class V1EndpointHints(BaseModel):
    for_zones: list[V1ForZone] | None = Field(None, alias="forZones")
