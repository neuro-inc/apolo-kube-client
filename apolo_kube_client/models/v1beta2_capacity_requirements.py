from pydantic import BaseModel


__all__ = ("V1beta2CapacityRequirements",)


class V1beta2CapacityRequirements(BaseModel):
    requests: dict[str, str] = {}
