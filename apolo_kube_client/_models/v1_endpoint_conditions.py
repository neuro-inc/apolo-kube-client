from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1EndpointConditions",)


class V1EndpointConditions(BaseModel):
    """EndpointConditions represents the current condition of an endpoint."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.discovery.v1.EndpointConditions"

    ready: Annotated[
        bool | None,
        Field(
            description="""ready indicates that this endpoint is ready to receive traffic, according to whatever system is managing the endpoint. A nil value should be interpreted as "true". In general, an endpoint should be marked ready if it is serving and not terminating, though this can be overridden in some cases, such as when the associated Service has set the publishNotReadyAddresses flag.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    serving: Annotated[
        bool | None,
        Field(
            description="""serving indicates that this endpoint is able to receive traffic, according to whatever system is managing the endpoint. For endpoints backed by pods, the EndpointSlice controller will mark the endpoint as serving if the pod's Ready condition is True. A nil value should be interpreted as "true".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    terminating: Annotated[
        bool | None,
        Field(
            description="""terminating indicates that this endpoint is terminating. A nil value should be interpreted as "false".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
