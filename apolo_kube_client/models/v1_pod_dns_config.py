from pydantic import BaseModel, Field

from .v1_pod_d_n_s_config_option import V1PodDNSConfigOption


class V1PodDNSConfig(BaseModel):
    nameservers: list[str] | None = Field(None, alias="nameservers")

    options: list[V1PodDNSConfigOption] | None = Field(None, alias="options")

    searches: list[str] | None = Field(None, alias="searches")
