from pydantic import BaseModel


__all__ = ("AdmissionregistrationV1ServiceReference",)


class AdmissionregistrationV1ServiceReference(BaseModel):
    name: str | None = None

    namespace: str | None = None

    path: str | None = None

    port: int | None = None
