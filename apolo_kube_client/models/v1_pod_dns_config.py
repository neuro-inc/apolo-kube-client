from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_pod_dns_config_option import V1PodDNSConfigOption

__all__ = ("V1PodDNSConfig",)


class V1PodDNSConfig(BaseModel):
    nameservers: list[str] = Field(default_factory=lambda: [])

    options: list[V1PodDNSConfigOption] = Field(default_factory=lambda: [])

    searches: list[str] = Field(default_factory=lambda: [])
