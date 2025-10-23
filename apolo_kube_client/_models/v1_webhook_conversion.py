from pydantic import AliasChoices, BaseModel, Field
from .apiextensions_v1_webhook_client_config import ApiextensionsV1WebhookClientConfig
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1WebhookConversion",)


class V1WebhookConversion(BaseModel):
    client_config: Annotated[
        ApiextensionsV1WebhookClientConfig,
        BeforeValidator(_default_if_none(ApiextensionsV1WebhookClientConfig)),
    ] = Field(
        default_factory=lambda: ApiextensionsV1WebhookClientConfig(),
        serialization_alias="clientConfig",
        validation_alias=AliasChoices("client_config", "clientConfig"),
        exclude_if=_exclude_if,
    )

    conversion_review_versions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="conversionReviewVersions",
        validation_alias=AliasChoices(
            "conversion_review_versions", "conversionReviewVersions"
        ),
        exclude_if=_exclude_if,
    )
