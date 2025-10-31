from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_container_status import V1ContainerStatus
from .v1_host_ip import V1HostIP
from .v1_pod_condition import V1PodCondition
from .v1_pod_extended_resource_claim_status import V1PodExtendedResourceClaimStatus
from .v1_pod_ip import V1PodIP
from .v1_pod_resource_claim_status import V1PodResourceClaimStatus
from datetime import datetime
from pydantic import BeforeValidator

__all__ = ("V1PodStatus",)


class V1PodStatus(BaseModel):
    """PodStatus represents information about the status of a pod. Status may trail the actual state of a system, especially if the node that hosts the pod cannot contact the control plane."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PodStatus"

    conditions: Annotated[
        list[V1PodCondition],
        Field(
            description="""Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    container_statuses: Annotated[
        list[V1ContainerStatus],
        Field(
            alias="containerStatuses",
            description="""Statuses of containers in this pod. Each container in the pod should have at most one status in this list, and all statuses should be for containers in the pod. However this is not enforced. If a status for a non-existent container is present in the list, or the list has duplicate names, the behavior of various Kubernetes components is not defined and those statuses might be ignored. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    ephemeral_container_statuses: Annotated[
        list[V1ContainerStatus],
        Field(
            alias="ephemeralContainerStatuses",
            description="""Statuses for any ephemeral containers that have run in this pod. Each ephemeral container in the pod should have at most one status in this list, and all statuses should be for containers in the pod. However this is not enforced. If a status for a non-existent container is present in the list, or the list has duplicate names, the behavior of various Kubernetes components is not defined and those statuses might be ignored. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    extended_resource_claim_status: Annotated[
        V1PodExtendedResourceClaimStatus | None,
        Field(
            alias="extendedResourceClaimStatus",
            description="""Status of extended resource claim backed by DRA.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    host_ip: Annotated[
        str | None,
        Field(
            alias="hostIP",
            description="""hostIP holds the IP address of the host to which the pod is assigned. Empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns mean that HostIP will not be updated even if there is a node is assigned to pod""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    host_i_ps: Annotated[
        list[V1HostIP],
        Field(
            alias="hostIPs",
            description="""hostIPs holds the IP addresses allocated to the host. If this field is specified, the first entry must match the hostIP field. This list is empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns means that HostIPs will not be updated even if there is a node is assigned to this pod.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    init_container_statuses: Annotated[
        list[V1ContainerStatus],
        Field(
            alias="initContainerStatuses",
            description="""Statuses of init containers in this pod. The most recent successful non-restartable init container will have ready = true, the most recently started container will have startTime set. Each init container in the pod should have at most one status in this list, and all statuses should be for containers in the pod. However this is not enforced. If a status for a non-existent container is present in the list, or the list has duplicate names, the behavior of various Kubernetes components is not defined and those statuses might be ignored. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-and-container-status""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    message: Annotated[
        str | None,
        Field(
            description="""A human readable message indicating details about why the pod is in this condition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    nominated_node_name: Annotated[
        str | None,
        Field(
            alias="nominatedNodeName",
            description="""nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""If set, this represents the .metadata.generation that the pod status was set based upon. This is an alpha field. Enable PodObservedGenerationTracking to be able to use this field.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    phase: Annotated[
        str | None,
        Field(
            description="""The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:

Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.

More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    pod_ip: Annotated[
        str | None,
        Field(
            alias="podIP",
            description="""podIP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    pod_i_ps: Annotated[
        list[V1PodIP],
        Field(
            alias="podIPs",
            description="""podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    qos_class: Annotated[
        str | None,
        Field(
            alias="qosClass",
            description="""The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#quality-of-service-classes""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resize: Annotated[
        str | None,
        Field(
            description="""Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to "Proposed" Deprecated: Resize status is moved to two pod conditions PodResizePending and PodResizeInProgress. PodResizePending will track states where the spec has been resized, but the Kubelet has not yet allocated the resources. PodResizeInProgress will track in-progress resizes, and should be present whenever allocated resources != acknowledged resources.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource_claim_statuses: Annotated[
        list[V1PodResourceClaimStatus],
        Field(
            alias="resourceClaimStatuses",
            description="""Status of resource claims.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    start_time: Annotated[
        datetime | None,
        Field(
            alias="startTime",
            description="""RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
