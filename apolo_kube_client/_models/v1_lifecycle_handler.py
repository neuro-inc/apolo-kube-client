from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_exec_action import V1ExecAction
from .v1_http_get_action import V1HTTPGetAction
from .v1_sleep_action import V1SleepAction
from .v1_tcp_socket_action import V1TCPSocketAction
from pydantic import BeforeValidator

__all__ = ("V1LifecycleHandler",)


class V1LifecycleHandler(BaseModel):
    """LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.LifecycleHandler"

    exec_: Annotated[
        V1ExecAction,
        Field(
            alias="exec",
            description="""Exec specifies a command to execute in the container.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ExecAction)),
    ] = V1ExecAction()

    http_get: Annotated[
        V1HTTPGetAction | None,
        Field(
            alias="httpGet",
            description="""HTTPGet specifies an HTTP GET request to perform.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    sleep: Annotated[
        V1SleepAction | None,
        Field(
            description="""Sleep represents a duration that the container should sleep.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    tcp_socket: Annotated[
        V1TCPSocketAction | None,
        Field(
            alias="tcpSocket",
            description="""Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
