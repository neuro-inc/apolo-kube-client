from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_ip_address import V1IPAddress
from .v1_list_meta import V1ListMeta

__all__ = ("V1IPAddressList",)


class V1IPAddressList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1IPAddress] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
