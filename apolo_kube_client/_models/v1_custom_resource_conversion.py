from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_webhook_conversion import V1WebhookConversion
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CustomResourceConversion",)


class V1CustomResourceConversion(BaseModel):
    strategy: str | None = Field(default=None, exclude_if=_exclude_if)

    webhook: Annotated[
        V1WebhookConversion, BeforeValidator(_default_if_none(V1WebhookConversion))
    ] = Field(default_factory=lambda: V1WebhookConversion(), exclude_if=_exclude_if)
