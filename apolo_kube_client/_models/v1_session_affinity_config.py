from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_client_ip_config import V1ClientIPConfig
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SessionAffinityConfig",)


class V1SessionAffinityConfig(BaseModel):
    client_ip: Annotated[
        V1ClientIPConfig, BeforeValidator(_default_if_none(V1ClientIPConfig))
    ] = Field(
        default_factory=lambda: V1ClientIPConfig(),
        serialization_alias="clientIP",
        validation_alias=AliasChoices("client_ip", "clientIP"),
        exclude_if=_exclude_if,
    )
