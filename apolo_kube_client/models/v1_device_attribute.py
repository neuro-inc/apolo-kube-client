from pydantic import BaseModel


__all__ = ("V1DeviceAttribute",)


class V1DeviceAttribute(BaseModel):
    bool: bool | None = None

    int: int | None = None

    string: str | None = None

    version: str | None = None
