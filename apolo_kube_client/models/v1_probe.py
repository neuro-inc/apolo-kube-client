from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_exec_action import V1ExecAction
from .v1_grpc_action import V1GRPCAction
from .v1_http_get_action import V1HTTPGetAction
from .v1_tcp_socket_action import V1TCPSocketAction

__all__ = ("V1Probe",)


class V1Probe(BaseModel):
    _exec: V1ExecAction = Field(default_factory=lambda: V1ExecAction(), alias="exec")

    failure_threshold: int | None = Field(
        default_factory=lambda: None, alias="failureThreshold"
    )

    grpc: V1GRPCAction = Field(default_factory=lambda: V1GRPCAction(), alias="grpc")

    http_get: V1HTTPGetAction = Field(
        default_factory=lambda: V1HTTPGetAction(), alias="httpGet"
    )

    initial_delay_seconds: int | None = Field(
        default_factory=lambda: None, alias="initialDelaySeconds"
    )

    period_seconds: int | None = Field(
        default_factory=lambda: None, alias="periodSeconds"
    )

    success_threshold: int | None = Field(
        default_factory=lambda: None, alias="successThreshold"
    )

    tcp_socket: V1TCPSocketAction = Field(
        default_factory=lambda: V1TCPSocketAction(), alias="tcpSocket"
    )

    termination_grace_period_seconds: int | None = Field(
        default_factory=lambda: None, alias="terminationGracePeriodSeconds"
    )

    timeout_seconds: int | None = Field(
        default_factory=lambda: None, alias="timeoutSeconds"
    )
