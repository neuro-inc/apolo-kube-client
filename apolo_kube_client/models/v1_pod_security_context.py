from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_app_armor_profile import V1AppArmorProfile
from .v1_se_linux_options import V1SELinuxOptions
from .v1_seccomp_profile import V1SeccompProfile
from .v1_sysctl import V1Sysctl
from .v1_windows_security_context_options import V1WindowsSecurityContextOptions

__all__ = ("V1PodSecurityContext",)


class V1PodSecurityContext(BaseModel):
    app_armor_profile: V1AppArmorProfile = Field(
        default_factory=lambda: V1AppArmorProfile(), alias="appArmorProfile"
    )

    fs_group: int | None = Field(default_factory=lambda: None, alias="fsGroup")

    fs_group_change_policy: str | None = Field(
        default_factory=lambda: None, alias="fsGroupChangePolicy"
    )

    run_as_group: int | None = Field(default_factory=lambda: None, alias="runAsGroup")

    run_as_non_root: bool | None = Field(
        default_factory=lambda: None, alias="runAsNonRoot"
    )

    run_as_user: int | None = Field(default_factory=lambda: None, alias="runAsUser")

    se_linux_change_policy: str | None = Field(
        default_factory=lambda: None, alias="seLinuxChangePolicy"
    )

    se_linux_options: V1SELinuxOptions = Field(
        default_factory=lambda: V1SELinuxOptions(), alias="seLinuxOptions"
    )

    seccomp_profile: V1SeccompProfile = Field(
        default_factory=lambda: V1SeccompProfile(), alias="seccompProfile"
    )

    supplemental_groups: list[int] = Field(
        default_factory=lambda: [], alias="supplementalGroups"
    )

    supplemental_groups_policy: str | None = Field(
        default_factory=lambda: None, alias="supplementalGroupsPolicy"
    )

    sysctls: list[V1Sysctl] = Field(default_factory=lambda: [], alias="sysctls")

    windows_options: V1WindowsSecurityContextOptions = Field(
        default_factory=lambda: V1WindowsSecurityContextOptions(),
        alias="windowsOptions",
    )
