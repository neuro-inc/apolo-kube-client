from pydantic import AliasChoices, BaseModel, Field
from .apiregistration_v1_service_reference import ApiregistrationV1ServiceReference
from .utils import _default_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1APIServiceSpec",)


class V1APIServiceSpec(BaseModel):
    ca_bundle: str | None = Field(
        default=None,
        serialization_alias="caBundle",
        validation_alias=AliasChoices("ca_bundle", "caBundle"),
        exclude_if=_exclude_if,
    )

    group: str | None = Field(default=None, exclude_if=_exclude_if)

    group_priority_minimum: int | None = Field(
        default=None,
        serialization_alias="groupPriorityMinimum",
        validation_alias=AliasChoices("group_priority_minimum", "groupPriorityMinimum"),
        exclude_if=_exclude_if,
    )

    insecure_skip_tls_verify: bool | None = Field(
        default=None,
        serialization_alias="insecureSkipTLSVerify",
        validation_alias=AliasChoices(
            "insecure_skip_tls_verify", "insecureSkipTLSVerify"
        ),
        exclude_if=_exclude_if,
    )

    service: Annotated[
        ApiregistrationV1ServiceReference,
        BeforeValidator(_default_if_none(ApiregistrationV1ServiceReference)),
    ] = Field(
        default_factory=lambda: ApiregistrationV1ServiceReference(),
        exclude_if=_exclude_if,
    )

    version: str | None = Field(default=None, exclude_if=_exclude_if)

    version_priority: int | None = Field(
        default=None,
        serialization_alias="versionPriority",
        validation_alias=AliasChoices("version_priority", "versionPriority"),
        exclude_if=_exclude_if,
    )
