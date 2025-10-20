from pydantic import BaseModel
from .v1_pod_dns_config_option import V1PodDNSConfigOption

__all__ = ("V1PodDNSConfig",)


class V1PodDNSConfig(BaseModel):
    nameservers: list[str] = []

    options: list[V1PodDNSConfigOption] = []

    searches: list[str] = []
