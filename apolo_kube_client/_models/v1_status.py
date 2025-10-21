from pydantic import AliasChoices, Field
from .base import ListModel
from .utils import _default_if_none
from .v1_list_meta import V1ListMeta
from .v1_status_details import V1StatusDetails
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Status",)


class V1Status(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    code: int | None = None

    details: Annotated[
        V1StatusDetails, BeforeValidator(_default_if_none(V1StatusDetails))
    ] = Field(default_factory=lambda: V1StatusDetails())

    kind: str | None = None

    message: str | None = None

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta())
    )

    reason: str | None = None

    status: str | None = None
