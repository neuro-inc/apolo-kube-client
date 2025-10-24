from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ServiceBackendPort",)


class V1ServiceBackendPort(BaseModel):
    """ServiceBackendPort is the service port being referenced."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.ServiceBackendPort"

    name: Annotated[
        str | None,
        Field(
            description="""name is the name of the port on the Service. This is a mutually exclusive setting with "Number".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    number: Annotated[
        int | None,
        Field(
            description="""number is the numerical port number (e.g. 80) on the Service. This is a mutually exclusive setting with "Name".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
