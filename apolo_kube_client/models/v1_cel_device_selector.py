from pydantic import BaseModel


__all__ = ("V1CELDeviceSelector",)


class V1CELDeviceSelector(BaseModel):
    expression: str | None = None
