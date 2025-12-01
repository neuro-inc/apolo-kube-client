from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1PodIP",)


class V1PodIP(BaseConfiguredModel):
    """PodIP represents a single IP address allocated to the pod."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PodIP"

    ip: Annotated[
        str, Field(description="""IP is the IP address assigned to the pod""")
    ]
