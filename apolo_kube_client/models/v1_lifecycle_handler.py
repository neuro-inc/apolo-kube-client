from pydantic import BaseModel, Field

from .v1_exec_action import V1ExecAction
from .v1_h_t_t_p_get_action import V1HTTPGetAction
from .v1_sleep_action import V1SleepAction
from .v1_t_c_p_socket_action import V1TCPSocketAction


class V1LifecycleHandler(BaseModel):
    _exec: V1ExecAction | None = Field(None, alias="exec")

    http_get: V1HTTPGetAction | None = Field(None, alias="httpGet")

    sleep: V1SleepAction | None = Field(None, alias="sleep")

    tcp_socket: V1TCPSocketAction | None = Field(None, alias="tcpSocket")
