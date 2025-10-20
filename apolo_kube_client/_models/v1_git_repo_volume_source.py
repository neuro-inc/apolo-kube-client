from pydantic import BaseModel


__all__ = ("V1GitRepoVolumeSource",)


class V1GitRepoVolumeSource(BaseModel):
    directory: str | None = None

    repository: str | None = None

    revision: str | None = None
