from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_client_ip_config import V1ClientIPConfig

__all__ = ("V1SessionAffinityConfig",)


class V1SessionAffinityConfig(BaseModel):
    client_ip: V1ClientIPConfig = Field(
        default_factory=lambda: V1ClientIPConfig(), alias="clientIP"
    )
