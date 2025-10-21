from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_exec_action import V1ExecAction
from .v1_grpc_action import V1GRPCAction
from .v1_http_get_action import V1HTTPGetAction
from .v1_tcp_socket_action import V1TCPSocketAction
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Probe",)


class V1Probe(BaseModel):
    exec_: Annotated[V1ExecAction, BeforeValidator(_default_if_none(V1ExecAction))] = (
        Field(
            default_factory=lambda: V1ExecAction(),
            serialization_alias="exec",
            validation_alias=AliasChoices("exec_", "exec"),
        )
    )

    failure_threshold: int | None = Field(
        default=None,
        serialization_alias="failureThreshold",
        validation_alias=AliasChoices("failure_threshold", "failureThreshold"),
    )

    grpc: Annotated[V1GRPCAction, BeforeValidator(_default_if_none(V1GRPCAction))] = (
        Field(default_factory=lambda: V1GRPCAction())
    )

    http_get: Annotated[
        V1HTTPGetAction, BeforeValidator(_default_if_none(V1HTTPGetAction))
    ] = Field(
        default_factory=lambda: V1HTTPGetAction(),
        serialization_alias="httpGet",
        validation_alias=AliasChoices("http_get", "httpGet"),
    )

    initial_delay_seconds: int | None = Field(
        default=None,
        serialization_alias="initialDelaySeconds",
        validation_alias=AliasChoices("initial_delay_seconds", "initialDelaySeconds"),
    )

    period_seconds: int | None = Field(
        default=None,
        serialization_alias="periodSeconds",
        validation_alias=AliasChoices("period_seconds", "periodSeconds"),
    )

    success_threshold: int | None = Field(
        default=None,
        serialization_alias="successThreshold",
        validation_alias=AliasChoices("success_threshold", "successThreshold"),
    )

    tcp_socket: Annotated[
        V1TCPSocketAction, BeforeValidator(_default_if_none(V1TCPSocketAction))
    ] = Field(
        default_factory=lambda: V1TCPSocketAction(),
        serialization_alias="tcpSocket",
        validation_alias=AliasChoices("tcp_socket", "tcpSocket"),
    )

    termination_grace_period_seconds: int | None = Field(
        default=None,
        serialization_alias="terminationGracePeriodSeconds",
        validation_alias=AliasChoices(
            "termination_grace_period_seconds", "terminationGracePeriodSeconds"
        ),
    )

    timeout_seconds: int | None = Field(
        default=None,
        serialization_alias="timeoutSeconds",
        validation_alias=AliasChoices("timeout_seconds", "timeoutSeconds"),
    )
