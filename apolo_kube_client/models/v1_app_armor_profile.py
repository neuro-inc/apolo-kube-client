from pydantic import BaseModel, Field


class V1AppArmorProfile(BaseModel):
    localhost_profile: str | None = Field(None, alias="localhostProfile")

    type: str | None = Field(None, alias="type")
