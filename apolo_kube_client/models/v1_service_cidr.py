from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_service_cidr_spec import V1ServiceCIDRSpec
from .v1_service_cidr_status import V1ServiceCIDRStatus

__all__ = ("V1ServiceCIDR",)


class V1ServiceCIDR(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1ServiceCIDRSpec = Field(default_factory=lambda: V1ServiceCIDRSpec())

    status: V1ServiceCIDRStatus = Field(default_factory=lambda: V1ServiceCIDRStatus())
