from pydantic import BaseModel


__all__ = ("V1ResourceQuotaStatus",)


class V1ResourceQuotaStatus(BaseModel):
    hard: dict[str, str] = {}

    used: dict[str, str] = {}
