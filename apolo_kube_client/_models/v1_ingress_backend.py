from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_ingress_service_backend import V1IngressServiceBackend
from .v1_typed_local_object_reference import V1TypedLocalObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressBackend",)


class V1IngressBackend(BaseModel):
    resource: Annotated[
        V1TypedLocalObjectReference,
        BeforeValidator(_default_if_none(V1TypedLocalObjectReference)),
    ] = Field(
        default_factory=lambda: V1TypedLocalObjectReference(), exclude_if=_exclude_if
    )

    service: Annotated[
        V1IngressServiceBackend,
        BeforeValidator(_default_if_none(V1IngressServiceBackend)),
    ] = Field(default_factory=lambda: V1IngressServiceBackend(), exclude_if=_exclude_if)
