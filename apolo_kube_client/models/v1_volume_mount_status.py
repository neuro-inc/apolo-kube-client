from pydantic import BaseModel, Field


class V1VolumeMountStatus(BaseModel):
    mount_path: str | None = Field(None, alias="mountPath")

    name: str | None = Field(None, alias="name")

    read_only: bool | None = Field(None, alias="readOnly")

    recursive_read_only: str | None = Field(None, alias="recursiveReadOnly")
