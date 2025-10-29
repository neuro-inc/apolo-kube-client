from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_node_swap_status import V1NodeSwapStatus
from pydantic import BeforeValidator

__all__ = ("V1NodeSystemInfo",)


class V1NodeSystemInfo(BaseModel):
    """NodeSystemInfo is a set of ids/uuids to uniquely identify the node."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeSystemInfo"

    architecture: Annotated[
        str, Field(description="""The Architecture reported by the node""")
    ]

    boot_id: Annotated[
        str, Field(alias="bootID", description="""Boot ID reported by the node.""")
    ]

    container_runtime_version: Annotated[
        str,
        Field(
            alias="containerRuntimeVersion",
            description="""ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2).""",
        ),
    ]

    kernel_version: Annotated[
        str,
        Field(
            alias="kernelVersion",
            description="""Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).""",
        ),
    ]

    kube_proxy_version: Annotated[
        str,
        Field(
            alias="kubeProxyVersion",
            description="""Deprecated: KubeProxy Version reported by the node.""",
        ),
    ]

    kubelet_version: Annotated[
        str,
        Field(
            alias="kubeletVersion",
            description="""Kubelet Version reported by the node.""",
        ),
    ]

    machine_id: Annotated[
        str,
        Field(
            alias="machineID",
            description="""MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html""",
        ),
    ]

    operating_system: Annotated[
        str,
        Field(
            alias="operatingSystem",
            description="""The Operating System reported by the node""",
        ),
    ]

    os_image: Annotated[
        str,
        Field(
            alias="osImage",
            description="""OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).""",
        ),
    ]

    swap: Annotated[
        V1NodeSwapStatus,
        Field(
            description="""Swap Info reported by the node.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1NodeSwapStatus)),
    ] = V1NodeSwapStatus()

    system_uuid: Annotated[
        str,
        Field(
            alias="systemUUID",
            description="""SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid""",
        ),
    ]
