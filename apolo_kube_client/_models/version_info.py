from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("VersionInfo",)


class VersionInfo(BaseModel):
    build_date: str | None = Field(
        default=None,
        serialization_alias="buildDate",
        validation_alias=AliasChoices("build_date", "buildDate"),
        exclude_if=_exclude_if,
    )

    compiler: str | None = Field(default=None, exclude_if=_exclude_if)

    emulation_major: str | None = Field(
        default=None,
        serialization_alias="emulationMajor",
        validation_alias=AliasChoices("emulation_major", "emulationMajor"),
        exclude_if=_exclude_if,
    )

    emulation_minor: str | None = Field(
        default=None,
        serialization_alias="emulationMinor",
        validation_alias=AliasChoices("emulation_minor", "emulationMinor"),
        exclude_if=_exclude_if,
    )

    git_commit: str | None = Field(
        default=None,
        serialization_alias="gitCommit",
        validation_alias=AliasChoices("git_commit", "gitCommit"),
        exclude_if=_exclude_if,
    )

    git_tree_state: str | None = Field(
        default=None,
        serialization_alias="gitTreeState",
        validation_alias=AliasChoices("git_tree_state", "gitTreeState"),
        exclude_if=_exclude_if,
    )

    git_version: str | None = Field(
        default=None,
        serialization_alias="gitVersion",
        validation_alias=AliasChoices("git_version", "gitVersion"),
        exclude_if=_exclude_if,
    )

    go_version: str | None = Field(
        default=None,
        serialization_alias="goVersion",
        validation_alias=AliasChoices("go_version", "goVersion"),
        exclude_if=_exclude_if,
    )

    major: str | None = Field(default=None, exclude_if=_exclude_if)

    min_compatibility_major: str | None = Field(
        default=None,
        serialization_alias="minCompatibilityMajor",
        validation_alias=AliasChoices(
            "min_compatibility_major", "minCompatibilityMajor"
        ),
        exclude_if=_exclude_if,
    )

    min_compatibility_minor: str | None = Field(
        default=None,
        serialization_alias="minCompatibilityMinor",
        validation_alias=AliasChoices(
            "min_compatibility_minor", "minCompatibilityMinor"
        ),
        exclude_if=_exclude_if,
    )

    minor: str | None = Field(default=None, exclude_if=_exclude_if)

    platform: str | None = Field(default=None, exclude_if=_exclude_if)
