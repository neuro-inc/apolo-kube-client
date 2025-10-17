from pydantic import BaseModel


__all__ = ("V1PodFailurePolicyOnPodConditionsPattern",)


class V1PodFailurePolicyOnPodConditionsPattern(BaseModel):
    status: str | None = None

    type: str | None = None
