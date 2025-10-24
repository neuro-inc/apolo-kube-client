from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("ApiregistrationV1ServiceReference",)


class ApiregistrationV1ServiceReference(BaseModel):
    """ServiceReference holds a reference to Service.legacy.k8s.io"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.kube-aggregator.pkg.apis.apiregistration.v1.ServiceReference"
    )

    name: Annotated[
        str | None,
        Field(
            description="""Name is the name of the service""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    namespace: Annotated[
        str | None,
        Field(
            description="""Namespace is the namespace of the service""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    port: Annotated[
        int | None,
        Field(
            description="""If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
