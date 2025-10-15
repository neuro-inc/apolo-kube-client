from pydantic import BaseModel, Field


class V1SELinuxOptions(BaseModel):
    level: str | None = Field(None, alias="level")

    role: str | None = Field(None, alias="role")

    type: str | None = Field(None, alias="type")

    user: str | None = Field(None, alias="user")
