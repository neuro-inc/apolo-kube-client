from __future__ import annotations

from pydantic import BaseModel, Field

from .apiregistration_v1_service_reference import ApiregistrationV1ServiceReference

__all__ = ("V1APIServiceSpec",)


class V1APIServiceSpec(BaseModel):
    ca_bundle: str | None = Field(None, alias="caBundle")

    group: str | None = Field(None, alias="group")

    group_priority_minimum: int | None = Field(None, alias="groupPriorityMinimum")

    insecure_skip_tls_verify: bool | None = Field(None, alias="insecureSkipTLSVerify")

    service: ApiregistrationV1ServiceReference | None = Field(None, alias="service")

    version: str | None = Field(None, alias="version")

    version_priority: int | None = Field(None, alias="versionPriority")
