from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_app_armor_profile import V1AppArmorProfile
from .v1_se_linux_options import V1SELinuxOptions
from .v1_seccomp_profile import V1SeccompProfile
from .v1_sysctl import V1Sysctl
from .v1_windows_security_context_options import V1WindowsSecurityContextOptions
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodSecurityContext",)


class V1PodSecurityContext(BaseModel):
    app_armor_profile: Annotated[
        V1AppArmorProfile, BeforeValidator(_default_if_none(V1AppArmorProfile))
    ] = Field(
        default_factory=lambda: V1AppArmorProfile(),
        serialization_alias="appArmorProfile",
        validation_alias=AliasChoices("app_armor_profile", "appArmorProfile"),
        exclude_if=_exclude_if,
    )

    fs_group: int | None = Field(
        default=None,
        serialization_alias="fsGroup",
        validation_alias=AliasChoices("fs_group", "fsGroup"),
        exclude_if=_exclude_if,
    )

    fs_group_change_policy: str | None = Field(
        default=None,
        serialization_alias="fsGroupChangePolicy",
        validation_alias=AliasChoices("fs_group_change_policy", "fsGroupChangePolicy"),
        exclude_if=_exclude_if,
    )

    run_as_group: int | None = Field(
        default=None,
        serialization_alias="runAsGroup",
        validation_alias=AliasChoices("run_as_group", "runAsGroup"),
        exclude_if=_exclude_if,
    )

    run_as_non_root: bool | None = Field(
        default=None,
        serialization_alias="runAsNonRoot",
        validation_alias=AliasChoices("run_as_non_root", "runAsNonRoot"),
        exclude_if=_exclude_if,
    )

    run_as_user: int | None = Field(
        default=None,
        serialization_alias="runAsUser",
        validation_alias=AliasChoices("run_as_user", "runAsUser"),
        exclude_if=_exclude_if,
    )

    se_linux_change_policy: str | None = Field(
        default=None,
        serialization_alias="seLinuxChangePolicy",
        validation_alias=AliasChoices("se_linux_change_policy", "seLinuxChangePolicy"),
        exclude_if=_exclude_if,
    )

    se_linux_options: Annotated[
        V1SELinuxOptions, BeforeValidator(_default_if_none(V1SELinuxOptions))
    ] = Field(
        default_factory=lambda: V1SELinuxOptions(),
        serialization_alias="seLinuxOptions",
        validation_alias=AliasChoices("se_linux_options", "seLinuxOptions"),
        exclude_if=_exclude_if,
    )

    seccomp_profile: Annotated[
        V1SeccompProfile, BeforeValidator(_default_if_none(V1SeccompProfile))
    ] = Field(
        default_factory=lambda: V1SeccompProfile(),
        serialization_alias="seccompProfile",
        validation_alias=AliasChoices("seccomp_profile", "seccompProfile"),
        exclude_if=_exclude_if,
    )

    supplemental_groups: Annotated[
        list[int], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="supplementalGroups",
        validation_alias=AliasChoices("supplemental_groups", "supplementalGroups"),
        exclude_if=_exclude_if,
    )

    supplemental_groups_policy: str | None = Field(
        default=None,
        serialization_alias="supplementalGroupsPolicy",
        validation_alias=AliasChoices(
            "supplemental_groups_policy", "supplementalGroupsPolicy"
        ),
        exclude_if=_exclude_if,
    )

    sysctls: Annotated[list[V1Sysctl], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )

    windows_options: Annotated[
        V1WindowsSecurityContextOptions,
        BeforeValidator(_default_if_none(V1WindowsSecurityContextOptions)),
    ] = Field(
        default_factory=lambda: V1WindowsSecurityContextOptions(),
        serialization_alias="windowsOptions",
        validation_alias=AliasChoices("windows_options", "windowsOptions"),
        exclude_if=_exclude_if,
    )
