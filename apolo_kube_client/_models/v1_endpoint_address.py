from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_reference import V1ObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1EndpointAddress",)


class V1EndpointAddress(BaseModel):
    hostname: str | None = Field(default=None, exclude_if=_exclude_if)

    ip: str | None = Field(default=None, exclude_if=_exclude_if)

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
        exclude_if=_exclude_if,
    )

    target_ref: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(
        default_factory=lambda: V1ObjectReference(),
        serialization_alias="targetRef",
        validation_alias=AliasChoices("target_ref", "targetRef"),
        exclude_if=_exclude_if,
    )
