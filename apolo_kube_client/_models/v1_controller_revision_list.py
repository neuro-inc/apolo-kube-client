from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_controller_revision import V1ControllerRevision
from .v1_list_meta import V1ListMeta

__all__ = ("V1ControllerRevisionList",)


class V1ControllerRevisionList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ControllerRevision] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
