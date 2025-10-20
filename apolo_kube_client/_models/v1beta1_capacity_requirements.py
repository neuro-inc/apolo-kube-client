from pydantic import BaseModel


__all__ = ("V1beta1CapacityRequirements",)


class V1beta1CapacityRequirements(BaseModel):
    requests: dict[str, str] = {}
