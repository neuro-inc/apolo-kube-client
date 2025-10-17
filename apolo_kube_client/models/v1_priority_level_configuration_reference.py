from pydantic import BaseModel


__all__ = ("V1PriorityLevelConfigurationReference",)


class V1PriorityLevelConfigurationReference(BaseModel):
    name: str | None = None
