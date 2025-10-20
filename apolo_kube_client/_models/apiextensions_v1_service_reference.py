from pydantic import BaseModel


__all__ = ("ApiextensionsV1ServiceReference",)


class ApiextensionsV1ServiceReference(BaseModel):
    name: str | None = None

    namespace: str | None = None

    path: str | None = None

    port: int | None = None
