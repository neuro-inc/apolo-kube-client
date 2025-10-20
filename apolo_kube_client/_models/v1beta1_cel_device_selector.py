from pydantic import BaseModel


__all__ = ("V1beta1CELDeviceSelector",)


class V1beta1CELDeviceSelector(BaseModel):
    expression: str | None = None
