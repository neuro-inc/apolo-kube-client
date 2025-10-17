from pydantic import BaseModel


__all__ = ("V1ServiceCIDRSpec",)


class V1ServiceCIDRSpec(BaseModel):
    cidrs: list[str] = []
