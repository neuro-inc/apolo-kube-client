from pydantic import BaseModel, Field


class V1NFSVolumeSource(BaseModel):
    path: str | None = Field(None, alias="path")

    read_only: bool | None = Field(None, alias="readOnly")

    server: str | None = Field(None, alias="server")
