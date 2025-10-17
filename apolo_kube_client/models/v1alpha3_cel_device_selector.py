from pydantic import BaseModel


__all__ = ("V1alpha3CELDeviceSelector",)


class V1alpha3CELDeviceSelector(BaseModel):
    expression: str | None = None
