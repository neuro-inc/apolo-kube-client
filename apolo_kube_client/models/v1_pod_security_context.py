from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_app_armor_profile import V1AppArmorProfile
from .v1_se_linux_options import V1SELinuxOptions
from .v1_seccomp_profile import V1SeccompProfile
from .v1_sysctl import V1Sysctl
from .v1_windows_security_context_options import V1WindowsSecurityContextOptions

__all__ = ("V1PodSecurityContext",)


class V1PodSecurityContext(BaseModel):
    app_armor_profile: V1AppArmorProfile | None = Field(None, alias="appArmorProfile")

    fs_group: int | None = Field(None, alias="fsGroup")

    fs_group_change_policy: str | None = Field(None, alias="fsGroupChangePolicy")

    run_as_group: int | None = Field(None, alias="runAsGroup")

    run_as_non_root: bool | None = Field(None, alias="runAsNonRoot")

    run_as_user: int | None = Field(None, alias="runAsUser")

    se_linux_change_policy: str | None = Field(None, alias="seLinuxChangePolicy")

    se_linux_options: V1SELinuxOptions | None = Field(None, alias="seLinuxOptions")

    seccomp_profile: V1SeccompProfile | None = Field(None, alias="seccompProfile")

    supplemental_groups: list[int] | None = Field(None, alias="supplementalGroups")

    supplemental_groups_policy: str | None = Field(
        None, alias="supplementalGroupsPolicy"
    )

    sysctls: list[V1Sysctl] | None = Field(None, alias="sysctls")

    windows_options: V1WindowsSecurityContextOptions | None = Field(
        None, alias="windowsOptions"
    )
