from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_node_config_source import V1NodeConfigSource
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeConfigStatus",)


class V1NodeConfigStatus(BaseModel):
    active: Annotated[
        V1NodeConfigSource, BeforeValidator(_default_if_none(V1NodeConfigSource))
    ] = Field(default_factory=lambda: V1NodeConfigSource(), exclude_if=_exclude_if)

    assigned: Annotated[
        V1NodeConfigSource, BeforeValidator(_default_if_none(V1NodeConfigSource))
    ] = Field(default_factory=lambda: V1NodeConfigSource(), exclude_if=_exclude_if)

    error: str | None = Field(default=None, exclude_if=_exclude_if)

    last_known_good: Annotated[
        V1NodeConfigSource, BeforeValidator(_default_if_none(V1NodeConfigSource))
    ] = Field(
        default_factory=lambda: V1NodeConfigSource(),
        serialization_alias="lastKnownGood",
        validation_alias=AliasChoices("last_known_good", "lastKnownGood"),
        exclude_if=_exclude_if,
    )
