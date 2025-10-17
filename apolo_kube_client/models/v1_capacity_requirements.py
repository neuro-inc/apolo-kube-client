from pydantic import BaseModel


__all__ = ("V1CapacityRequirements",)


class V1CapacityRequirements(BaseModel):
    requests: dict[str, str] = {}
