from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_node_runtime_handler_features import V1NodeRuntimeHandlerFeatures
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeRuntimeHandler",)


class V1NodeRuntimeHandler(BaseModel):
    features: Annotated[
        V1NodeRuntimeHandlerFeatures,
        BeforeValidator(_default_if_none(V1NodeRuntimeHandlerFeatures)),
    ] = Field(
        default_factory=lambda: V1NodeRuntimeHandlerFeatures(), exclude_if=_exclude_if
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)
