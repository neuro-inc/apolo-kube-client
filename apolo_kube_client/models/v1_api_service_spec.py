from __future__ import annotations
from pydantic import BaseModel, Field
from .apiregistration_v1_service_reference import ApiregistrationV1ServiceReference

__all__ = ("V1APIServiceSpec",)


class V1APIServiceSpec(BaseModel):
    ca_bundle: str | None = Field(default_factory=lambda: None, alias="caBundle")

    group: str | None = Field(default_factory=lambda: None)

    group_priority_minimum: int | None = Field(
        default_factory=lambda: None, alias="groupPriorityMinimum"
    )

    insecure_skip_tls_verify: bool | None = Field(
        default_factory=lambda: None, alias="insecureSkipTLSVerify"
    )

    service: ApiregistrationV1ServiceReference = Field(
        default_factory=lambda: ApiregistrationV1ServiceReference()
    )

    version: str | None = Field(default_factory=lambda: None)

    version_priority: int | None = Field(
        default_factory=lambda: None, alias="versionPriority"
    )
