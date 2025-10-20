from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1DaemonEndpoint",)


class V1DaemonEndpoint(BaseModel):
    port: int | None = Field(
        default=None,
        serialization_alias="Port",
        validation_alias=AliasChoices("port", "Port"),
    )
