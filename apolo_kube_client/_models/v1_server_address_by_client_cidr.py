from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ServerAddressByClientCIDR",)


class V1ServerAddressByClientCIDR(BaseModel):
    client_cidr: str | None = Field(
        default=None,
        serialization_alias="clientCIDR",
        validation_alias=AliasChoices("client_cidr", "clientCIDR"),
        exclude_if=_exclude_if,
    )

    server_address: str | None = Field(
        default=None,
        serialization_alias="serverAddress",
        validation_alias=AliasChoices("server_address", "serverAddress"),
        exclude_if=_exclude_if,
    )
