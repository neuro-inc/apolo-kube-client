from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1NetworkPolicyPort",)


class V1NetworkPolicyPort(BaseModel):
    """NetworkPolicyPort describes a port to allow traffic on"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.NetworkPolicyPort"

    end_port: Annotated[
        int | None,
        Field(
            alias="endPort",
            description="""endPort indicates that the range of ports from port to endPort if set, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    port: Annotated[
        JsonType,
        Field(
            description="""port represents the port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched.""",
            exclude_if=lambda v: v == {},
        ),
    ] = {}

    protocol: Annotated[
        str | None,
        Field(
            description="""protocol represents the protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
