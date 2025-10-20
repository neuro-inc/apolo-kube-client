from pydantic import BaseModel


__all__ = ("V1NodeAddress",)


class V1NodeAddress(BaseModel):
    address: str | None = None

    type: str | None = None
