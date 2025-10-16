from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("VersionInfo",)


class VersionInfo(BaseModel):
    build_date: str | None = Field(default_factory=lambda: None, alias="buildDate")

    compiler: str | None = Field(default_factory=lambda: None, alias="compiler")

    emulation_major: str | None = Field(
        default_factory=lambda: None, alias="emulationMajor"
    )

    emulation_minor: str | None = Field(
        default_factory=lambda: None, alias="emulationMinor"
    )

    git_commit: str | None = Field(default_factory=lambda: None, alias="gitCommit")

    git_tree_state: str | None = Field(
        default_factory=lambda: None, alias="gitTreeState"
    )

    git_version: str | None = Field(default_factory=lambda: None, alias="gitVersion")

    go_version: str | None = Field(default_factory=lambda: None, alias="goVersion")

    major: str | None = Field(default_factory=lambda: None, alias="major")

    min_compatibility_major: str | None = Field(
        default_factory=lambda: None, alias="minCompatibilityMajor"
    )

    min_compatibility_minor: str | None = Field(
        default_factory=lambda: None, alias="minCompatibilityMinor"
    )

    minor: str | None = Field(default_factory=lambda: None, alias="minor")

    platform: str | None = Field(default_factory=lambda: None, alias="platform")
