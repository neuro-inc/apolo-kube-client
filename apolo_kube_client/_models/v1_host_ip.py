from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1HostIP",)


class V1HostIP(BaseModel):
    """HostIP represents a single IP address allocated to the host."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.HostIP"

    ip: Annotated[
        str, Field(description="""IP is the IP address assigned to the host""")
    ]
