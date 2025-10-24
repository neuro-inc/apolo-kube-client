from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("VersionInfo",)


class VersionInfo(BaseModel):
    """Info contains versioning information. how we'll want to distribute that information."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.apimachinery.pkg.version.Info"

    build_date: Annotated[str, Field(alias="buildDate")]

    compiler: Annotated[str, Field()]

    emulation_major: Annotated[
        str | None,
        Field(
            alias="emulationMajor",
            description="""EmulationMajor is the major version of the emulation version""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    emulation_minor: Annotated[
        str | None,
        Field(
            alias="emulationMinor",
            description="""EmulationMinor is the minor version of the emulation version""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    git_commit: Annotated[str, Field(alias="gitCommit")]

    git_tree_state: Annotated[str, Field(alias="gitTreeState")]

    git_version: Annotated[str, Field(alias="gitVersion")]

    go_version: Annotated[str, Field(alias="goVersion")]

    major: Annotated[
        str, Field(description="""Major is the major version of the binary version""")
    ]

    min_compatibility_major: Annotated[
        str | None,
        Field(
            alias="minCompatibilityMajor",
            description="""MinCompatibilityMajor is the major version of the minimum compatibility version""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    min_compatibility_minor: Annotated[
        str | None,
        Field(
            alias="minCompatibilityMinor",
            description="""MinCompatibilityMinor is the minor version of the minimum compatibility version""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    minor: Annotated[
        str, Field(description="""Minor is the minor version of the binary version""")
    ]

    platform: Annotated[str, Field()]
