from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_webhook_conversion import V1WebhookConversion

__all__ = ("V1CustomResourceConversion",)


class V1CustomResourceConversion(BaseModel):
    """CustomResourceConversion describes how to convert different versions of a CR."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceConversion"
    )

    strategy: Annotated[
        str,
        Field(
            description="""strategy specifies how custom resources are converted between versions. Allowed values are: - `"None"`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `"Webhook"`: API Server will call to an external webhook to do the conversion. Additional information
  is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set."""
        ),
    ]

    webhook: Annotated[
        V1WebhookConversion | None,
        Field(
            description="""webhook describes how to call the conversion webhook. Required when `strategy` is set to `"Webhook"`.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
