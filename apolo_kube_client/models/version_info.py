from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("VersionInfo",)


class VersionInfo(BaseModel):
    build_date: str | None = Field(
        default=None,
        serialization_alias="buildDate",
        validation_alias=AliasChoices("build_date", "buildDate"),
    )

    compiler: str | None = Field(default=None)

    emulation_major: str | None = Field(
        default=None,
        serialization_alias="emulationMajor",
        validation_alias=AliasChoices("emulation_major", "emulationMajor"),
    )

    emulation_minor: str | None = Field(
        default=None,
        serialization_alias="emulationMinor",
        validation_alias=AliasChoices("emulation_minor", "emulationMinor"),
    )

    git_commit: str | None = Field(
        default=None,
        serialization_alias="gitCommit",
        validation_alias=AliasChoices("git_commit", "gitCommit"),
    )

    git_tree_state: str | None = Field(
        default=None,
        serialization_alias="gitTreeState",
        validation_alias=AliasChoices("git_tree_state", "gitTreeState"),
    )

    git_version: str | None = Field(
        default=None,
        serialization_alias="gitVersion",
        validation_alias=AliasChoices("git_version", "gitVersion"),
    )

    go_version: str | None = Field(
        default=None,
        serialization_alias="goVersion",
        validation_alias=AliasChoices("go_version", "goVersion"),
    )

    major: str | None = Field(default=None)

    min_compatibility_major: str | None = Field(
        default=None,
        serialization_alias="minCompatibilityMajor",
        validation_alias=AliasChoices(
            "min_compatibility_major", "minCompatibilityMajor"
        ),
    )

    min_compatibility_minor: str | None = Field(
        default=None,
        serialization_alias="minCompatibilityMinor",
        validation_alias=AliasChoices(
            "min_compatibility_minor", "minCompatibilityMinor"
        ),
    )

    minor: str | None = Field(default=None)

    platform: str | None = Field(default=None)
