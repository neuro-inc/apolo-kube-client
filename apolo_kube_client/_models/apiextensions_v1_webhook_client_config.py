from pydantic import AliasChoices, BaseModel, Field
from .apiextensions_v1_service_reference import ApiextensionsV1ServiceReference
from .utils import _default_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("ApiextensionsV1WebhookClientConfig",)


class ApiextensionsV1WebhookClientConfig(BaseModel):
    ca_bundle: str | None = Field(
        default=None,
        serialization_alias="caBundle",
        validation_alias=AliasChoices("ca_bundle", "caBundle"),
        exclude_if=_exclude_if,
    )

    service: Annotated[
        ApiextensionsV1ServiceReference,
        BeforeValidator(_default_if_none(ApiextensionsV1ServiceReference)),
    ] = Field(
        default_factory=lambda: ApiextensionsV1ServiceReference(),
        exclude_if=_exclude_if,
    )

    url: str | None = Field(default=None, exclude_if=_exclude_if)
