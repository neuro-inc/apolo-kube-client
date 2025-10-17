from pydantic import AliasChoices, BaseModel, Field
from .v1_node_config_source import V1NodeConfigSource

__all__ = ("V1NodeConfigStatus",)


class V1NodeConfigStatus(BaseModel):
    active: V1NodeConfigSource = Field(default_factory=lambda: V1NodeConfigSource())

    assigned: V1NodeConfigSource = Field(default_factory=lambda: V1NodeConfigSource())

    error: str | None = None

    last_known_good: V1NodeConfigSource = Field(
        default_factory=lambda: V1NodeConfigSource(),
        serialization_alias="lastKnownGood",
        validation_alias=AliasChoices("last_known_good", "lastKnownGood"),
    )
