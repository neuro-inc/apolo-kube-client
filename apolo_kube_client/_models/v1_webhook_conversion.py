from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .apiextensions_v1_webhook_client_config import ApiextensionsV1WebhookClientConfig
from .utils import _default_if_none
from pydantic import BeforeValidator

__all__ = ("V1WebhookConversion",)


class V1WebhookConversion(BaseModel):
    """WebhookConversion describes how to call a conversion webhook"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.WebhookConversion"
    )

    client_config: Annotated[
        ApiextensionsV1WebhookClientConfig,
        Field(
            alias="clientConfig",
            description="""clientConfig is the instructions for how to call the webhook if strategy is `Webhook`.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(ApiextensionsV1WebhookClientConfig)),
    ] = ApiextensionsV1WebhookClientConfig()

    conversion_review_versions: Annotated[
        list[str],
        Field(
            alias="conversionReviewVersions",
            description="""conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail.""",
        ),
    ]
