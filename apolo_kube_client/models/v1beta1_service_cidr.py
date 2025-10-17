from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1beta1_service_cidr_spec import V1beta1ServiceCIDRSpec
from .v1beta1_service_cidr_status import V1beta1ServiceCIDRStatus

__all__ = ("V1beta1ServiceCIDR",)


class V1beta1ServiceCIDR(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1beta1ServiceCIDRSpec = Field(
        default_factory=lambda: V1beta1ServiceCIDRSpec()
    )

    status: V1beta1ServiceCIDRStatus = Field(
        default_factory=lambda: V1beta1ServiceCIDRStatus()
    )
