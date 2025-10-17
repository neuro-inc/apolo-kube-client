from pydantic import BaseModel


__all__ = ("V1beta2CapacityRequestPolicyRange",)


class V1beta2CapacityRequestPolicyRange(BaseModel):
    max: str | None = None

    min: str | None = None

    step: str | None = None
