from pydantic import BaseModel


__all__ = ("V1EventSource",)


class V1EventSource(BaseModel):
    component: str | None = None

    host: str | None = None
