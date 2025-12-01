from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, BeforeValidator, Field

from .utils import _default_if_none
from .v1_node_runtime_handler_features import V1NodeRuntimeHandlerFeatures


__all__ = ("V1NodeRuntimeHandler",)


class V1NodeRuntimeHandler(BaseModel):
    """NodeRuntimeHandler is a set of runtime handler information."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeRuntimeHandler"

    features: Annotated[
        V1NodeRuntimeHandlerFeatures,
        Field(
            description="""Supported features.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1NodeRuntimeHandlerFeatures)),
    ] = V1NodeRuntimeHandlerFeatures()

    name: Annotated[
        str | None,
        Field(
            description="""Runtime handler name. Empty for the default runtime handler.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
