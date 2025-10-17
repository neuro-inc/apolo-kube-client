from pydantic import BaseModel


__all__ = ("V1GRPCAction",)


class V1GRPCAction(BaseModel):
    port: int | None = None

    service: str | None = None
