from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1beta1_ip_address_spec import V1beta1IPAddressSpec

__all__ = ("V1beta1IPAddress",)


class V1beta1IPAddress(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1beta1IPAddressSpec = Field(default_factory=lambda: V1beta1IPAddressSpec())
