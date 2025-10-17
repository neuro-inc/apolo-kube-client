from pydantic import BaseModel


__all__ = ("V1beta1ServiceCIDRSpec",)


class V1beta1ServiceCIDRSpec(BaseModel):
    cidrs: list[str] = []
