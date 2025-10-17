from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_overhead import V1Overhead
from .v1_scheduling import V1Scheduling

__all__ = ("V1RuntimeClass",)


class V1RuntimeClass(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    handler: str | None = None

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    overhead: V1Overhead = Field(default_factory=lambda: V1Overhead())

    scheduling: V1Scheduling = Field(default_factory=lambda: V1Scheduling())
