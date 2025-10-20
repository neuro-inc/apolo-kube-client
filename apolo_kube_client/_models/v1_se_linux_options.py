from pydantic import BaseModel


__all__ = ("V1SELinuxOptions",)


class V1SELinuxOptions(BaseModel):
    level: str | None = None

    role: str | None = None

    type: str | None = None

    user: str | None = None
