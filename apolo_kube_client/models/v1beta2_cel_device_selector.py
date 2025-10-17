from pydantic import BaseModel


__all__ = ("V1beta2CELDeviceSelector",)


class V1beta2CELDeviceSelector(BaseModel):
    expression: str | None = None
