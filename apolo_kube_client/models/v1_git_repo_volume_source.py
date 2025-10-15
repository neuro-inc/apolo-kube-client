from pydantic import BaseModel, Field


class V1GitRepoVolumeSource(BaseModel):
    directory: str | None = Field(None, alias="directory")

    repository: str | None = Field(None, alias="repository")

    revision: str | None = Field(None, alias="revision")
