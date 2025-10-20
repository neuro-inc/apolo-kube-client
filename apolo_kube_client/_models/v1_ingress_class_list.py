from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_ingress_class import V1IngressClass
from .v1_list_meta import V1ListMeta

__all__ = ("V1IngressClassList",)


class V1IngressClassList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1IngressClass] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
