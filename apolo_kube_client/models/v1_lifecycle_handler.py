from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_exec_action import V1ExecAction
from .v1_http_get_action import V1HTTPGetAction
from .v1_sleep_action import V1SleepAction
from .v1_tcp_socket_action import V1TCPSocketAction

__all__ = ("V1LifecycleHandler",)


class V1LifecycleHandler(BaseModel):
    exec_: V1ExecAction = Field(default_factory=lambda: V1ExecAction(), alias="exec")

    http_get: V1HTTPGetAction = Field(
        default_factory=lambda: V1HTTPGetAction(), alias="httpGet"
    )

    sleep: V1SleepAction = Field(default_factory=lambda: V1SleepAction())

    tcp_socket: V1TCPSocketAction = Field(
        default_factory=lambda: V1TCPSocketAction(), alias="tcpSocket"
    )
