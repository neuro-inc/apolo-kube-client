from pydantic import BaseModel


__all__ = ("V1Capabilities",)


class V1Capabilities(BaseModel):
    add: list[str] = []

    drop: list[str] = []
