from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, BeforeValidator, Field

from .utils import _default_if_none
from .v1_queuing_configuration import V1QueuingConfiguration


__all__ = ("V1LimitResponse",)


class V1LimitResponse(BaseModel):
    """LimitResponse defines how to handle requests that can not be executed right now."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.flowcontrol.v1.LimitResponse"

    queuing: Annotated[
        V1QueuingConfiguration,
        Field(
            description="""`queuing` holds the configuration parameters for queuing. This field may be non-empty only if `type` is `"Queue"`.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1QueuingConfiguration)),
    ] = V1QueuingConfiguration()

    type: Annotated[
        str,
        Field(
            description="""`type` is "Queue" or "Reject". "Queue" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. "Reject" means that requests that can not be executed upon arrival are rejected. Required."""
        ),
    ]
