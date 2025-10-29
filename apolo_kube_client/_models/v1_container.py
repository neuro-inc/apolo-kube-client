from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_container_port import V1ContainerPort
from .v1_container_resize_policy import V1ContainerResizePolicy
from .v1_container_restart_rule import V1ContainerRestartRule
from .v1_env_from_source import V1EnvFromSource
from .v1_env_var import V1EnvVar
from .v1_lifecycle import V1Lifecycle
from .v1_probe import V1Probe
from .v1_resource_requirements import V1ResourceRequirements
from .v1_security_context import V1SecurityContext
from .v1_volume_device import V1VolumeDevice
from .v1_volume_mount import V1VolumeMount
from pydantic import BeforeValidator

__all__ = ("V1Container",)


class V1Container(BaseModel):
    """A single application container that you want to run within a pod."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.Container"

    args: Annotated[
        list[str],
        Field(
            description="""Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    command: Annotated[
        list[str],
        Field(
            description="""Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    env: Annotated[
        list[V1EnvVar],
        Field(
            description="""List of environment variables to set in the container. Cannot be updated.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    env_from: Annotated[
        list[V1EnvFromSource],
        Field(
            alias="envFrom",
            description="""List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    image: Annotated[
        str | None,
        Field(
            description="""Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    image_pull_policy: Annotated[
        str | None,
        Field(
            alias="imagePullPolicy",
            description="""Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    lifecycle: Annotated[
        V1Lifecycle,
        Field(
            description="""Actions that the management system should take in response to container lifecycle events. Cannot be updated.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1Lifecycle)),
    ] = V1Lifecycle()

    liveness_probe: Annotated[
        V1Probe,
        Field(
            alias="livenessProbe",
            description="""Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1Probe)),
    ] = V1Probe()

    name: Annotated[
        str,
        Field(
            description="""Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated."""
        ),
    ]

    ports: Annotated[
        list[V1ContainerPort],
        Field(
            description="""List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    readiness_probe: Annotated[
        V1Probe,
        Field(
            alias="readinessProbe",
            description="""Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1Probe)),
    ] = V1Probe()

    resize_policy: Annotated[
        list[V1ContainerResizePolicy],
        Field(
            alias="resizePolicy",
            description="""Resources resize policy for the container.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    resources: Annotated[
        V1ResourceRequirements,
        Field(
            description="""Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ResourceRequirements)),
    ] = V1ResourceRequirements()

    restart_policy: Annotated[
        str | None,
        Field(
            alias="restartPolicy",
            description="""RestartPolicy defines the restart behavior of individual containers in a pod. This overrides the pod-level restart policy. When this field is not specified, the restart behavior is defined by the Pod's restart policy and the container type. Additionally, setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    restart_policy_rules: Annotated[
        list[V1ContainerRestartRule],
        Field(
            alias="restartPolicyRules",
            description="""Represents a list of rules to be checked to determine if the container should be restarted on exit. The rules are evaluated in order. Once a rule matches a container exit condition, the remaining rules are ignored. If no rule matches the container exit condition, the Container-level restart policy determines the whether the container is restarted or not. Constraints on the rules: - At most 20 rules are allowed. - Rules can have the same action. - Identical rules are not forbidden in validations. When rules are specified, container MUST set RestartPolicy explicitly even it if matches the Pod's RestartPolicy.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    security_context: Annotated[
        V1SecurityContext,
        Field(
            alias="securityContext",
            description="""SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecurityContext)),
    ] = V1SecurityContext()

    startup_probe: Annotated[
        V1Probe,
        Field(
            alias="startupProbe",
            description="""StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1Probe)),
    ] = V1Probe()

    stdin: Annotated[
        bool | None,
        Field(
            description="""Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    stdin_once: Annotated[
        bool | None,
        Field(
            alias="stdinOnce",
            description="""Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    termination_message_path: Annotated[
        str | None,
        Field(
            alias="terminationMessagePath",
            description="""Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    termination_message_policy: Annotated[
        str | None,
        Field(
            alias="terminationMessagePolicy",
            description="""Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    tty: Annotated[
        bool | None,
        Field(
            description="""Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    volume_devices: Annotated[
        list[V1VolumeDevice],
        Field(
            alias="volumeDevices",
            description="""volumeDevices is the list of block devices to be used by the container.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    volume_mounts: Annotated[
        list[V1VolumeMount],
        Field(
            alias="volumeMounts",
            description="""Pod volumes to mount into the container's filesystem. Cannot be updated.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    working_dir: Annotated[
        str | None,
        Field(
            alias="workingDir",
            description="""Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
