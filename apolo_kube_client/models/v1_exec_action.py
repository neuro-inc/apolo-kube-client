from pydantic import BaseModel


__all__ = ("V1ExecAction",)


class V1ExecAction(BaseModel):
    command: list[str] = []
