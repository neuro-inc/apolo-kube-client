from pydantic import BaseModel


__all__ = ("V1HTTPHeader",)


class V1HTTPHeader(BaseModel):
    name: str | None = None

    value: str | None = None
