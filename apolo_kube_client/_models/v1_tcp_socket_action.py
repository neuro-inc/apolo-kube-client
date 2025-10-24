from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1TCPSocketAction",)


class V1TCPSocketAction(BaseModel):
    """TCPSocketAction describes an action based on opening a socket"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.TCPSocketAction"

    host: Annotated[
        str | None,
        Field(
            description="""Optional: Host name to connect to, defaults to the pod IP.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    port: Annotated[
        JsonType,
        Field(
            description="""Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME."""
        ),
    ]
