from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_app_armor_profile import V1AppArmorProfile
from .v1_se_linux_options import V1SELinuxOptions
from .v1_seccomp_profile import V1SeccompProfile
from .v1_sysctl import V1Sysctl
from .v1_windows_security_context_options import V1WindowsSecurityContextOptions

__all__ = ("V1PodSecurityContext",)


class V1PodSecurityContext(BaseModel):
    app_armor_profile: V1AppArmorProfile = Field(
        default_factory=lambda: V1AppArmorProfile(),
        serialization_alias="appArmorProfile",
        validation_alias=AliasChoices("app_armor_profile", "appArmorProfile"),
    )

    fs_group: int | None = Field(
        default=None,
        serialization_alias="fsGroup",
        validation_alias=AliasChoices("fs_group", "fsGroup"),
    )

    fs_group_change_policy: str | None = Field(
        default=None,
        serialization_alias="fsGroupChangePolicy",
        validation_alias=AliasChoices("fs_group_change_policy", "fsGroupChangePolicy"),
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

    se_linux_change_policy: str | None = Field(
        default=None,
        serialization_alias="seLinuxChangePolicy",
        validation_alias=AliasChoices("se_linux_change_policy", "seLinuxChangePolicy"),
    )

    se_linux_options: V1SELinuxOptions = Field(
        default_factory=lambda: V1SELinuxOptions(),
        serialization_alias="seLinuxOptions",
        validation_alias=AliasChoices("se_linux_options", "seLinuxOptions"),
    )

    seccomp_profile: V1SeccompProfile = Field(
        default_factory=lambda: V1SeccompProfile(),
        serialization_alias="seccompProfile",
        validation_alias=AliasChoices("seccomp_profile", "seccompProfile"),
    )

    supplemental_groups: list[int] = Field(
        default=[],
        serialization_alias="supplementalGroups",
        validation_alias=AliasChoices("supplemental_groups", "supplementalGroups"),
    )

    supplemental_groups_policy: str | None = Field(
        default=None,
        serialization_alias="supplementalGroupsPolicy",
        validation_alias=AliasChoices(
            "supplemental_groups_policy", "supplementalGroupsPolicy"
        ),
    )

    sysctls: list[V1Sysctl] = Field(default=[])

    windows_options: V1WindowsSecurityContextOptions = Field(
        default_factory=lambda: V1WindowsSecurityContextOptions(),
        serialization_alias="windowsOptions",
        validation_alias=AliasChoices("windows_options", "windowsOptions"),
    )
