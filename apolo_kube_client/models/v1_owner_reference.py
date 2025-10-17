from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1OwnerReference",)


class V1OwnerReference(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    block_owner_deletion: bool | None = Field(
        default=None,
        serialization_alias="blockOwnerDeletion",
        validation_alias=AliasChoices("block_owner_deletion", "blockOwnerDeletion"),
    )

    controller: bool | None = None

    kind: str | None = None

    name: str | None = None

    uid: str | None = None
