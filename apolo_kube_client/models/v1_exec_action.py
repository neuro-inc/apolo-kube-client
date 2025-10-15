from pydantic import BaseModel, Field


class V1ExecAction(BaseModel):
    command: list[str] | None = Field(None, alias="command")
