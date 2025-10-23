from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_daemon_endpoint import V1DaemonEndpoint
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeDaemonEndpoints",)


class V1NodeDaemonEndpoints(BaseModel):
    kubelet_endpoint: Annotated[
        V1DaemonEndpoint, BeforeValidator(_default_if_none(V1DaemonEndpoint))
    ] = Field(
        default_factory=lambda: V1DaemonEndpoint(),
        serialization_alias="kubeletEndpoint",
        validation_alias=AliasChoices("kubelet_endpoint", "kubeletEndpoint"),
        exclude_if=_exclude_if,
    )
