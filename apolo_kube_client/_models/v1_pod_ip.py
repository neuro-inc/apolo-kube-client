from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1PodIP",)


class V1PodIP(BaseModel):
    """PodIP represents a single IP address allocated to the pod."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PodIP"

    ip: Annotated[
        str, Field(description="""IP is the IP address assigned to the pod""")
    ]
