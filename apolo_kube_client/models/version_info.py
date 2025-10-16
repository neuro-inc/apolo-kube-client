from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("VersionInfo",)


class VersionInfo(BaseModel):
    build_date: str | None = Field(None, alias="buildDate")

    compiler: str | None = Field(None, alias="compiler")

    git_commit: str | None = Field(None, alias="gitCommit")

    git_tree_state: str | None = Field(None, alias="gitTreeState")

    git_version: str | None = Field(None, alias="gitVersion")

    go_version: str | None = Field(None, alias="goVersion")

    major: str | None = Field(None, alias="major")

    minor: str | None = Field(None, alias="minor")

    platform: str | None = Field(None, alias="platform")
