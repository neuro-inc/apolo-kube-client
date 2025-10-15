from pydantic import BaseModel, Field


class V1SleepAction(BaseModel):
    seconds: int | None = Field(None, alias="seconds")
