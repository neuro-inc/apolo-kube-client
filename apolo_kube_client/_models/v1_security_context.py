from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_app_armor_profile import V1AppArmorProfile
from .v1_capabilities import V1Capabilities
from .v1_se_linux_options import V1SELinuxOptions
from .v1_seccomp_profile import V1SeccompProfile
from .v1_windows_security_context_options import V1WindowsSecurityContextOptions
from pydantic import BeforeValidator

__all__ = ("V1SecurityContext",)


class V1SecurityContext(BaseModel):
    """SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext.  When both are set, the values in SecurityContext take precedence."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.SecurityContext"

    allow_privilege_escalation: Annotated[
        bool | None,
        Field(
            alias="allowPrivilegeEscalation",
            description="""AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    app_armor_profile: Annotated[
        V1AppArmorProfile | None,
        Field(
            alias="appArmorProfile",
            description="""appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod's appArmorProfile. Note that this field cannot be set when spec.os.name is windows.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    capabilities: Annotated[
        V1Capabilities,
        Field(
            description="""The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1Capabilities)),
    ] = V1Capabilities()

    privileged: Annotated[
        bool | None,
        Field(
            description="""Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    proc_mount: Annotated[
        str | None,
        Field(
            alias="procMount",
            description="""procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    read_only_root_filesystem: Annotated[
        bool | None,
        Field(
            alias="readOnlyRootFilesystem",
            description="""Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    run_as_group: Annotated[
        int | None,
        Field(
            alias="runAsGroup",
            description="""The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    run_as_non_root: Annotated[
        bool | None,
        Field(
            alias="runAsNonRoot",
            description="""Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    run_as_user: Annotated[
        int | None,
        Field(
            alias="runAsUser",
            description="""The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    se_linux_options: Annotated[
        V1SELinuxOptions,
        Field(
            alias="seLinuxOptions",
            description="""The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SELinuxOptions)),
    ] = V1SELinuxOptions()

    seccomp_profile: Annotated[
        V1SeccompProfile | None,
        Field(
            alias="seccompProfile",
            description="""The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    windows_options: Annotated[
        V1WindowsSecurityContextOptions,
        Field(
            alias="windowsOptions",
            description="""The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1WindowsSecurityContextOptions)),
    ] = V1WindowsSecurityContextOptions()
