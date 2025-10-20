from pydantic import BaseModel


__all__ = ("V1beta1ParentReference",)


class V1beta1ParentReference(BaseModel):
    group: str | None = None

    name: str | None = None

    namespace: str | None = None

    resource: str | None = None
