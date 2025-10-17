from pydantic import BaseModel


__all__ = ("V1ContainerRestartRuleOnExitCodes",)


class V1ContainerRestartRuleOnExitCodes(BaseModel):
    operator: str | None = None

    values: list[int] = []
