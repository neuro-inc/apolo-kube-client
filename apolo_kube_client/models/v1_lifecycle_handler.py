from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_exec_action import V1ExecAction
from .v1_http_get_action import V1HTTPGetAction
from .v1_sleep_action import V1SleepAction
from .v1_tcp_socket_action import V1TCPSocketAction

__all__ = ("V1LifecycleHandler",)


class V1LifecycleHandler(BaseModel):
    _exec: V1ExecAction | None = Field(None, alias="exec")

    http_get: V1HTTPGetAction | None = Field(None, alias="httpGet")

    sleep: V1SleepAction | None = Field(None, alias="sleep")

    tcp_socket: V1TCPSocketAction | None = Field(None, alias="tcpSocket")
