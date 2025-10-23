from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_node_config_source import V1NodeConfigSource
from .v1_taint import V1Taint
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeSpec",)


class V1NodeSpec(BaseModel):
    config_source: Annotated[
        V1NodeConfigSource, BeforeValidator(_default_if_none(V1NodeConfigSource))
    ] = Field(
        default_factory=lambda: V1NodeConfigSource(),
        serialization_alias="configSource",
        validation_alias=AliasChoices("config_source", "configSource"),
        exclude_if=_exclude_if,
    )

    external_id: str | None = Field(
        default=None,
        serialization_alias="externalID",
        validation_alias=AliasChoices("external_id", "externalID"),
        exclude_if=_exclude_if,
    )

    pod_cidr: str | None = Field(
        default=None,
        serialization_alias="podCIDR",
        validation_alias=AliasChoices("pod_cidr", "podCIDR"),
        exclude_if=_exclude_if,
    )

    pod_cid_rs: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="podCIDRs",
            validation_alias=AliasChoices("pod_cid_rs", "podCIDRs"),
            exclude_if=_exclude_if,
        )
    )

    provider_id: str | None = Field(
        default=None,
        serialization_alias="providerID",
        validation_alias=AliasChoices("provider_id", "providerID"),
        exclude_if=_exclude_if,
    )

    taints: Annotated[list[V1Taint], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )

    unschedulable: bool | None = Field(default=None, exclude_if=_exclude_if)
