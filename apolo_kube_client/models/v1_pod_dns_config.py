from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_pod_dns_config_option import V1PodDNSConfigOption

__all__ = ("V1PodDNSConfig",)


class V1PodDNSConfig(BaseModel):
    nameservers: list[str] | None = Field(None, alias="nameservers")

    options: list[V1PodDNSConfigOption] | None = Field(None, alias="options")

    searches: list[str] | None = Field(None, alias="searches")
