from pydantic import AliasChoices, Field
from .base import ListModel
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    code: int | None = Field(default=None, exclude_if=_exclude_if)

    details: Annotated[
        V1StatusDetails, BeforeValidator(_default_if_none(V1StatusDetails))
    ] = Field(default_factory=lambda: V1StatusDetails(), exclude_if=_exclude_if)

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta(), exclude_if=_exclude_if)
    )

    reason: str | None = Field(default=None, exclude_if=_exclude_if)

    status: str | None = Field(default=None, exclude_if=_exclude_if)
