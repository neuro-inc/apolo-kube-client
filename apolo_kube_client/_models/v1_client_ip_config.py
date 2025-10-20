from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ClientIPConfig",)


class V1ClientIPConfig(BaseModel):
    timeout_seconds: int | None = Field(
        default=None,
        serialization_alias="timeoutSeconds",
        validation_alias=AliasChoices("timeout_seconds", "timeoutSeconds"),
    )
