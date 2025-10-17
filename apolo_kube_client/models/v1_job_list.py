from pydantic import AliasChoices, BaseModel, Field
from .v1_job import V1Job
from .v1_list_meta import V1ListMeta

__all__ = ("V1JobList",)


class V1JobList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1Job] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
