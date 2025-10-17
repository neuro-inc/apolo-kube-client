from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1beta2ResourceClaimConsumerReference",)


class V1beta2ResourceClaimConsumerReference(BaseModel):
    api_group: str | None = Field(
        default=None,
        serialization_alias="apiGroup",
        validation_alias=AliasChoices("api_group", "apiGroup"),
    )

    name: str | None = None

    resource: str | None = None

    uid: str | None = None
