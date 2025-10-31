from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_exec_action import V1ExecAction
from .v1_grpc_action import V1GRPCAction
from .v1_http_get_action import V1HTTPGetAction
from .v1_tcp_socket_action import V1TCPSocketAction
from pydantic import BeforeValidator

__all__ = ("V1Probe",)


class V1Probe(BaseModel):
    """Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.Probe"

    exec_: Annotated[
        V1ExecAction,
        Field(
            alias="exec",
            description="""Exec specifies a command to execute in the container.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ExecAction)),
    ] = V1ExecAction()

    failure_threshold: Annotated[
        int | None,
        Field(
            alias="failureThreshold",
            description="""Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    grpc: Annotated[
        V1GRPCAction | None,
        Field(
            description="""GRPC specifies a GRPC HealthCheckRequest.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    http_get: Annotated[
        V1HTTPGetAction | None,
        Field(
            alias="httpGet",
            description="""HTTPGet specifies an HTTP GET request to perform.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    initial_delay_seconds: Annotated[
        int | None,
        Field(
            alias="initialDelaySeconds",
            description="""Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    period_seconds: Annotated[
        int | None,
        Field(
            alias="periodSeconds",
            description="""How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    success_threshold: Annotated[
        int | None,
        Field(
            alias="successThreshold",
            description="""Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    tcp_socket: Annotated[
        V1TCPSocketAction | None,
        Field(
            alias="tcpSocket",
            description="""TCPSocket specifies a connection to a TCP port.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    termination_grace_period_seconds: Annotated[
        int | None,
        Field(
            alias="terminationGracePeriodSeconds",
            description="""Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    timeout_seconds: Annotated[
        int | None,
        Field(
            alias="timeoutSeconds",
            description="""Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
