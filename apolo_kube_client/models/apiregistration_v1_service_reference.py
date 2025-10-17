from pydantic import BaseModel


__all__ = ("ApiregistrationV1ServiceReference",)


class ApiregistrationV1ServiceReference(BaseModel):
    name: str | None = None

    namespace: str | None = None

    port: int | None = None
