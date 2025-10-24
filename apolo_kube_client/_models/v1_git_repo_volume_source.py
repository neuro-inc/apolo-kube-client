from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1GitRepoVolumeSource",)


class V1GitRepoVolumeSource(BaseModel):
    """Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.

    DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.GitRepoVolumeSource"

    directory: Annotated[
        str | None,
        Field(
            description="""directory is the target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    repository: Annotated[str, Field(description="""repository is the URL""")]

    revision: Annotated[
        str | None,
        Field(
            description="""revision is the commit hash for the specified revision.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
