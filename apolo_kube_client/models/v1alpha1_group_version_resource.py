from pydantic import BaseModel


__all__ = ("V1alpha1GroupVersionResource",)


class V1alpha1GroupVersionResource(BaseModel):
    group: str | None = None

    resource: str | None = None

    version: str | None = None
