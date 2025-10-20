from pydantic import AliasChoices, BaseModel, Field


__all__ = ("DiscoveryV1EndpointPort",)


class DiscoveryV1EndpointPort(BaseModel):
    app_protocol: str | None = Field(
        default=None,
        serialization_alias="appProtocol",
        validation_alias=AliasChoices("app_protocol", "appProtocol"),
    )

    name: str | None = None

    port: int | None = None

    protocol: str | None = None
