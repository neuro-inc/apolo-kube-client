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
        None, alias="allowPrivilegeEscalation"
    )

    app_armor_profile: V1AppArmorProfile | None = Field(None, alias="appArmorProfile")

    capabilities: V1Capabilities | None = Field(None, alias="capabilities")

    privileged: bool | None = Field(None, alias="privileged")

    proc_mount: str | None = Field(None, alias="procMount")

    read_only_root_filesystem: bool | None = Field(None, alias="readOnlyRootFilesystem")

    run_as_group: int | None = Field(None, alias="runAsGroup")

    run_as_non_root: bool | None = Field(None, alias="runAsNonRoot")

    run_as_user: int | None = Field(None, alias="runAsUser")

    se_linux_options: V1SELinuxOptions | None = Field(None, alias="seLinuxOptions")

    seccomp_profile: V1SeccompProfile | None = Field(None, alias="seccompProfile")

    windows_options: V1WindowsSecurityContextOptions | None = Field(
        None, alias="windowsOptions"
    )
