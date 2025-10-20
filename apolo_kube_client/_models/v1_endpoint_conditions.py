from pydantic import BaseModel


__all__ = ("V1EndpointConditions",)


class V1EndpointConditions(BaseModel):
    ready: bool | None = None

    serving: bool | None = None

    terminating: bool | None = None
