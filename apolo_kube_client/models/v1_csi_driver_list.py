from pydantic import AliasChoices, BaseModel, Field
from .v1_csi_driver import V1CSIDriver
from .v1_list_meta import V1ListMeta

__all__ = ("V1CSIDriverList",)


class V1CSIDriverList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1CSIDriver] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
