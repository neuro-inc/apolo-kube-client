from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Secret",)


class V1Secret(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    data: dict[str, str] = {}

    immutable: bool | None = None

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    string_data: dict[str, str] = Field(
        default={},
        serialization_alias="stringData",
        validation_alias=AliasChoices("string_data", "stringData"),
    )

    type: str | None = None
