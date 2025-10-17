from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_app_armor_profile import V1AppArmorProfile
from .v1_capabilities import V1Capabilities
from .v1_se_linux_options import V1SELinuxOptions
from .v1_seccomp_profile import V1SeccompProfile
from .v1_windows_security_context_options import V1WindowsSecurityContextOptions

__all__ = ("V1SecurityContext",)


class V1SecurityContext(BaseModel):
    allow_privilege_escalation: bool | None = Field(
        default_factory=lambda: None, alias="allowPrivilegeEscalation"
    )

    app_armor_profile: V1AppArmorProfile = Field(
        default_factory=lambda: V1AppArmorProfile(), alias="appArmorProfile"
    )

    capabilities: V1Capabilities = Field(default_factory=lambda: V1Capabilities())

    privileged: bool | None = Field(default_factory=lambda: None)

    proc_mount: str | None = Field(default_factory=lambda: None, alias="procMount")

    read_only_root_filesystem: bool | None = Field(
        default_factory=lambda: None, alias="readOnlyRootFilesystem"
    )

    run_as_group: int | None = Field(default_factory=lambda: None, alias="runAsGroup")

    run_as_non_root: bool | None = Field(
        default_factory=lambda: None, alias="runAsNonRoot"
    )

    run_as_user: int | None = Field(default_factory=lambda: None, alias="runAsUser")

    se_linux_options: V1SELinuxOptions = Field(
        default_factory=lambda: V1SELinuxOptions(), alias="seLinuxOptions"
    )

    seccomp_profile: V1SeccompProfile = Field(
        default_factory=lambda: V1SeccompProfile(), alias="seccompProfile"
    )

    windows_options: V1WindowsSecurityContextOptions = Field(
        default_factory=lambda: V1WindowsSecurityContextOptions(),
        alias="windowsOptions",
    )
