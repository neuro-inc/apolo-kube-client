from pydantic import BaseModel
from .core_v1_resource_claim import CoreV1ResourceClaim

__all__ = ("V1ResourceRequirements",)


class V1ResourceRequirements(BaseModel):
    claims: list[CoreV1ResourceClaim] = []

    limits: dict[str, str] = {}

    requests: dict[str, str] = {}
