from pydantic import BaseModel, Field
from .utils import _default_if_none
from .v1_node_selector import V1NodeSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1VolumeNodeAffinity",)


class V1VolumeNodeAffinity(BaseModel):
    required: Annotated[
        V1NodeSelector, BeforeValidator(_default_if_none(V1NodeSelector))
    ] = Field(default_factory=lambda: V1NodeSelector())
