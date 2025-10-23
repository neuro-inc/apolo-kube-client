from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("CoreV1EndpointPort",)


class CoreV1EndpointPort(BaseModel):
    app_protocol: str | None = Field(
        default=None,
        serialization_alias="appProtocol",
        validation_alias=AliasChoices("app_protocol", "appProtocol"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    port: int | None = Field(default=None, exclude_if=_exclude_if)

    protocol: str | None = Field(default=None, exclude_if=_exclude_if)
