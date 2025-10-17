from pydantic import BaseModel


__all__ = ("V1CapacityRequestPolicyRange",)


class V1CapacityRequestPolicyRange(BaseModel):
    max: str | None = None

    min: str | None = None

    step: str | None = None
