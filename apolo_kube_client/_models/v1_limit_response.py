from pydantic import BaseModel, Field
from .utils import _default_if_none
from .v1_queuing_configuration import V1QueuingConfiguration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LimitResponse",)


class V1LimitResponse(BaseModel):
    queuing: Annotated[
        V1QueuingConfiguration,
        BeforeValidator(_default_if_none(V1QueuingConfiguration)),
    ] = Field(default_factory=lambda: V1QueuingConfiguration())

    type: str | None = None
