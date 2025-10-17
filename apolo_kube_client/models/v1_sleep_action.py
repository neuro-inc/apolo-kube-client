from pydantic import BaseModel


__all__ = ("V1SleepAction",)


class V1SleepAction(BaseModel):
    seconds: int | None = None
