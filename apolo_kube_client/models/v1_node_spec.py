from pydantic import AliasChoices, BaseModel, Field
from .v1_node_config_source import V1NodeConfigSource
from .v1_taint import V1Taint

__all__ = ("V1NodeSpec",)


class V1NodeSpec(BaseModel):
    config_source: V1NodeConfigSource = Field(
        default_factory=lambda: V1NodeConfigSource(),
        serialization_alias="configSource",
        validation_alias=AliasChoices("config_source", "configSource"),
    )

    external_id: str | None = Field(
        default=None,
        serialization_alias="externalID",
        validation_alias=AliasChoices("external_id", "externalID"),
    )

    pod_cidr: str | None = Field(
        default=None,
        serialization_alias="podCIDR",
        validation_alias=AliasChoices("pod_cidr", "podCIDR"),
    )

    pod_cid_rs: list[str] = Field(
        default=[],
        serialization_alias="podCIDRs",
        validation_alias=AliasChoices("pod_cid_rs", "podCIDRs"),
    )

    provider_id: str | None = Field(
        default=None,
        serialization_alias="providerID",
        validation_alias=AliasChoices("provider_id", "providerID"),
    )

    taints: list[V1Taint] = []

    unschedulable: bool | None = None
