from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_app_armor_profile import V1AppArmorProfile
from .v1_capabilities import V1Capabilities
from .v1_se_linux_options import V1SELinuxOptions
from .v1_seccomp_profile import V1SeccompProfile
from .v1_windows_security_context_options import V1WindowsSecurityContextOptions
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SecurityContext",)


class V1SecurityContext(BaseModel):
    allow_privilege_escalation: bool | None = Field(
        default=None,
        serialization_alias="allowPrivilegeEscalation",
        validation_alias=AliasChoices(
            "allow_privilege_escalation", "allowPrivilegeEscalation"
        ),
    )

    app_armor_profile: Annotated[
        V1AppArmorProfile, BeforeValidator(_default_if_none(V1AppArmorProfile))
    ] = Field(
        default_factory=lambda: V1AppArmorProfile(),
        serialization_alias="appArmorProfile",
        validation_alias=AliasChoices("app_armor_profile", "appArmorProfile"),
    )

    capabilities: Annotated[
        V1Capabilities, BeforeValidator(_default_if_none(V1Capabilities))
    ] = Field(default_factory=lambda: V1Capabilities())

    privileged: bool | None = None

    proc_mount: str | None = Field(
        default=None,
        serialization_alias="procMount",
        validation_alias=AliasChoices("proc_mount", "procMount"),
    )

    read_only_root_filesystem: bool | None = Field(
        default=None,
        serialization_alias="readOnlyRootFilesystem",
        validation_alias=AliasChoices(
            "read_only_root_filesystem", "readOnlyRootFilesystem"
        ),
    )

    run_as_group: int | None = Field(
        default=None,
        serialization_alias="runAsGroup",
        validation_alias=AliasChoices("run_as_group", "runAsGroup"),
    )

    run_as_non_root: bool | None = Field(
        default=None,
        serialization_alias="runAsNonRoot",
        validation_alias=AliasChoices("run_as_non_root", "runAsNonRoot"),
    )

    run_as_user: int | None = Field(
        default=None,
        serialization_alias="runAsUser",
        validation_alias=AliasChoices("run_as_user", "runAsUser"),
    )

    se_linux_options: Annotated[
        V1SELinuxOptions, BeforeValidator(_default_if_none(V1SELinuxOptions))
    ] = Field(
        default_factory=lambda: V1SELinuxOptions(),
        serialization_alias="seLinuxOptions",
        validation_alias=AliasChoices("se_linux_options", "seLinuxOptions"),
    )

    seccomp_profile: Annotated[
        V1SeccompProfile, BeforeValidator(_default_if_none(V1SeccompProfile))
    ] = Field(
        default_factory=lambda: V1SeccompProfile(),
        serialization_alias="seccompProfile",
        validation_alias=AliasChoices("seccomp_profile", "seccompProfile"),
    )

    windows_options: Annotated[
        V1WindowsSecurityContextOptions,
        BeforeValidator(_default_if_none(V1WindowsSecurityContextOptions)),
    ] = Field(
        default_factory=lambda: V1WindowsSecurityContextOptions(),
        serialization_alias="windowsOptions",
        validation_alias=AliasChoices("windows_options", "windowsOptions"),
    )
