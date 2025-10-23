from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_exec_action import V1ExecAction
from .v1_http_get_action import V1HTTPGetAction
from .v1_sleep_action import V1SleepAction
from .v1_tcp_socket_action import V1TCPSocketAction
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LifecycleHandler",)


class V1LifecycleHandler(BaseModel):
    exec_: Annotated[V1ExecAction, BeforeValidator(_default_if_none(V1ExecAction))] = (
        Field(
            default_factory=lambda: V1ExecAction(),
            serialization_alias="exec",
            validation_alias=AliasChoices("exec_", "exec"),
            exclude_if=_exclude_if,
        )
    )

    http_get: Annotated[
        V1HTTPGetAction, BeforeValidator(_default_if_none(V1HTTPGetAction))
    ] = Field(
        default_factory=lambda: V1HTTPGetAction(),
        serialization_alias="httpGet",
        validation_alias=AliasChoices("http_get", "httpGet"),
        exclude_if=_exclude_if,
    )

    sleep: Annotated[
        V1SleepAction, BeforeValidator(_default_if_none(V1SleepAction))
    ] = Field(default_factory=lambda: V1SleepAction(), exclude_if=_exclude_if)

    tcp_socket: Annotated[
        V1TCPSocketAction, BeforeValidator(_default_if_none(V1TCPSocketAction))
    ] = Field(
        default_factory=lambda: V1TCPSocketAction(),
        serialization_alias="tcpSocket",
        validation_alias=AliasChoices("tcp_socket", "tcpSocket"),
        exclude_if=_exclude_if,
    )
