from pydantic import BaseModel


__all__ = ("V1PodDNSConfigOption",)


class V1PodDNSConfigOption(BaseModel):
    name: str | None = None

    value: str | None = None
