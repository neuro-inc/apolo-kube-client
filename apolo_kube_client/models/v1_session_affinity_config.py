from pydantic import BaseModel, Field

from .v1_client_i_p_config import V1ClientIPConfig


class V1SessionAffinityConfig(BaseModel):
    client_ip: V1ClientIPConfig | None = Field(None, alias="clientIP")
